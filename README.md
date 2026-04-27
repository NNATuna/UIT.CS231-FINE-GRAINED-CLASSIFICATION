<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology" width="300">
  </a>
</p>


<h1 align="center">CS231 - COMPUTER VISION</h1>
<h3 align="center">Đồ án: Phân loại chi tiết loài chim (Fine-Grained Visual Categorization)</h3>

<p align="center">
  <img src="https://img.shields.io/badge/University-UIT-blueviolet" alt="UIT">
  <img src="https://img.shields.io/badge/Semester-2%202025--2026-green" alt="Semester">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

---

## 📌 Tổng quan Đồ án
Dự án giải quyết bài toán **Fine-Grained Visual Categorization (FGVC)** trên tập dữ liệu **Birds-525**. Mục tiêu trọng tâm là phân biệt 150 loài chim có độ tương đồng cao về hình thái, nơi các đặc trưng nhỏ như mỏ, vân lông hay hình dạng chân đóng vai trò quyết định.

Nhóm đã thực nghiệm và so sánh hiệu năng giữa các kiến trúc mạng nơ-ron tích chập (CNN) truyền thống và các mô hình dựa trên Transformer hiện đại để tìm ra sự cân bằng giữa độ chính xác và tài nguyên tính toán.

---

## 🛠️ Phương pháp tiếp cận
Dự án triển khai quy trình trích xuất đặc trưng (Feature Extraction) kết hợp với bộ phân loại học máy truyền thống:

**Kiến trúc Backbone:**
  - **VGG16:** Mô hình cơ bản để thiết lập baseline.
  - **EfficientNetB0:** Tối ưu hóa giữa hiệu suất và tham số.
  - **Vision Transformer (ViT-B/16):** Khai thác cơ chế Self-attention để nắm bắt đặc trưng toàn cục. 
  - **CLIP (Visual Encoder):** Học biểu diễn hình ảnh từ không gian ngôn ngữ. 
**Bộ phân loại:** **Random Forest** kết hợp **GridSearchCV** để tối ưu hóa siêu tham số. 
**Xử lý dữ liệu:** Kỹ thuật **Data Augmentation** giúp cân bằng mẫu và tăng tính vững (Robustness) cho mô hình.

---

## 👥 Thành viên thực hiện
| MSSV | Họ và tên | Vai trò chính |
| :--- | :--- | :--- |
| **24520034** | **Nguyễn Ngọc Anh Tuấn** | Chia tập dữ liệu, rút trích đặc trưng EfficientNetB0 và sử dụng mô hình phân loại RandomForest.  Hoàn thành báo cáo, slide và thực hiện demo trên |
| **24520704** | **Trần Nguyễn Lâm Huy** | Tăng cường dữ liệu, rút trích đặc trưng VGG16 và sử dụng mô hình phân loại RandomForest.  Hoàn thành báo cáo, slide và thực hiện demo trên VGG16 |
| **24520101** | **Nguyễn Duy Hoàng Anh** | Thu thập và tổng hợp dữ liệu, rút trích đặc trưng bằng CLIP, tìm tham số bằng GridSearchCV, sử dụng mô hình phân loại RandomForest.  Hoàn thành báo cáo, slide và thực hiện demo trên CLIP ViT-B/32 |
| **24521796** | **Nguyễn Bá Toàn** | Thu thập dữ liệu, rút trích đặc trưng bằng Vision Transformer và sử dụng mô hình phân loại RandomForest.  Hoàn thành báo cáo, slide và thực hiện demo trên ViT-B/16 |

---

## 📂 Cấu trúc thư mục
```bash
├── docs/           # Tài liệu báo cáo (PDF), Slide thuyết trình và Hình ảnh minh họa.
├── notebooks/      # Jupyter Notebooks thực hiện huấn luyện, GridSearch và Evaluation.
└── README.md       # Giới thiệu dự án.
```

---

## 🎓 Thông tin môn học
**Môn học:** Nhập môn Thị giác Máy tính (CS231.Q23) 
**Đơn vị:** Khoa Khoa học Máy tính - Trường Đại học Công nghệ Thông tin (VNU-HCM).

---
*Dự án đạt độ chính xác xấp xỉ **96%** với phương pháp ViT-B/16 kết hợp Random Forest trên tập kiểm tra.*
