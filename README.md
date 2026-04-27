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

## 📖 Mục lục
- [Thông tin môn học](#-thông-tin-môn-học)
- [Giới thiệu Đồ án](#-giới-thiệu-đồ-án)
- [Thông tin thành viên](#-thành-viên)
- [Nhiệm vụ chính](#️-nhiệm-vụ-chính)
- [Cấu trúc đồ án](#️-cấu-trúc-đồ-án)

---
---
## 📚 Thông tin môn học
- **Tên môn học:** Nhập môn Thị giác Máy tính (CS231)
- **Mã môn học:** CS231 - Lớp: CS231.Q23
- **Năm học:** 2025 - 2026
- **Giảng viên:** TS. Mai Tiến Dũng
- Môn học được giảng dạy tại Trường Đại học Công nghệ Thông tin - Đại học Quốc gia Thành phố Hồ Chí Minh
## 📝 Giới thiệu Đồ án

Dự án tập trung vào bài toán **Fine-Grained Visual Categorization (FGVC)** - phân loại chi tiết 150 loài chim trên tập dữ liệu Birds-525. Áp dụng và so sánh nhiều phương pháp từ truyền thống đến các kiến trúc SOTA (State-of-the-Art) như **VGG16**, **Bilinear CNN (B-CNN)**, **Vision Transformer (ViT)** và **Contrastive Language-Image Pre-training (CLIP)** để tìm ra giải pháp tối ưu cho việc nhận diện các đặc trưng nhỏ giữa các loài chim có độ tương đồng cao.

---

## 👥 Thành viên
| **Student ID** | **Member**          | **Email**                    |
|----------------|---------------------|------------------------------|
| 24520101       | Nguyen Duy Hoàng Anh     | 24520101@gm.uit.edu.vn       |
| 24520034       | Nguyễn Ngọc Anh Tuấn       | 24520034@gm.uit.edu.vn       |
| 24520704       | Trần Nguyễn Lâm Huy       | 24520704@gm.uit.edu.vn       |
| 24521796       | Nguyễn Bá Toàn       | 24521796@gm.uit.edu.vn       |

---

---

## 🏗️ Nhiệm vụ chính

Cài đặt và triển các thuật toán Thị giác Máy tính như:
- Xử lý và tăng cường dữ liệu.
- Rút trích đặc trưng (feature extract) qua các mô hình:
  - VGG16
  - CLIP (Contrastive Language-Image Pre-training)
  - ViT (Vision Transformer)
  - Custom Bilinear CNN (B-CNN)
- Tìm tham số tối ưu bằng GridSearchCV
- Sử dụng mô hình phân loại Random Forest để huấn luyện mô hình
- Đánh giá mô hình qua các phương pháp rút trích đặc trưng.
- Xây dựng demo với từng loại mô hình

## 💻 Cấu trúc đồ án
- `./docs/`: Lưu trữ tài liệu báo cáo và slide trình bày

- `./notebooks/`: Các notebook Jupyter phục vụ phân tích và thử nghiệm

- `DATASET.md':  Bộ dữ liệu 150 loài chim đã được tăng cương và chưa được tăng cường.
