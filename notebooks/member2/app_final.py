import gradio as gr
import torch
import numpy as np
import cv2
import joblib
import json
from PIL import Image
from transformers import AutoImageProcessor, ViTModel

# ==========================================
# 1. CẤU HÌNH VÀ TẢI DỮ LIỆU
# ==========================================
print("Đang khởi tạo hệ thống...")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

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

# --- Tải ViT Model ---
MODEL_NAME = "google/vit-base-patch16-224-in21k"
processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
vit_model = ViTModel.from_pretrained(MODEL_NAME).to(device)
vit_model.eval()

# --- Tải các file Random Forest (.pkl) ---
try:
    rf_vit = joblib.load("ViT.pkl") # File train bằng ViT
    rf_color = joblib.load("Color_Histogram.pkl")    # File train bằng Color Histogram
    print("Đã tải xong các mô hình Random Forest.")
except Exception as e:
    print(f"Lỗi tải file .pkl: {e}")

# ==========================================
# 2. HÀM RÚT TRÍCH ĐẶC TRƯNG (Khớp với Notebook)
# ==========================================

def extract_vit_feature(image):
    """Rút trích vector 768 chiều từ ViT (CLS Token)"""
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    inputs = processor(images=image, return_tensors="pt")
    pixel_values = inputs.pixel_values.to(device)
    
    with torch.no_grad():
        outputs = vit_model(pixel_values=pixel_values)
        cls_features = outputs.last_hidden_state[:, 0, :]
    
    return cls_features.cpu().numpy()

def extract_color_histogram(image, bins=(8, 8, 8)):
    """Rút trích vector 512 chiều từ HSV Histogram (Y hệt Notebook)"""
    # Chuyển PIL Image sang OpenCV BGR
    img_np = np.array(image.convert("RGB"))
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    
    # Chuyển sang HSV
    hsv_image = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    
    # Tính 3D Histogram (H: 0-180, S: 0-256, V: 0-256)
    hist = cv2.calcHist([hsv_image], [0, 1, 2], None, bins, [0, 180, 0, 256, 0, 256])
    
    # Chuẩn hóa và flatten
    cv2.normalize(hist, hist)
    return hist.flatten().reshape(1, -1)

# ==========================================
# 3. HÀM DỰ ĐOÁN CHÍNH
# ==========================================

def predict_bird(image, method):
    if image is None: return "Vui lòng chọn ảnh!"
    
    if method == "Sử dụng ViT (Độ chính xác cao)":
        features = extract_vit_feature(image)
        model = rf_vit
    else:
        features = extract_color_histogram(image)
        model = rf_color
    
    # Dự đoán index
    pred_idx = model.predict(features)[0]
    
    # Lấy tên từ label_map
    bird_name = idx_to_class.get(pred_idx, f"Unknown ID: {pred_idx}")
    
    # Tính độ tự tin (%)
    probs = model.predict_proba(features)
    confidence = np.max(probs) * 100
    
    return f"Loài chim dự đoán: {bird_name}\nĐộ tin cậy: {confidence:.2f}%"

# ==========================================
# 4. GIAO DIỆN GRADIO
# ==========================================

with gr.Blocks(title="Bird Classifier Test") as demo:
    gr.Markdown("# 🦅 Hệ thống Phân loại Loài chim")
    gr.Markdown("Kiểm tra mô hình Random Forest được huấn luyện bằng ViT-B/16 và Color Histogram.")
    
    with gr.Row():
        with gr.Column():
            img_input = gr.Image(type="pil", label="Ảnh đầu vào")
            method_input = gr.Radio(
                ["Sử dụng ViT (Độ chính xác cao)", "Sử dụng Color Histogram (HSV)"], 
                label="Chọn phương pháp trích đặc trưng",
                value="Sử dụng ViT (Độ chính xác cao)"
            )
            btn = gr.Button("Dự đoán", variant="primary")
        
        with gr.Column():
            output_text = gr.Textbox(label="Kết quả dự đoán", lines=5)

    btn.click(fn=predict_bird, inputs=[img_input, method_input], outputs=output_text)

if __name__ == "__main__":
    demo.launch()