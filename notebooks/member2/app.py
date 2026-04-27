import gradio as gr
import torch
import numpy as np
from PIL import Image
import time
import joblib
from transformers import AutoImageProcessor, ViTModel
import json
import os

# ========================= CONFIG =========================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Đang sử dụng: {device}")

MODEL_NAME = "google/vit-base-patch16-224-in21k"

# Load ViT
print("Đang tải ViT model...")
processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
vit_model = ViTModel.from_pretrained(MODEL_NAME)
vit_model = vit_model.to(device)
vit_model.eval()

# --- Tải Label Map (Từ file label_map.json của bạn) ---
try:
    with open("label_map.json", "r") as f:
        label_list = json.load(f)
    # Tạo dictionary mapping từ index sang tên loài
    idx_to_class = {i: name for i, name in enumerate(label_list)}
    print(f"Đã tải nhãn cho {len(idx_to_class)} loài chim.")
except Exception as e:
    print(f"Lỗi tải label_map.json: {e}")
    idx_to_class = {}

# Load 2 mô hình Random Forest
print("Đang tải 2 mô hình Random Forest...")
rf_aug = joblib.load("aug_random_forest.pkl")
rf_org = joblib.load("org_random_forest.pkl")

# ====================== HELPER FUNCTIONS ======================
def extract_vit_features(image: Image.Image):
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    inputs = processor(images=image, return_tensors="pt").pixel_values.to(device)
    
    with torch.no_grad():
        outputs = vit_model(pixel_values=inputs)
        features = outputs.last_hidden_state[:, 0, :].cpu().numpy()
    
    return features

def predict_with_model(image, rf_model, model_name):
    start_time = time.time()
    
    features = extract_vit_features(image)
    pred_idx = rf_model.predict(features)[0]
    pred_proba = rf_model.predict_proba(features)[0]
    
    confidence = float(pred_proba[pred_idx]) * 100
    pred_class_name = idx_to_class.get(pred_idx, "Không xác định")
    
    infer_time = (time.time() - start_time) * 1000  # ms
    
    return pred_class_name, f"{confidence:.2f}%", f"{infer_time:.1f} ms"

# ====================== GRADIO INTERFACE ======================
def compare_models(image):
    if image is None:
        return "Vui lòng upload ảnh!", "", "", "", "", ""
    
    aug_class, aug_conf, aug_time = predict_with_model(image, rf_aug, "Augmented")
    org_class, org_conf, org_time = predict_with_model(image, rf_org, "Original")
    
    result = f"""
**KẾT QUẢ SO SÁNH**

**1. Model Augmented (aug_random_forest.pkl)**  
→ Loài dự đoán: **{aug_class}**  
→ Độ tin cậy: **{aug_conf}**  
→ Thời gian: **{aug_time}**

**2. Model Original (org_random_forest.pkl)**  
→ Loài dự đoán: **{org_class}**  
→ Độ tin cậy: **{org_conf}**  
→ Thời gian: **{org_time}**
"""
    
    return result, aug_class, aug_conf, org_class, org_conf

# Giao diện Gradio
with gr.Blocks(title="Phân Loại 150 Loài Chim", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🐦 Phân Loại 150 Loài Chim\n**Vision Transformer (ViT-B/16) + Random Forest**")
    
    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(
                type="pil", 
                label="Upload ảnh chim cần phân loại", 
                height=400
            )
            btn = gr.Button("SUBMIT", variant="primary", size="large")
        
        with gr.Column(scale=1):
            output_text = gr.Markdown(label="Kết quả so sánh")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Augmented Model")
            aug_label = gr.Textbox(label="Loài dự đoán", interactive=False)
            aug_conf = gr.Textbox(label="Độ tin cậy", interactive=False)
        with gr.Column():
            gr.Markdown("### Original Model")
            org_label = gr.Textbox(label="Loài dự đoán", interactive=False)
            org_conf = gr.Textbox(label="Độ tin cậy", interactive=False)
    
    btn.click(
        fn=compare_models,
        inputs=input_image,
        outputs=[output_text, aug_label, aug_conf, org_label, org_conf]
    )
# ====================== CHẠY APP ======================
if __name__ == "__main__":
    demo.launch(share=True)