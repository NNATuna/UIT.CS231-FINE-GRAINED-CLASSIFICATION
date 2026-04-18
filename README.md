<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology" width="300">
  </a>
</p>

<h1 align="center">CS231 - Computer Vision</h1>

<p align="center">
  <img src="https://img.shields.io/badge/University-UIT-blueviolet" alt="UIT">
  <img src="https://img.shields.io/badge/Semester-2%202025--2026-green" alt="Semester">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

---

## 📝 Giới thiệu Đồ án

Dự án tập trung vào bài toán **Fine-Grained Visual Categorization (FGVC)** - phân loại chi tiết 150 loài chim trên tập dữ liệu Birds-525. Áp dụng và so sánh nhiều phương pháp từ truyền thống đến các kiến trúc SOTA (State-of-the-Art) như **Bilinear CNN (B-CNN)**, **Vision Transformer (ViT)** và **CLIP** để tìm ra giải pháp tối ưu cho việc nhận diện các đặc trưng nhỏ giữa các loài chim có độ tương đồng cao.

---

## 👥 Thành viên

| Thành viên   | Vai trò                     | Nhiệm vụ trọng tâm                                                    |
| :----------- | :-------------------------- | :-------------------------------------------------------------------- |
| **Member 1** | Kỹ sư Tiền xử lý & Baseline | Data Augmentation, HOG, VGG16 + Random Forest Baseline.               |
| **Member 2** | Đánh giá & SOTA             | Vision Transformer (ViT), Color Histogram, Evaluation Metrics.        |
| **Member 3** | CNN & End-to-End            | **Custom Bilinear CNN (B-CNN)**, EfficientNetV2, End-to-End Training. |
| **Member 4** | Ứng dụng & CLIP             | OpenAI-CLIP (Zero-shot), LBP Features, Gradio/Streamlit App.          |

---

## 🏗️ Cấu trúc thư mục dự án

Hệ thống được tổ chức dạng Modular Notebooks để tối ưu trên môi trường Cloud (Colab/Kaggle):

```text
CS231-FINE-GRAINED-CLASSIFICATION/
├── notebooks/
│   ├── Member_1/           # Preprocessing & Baseline (VGG16)
│   ├── Member_2/           # Transformer (ViT) & Metrics
│   ├── Member_3/           # Modern CNN (B-CNN, EfficientNetV2)
│   └── Member_4/           # CLIP & Demo Application
├── results/                # Biểu đồ Accuracy/Loss & Confusion Matrix
├── docs/                   # File Báo cáo (PDF) & Slide thuyết trình
├── .gitignore              # Chặn dataset & weights nặng
└── README.md               # Tài liệu hướng dẫn chính
```
