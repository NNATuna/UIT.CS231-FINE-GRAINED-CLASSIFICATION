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

## 🐦 Dự án: Phân loại 150 loài chim (Bird Species Classification)

Dự án này tập trung vào việc xây dựng một Pipeline hiệu quả kết hợp giữa **Deep Learning** (để trích xuất đặc trưng) và **Machine Learning truyền thống** (để phân loại). Mục tiêu là tối ưu hóa độ chính xác trên bộ dữ liệu gồm 20.080 hình ảnh của 150 loài chim khác nhau.

### 🏗️ Kiến trúc Model
Mô hình sử dụng phương pháp **Hybrid Architecture**:
1. **Feature Extractor:** EfficientNetB0 (Pre-trained trên ImageNet) trích xuất đặc trưng 1280 chiều.
2. **Dimensionality Reduction:** Sử dụng PCA để giảm số chiều (tùy chọn).
3. **Classifier:** Random Forest Classifier để thực hiện phân loại cuối cùng.

---

### 📂 Cấu trúc thư mục

Thư mục bao gồm 3 file chính đại diện cho các giai đoạn thử nghiệm của dự án:

1.  **`Eff_RF_Clean_ORIG.ipynb`**: 
    * Sử dụng dữ liệu gốc (Original Dataset).
    * Quy trình: Load Data -> EfficientNetB0 Features -> Random Forest.
    * Dùng làm mốc (Baseline) để so sánh hiệu năng.

2.  **`Eff_RF_Clean_AUG.ipynb`**:
    * Sử dụng dữ liệu đã qua tăng cường (**Augmented Data**) để cải thiện khả năng tổng quát hóa của mô hình.
    * Xử lý các vấn đề về Overfitting khi làm việc với số lượng loài lớn.

3.  **`Demo.ipynb`**:
    * File demo hoàn chỉnh tích hợp giao diện người dùng bằng **Gradio**.
    * Cho phép người dùng upload ảnh chim và nhận kết quả dự đoán trực quan ngay trên trình duyệt.

---

### 🚀 Hướng dẫn sử dụng

#### 1. Yêu cầu hệ thống
* Python 3.10+
* TensorFlow 2.19.0
* Scikit-learn, Joblib, Gradio
* Google Colab (Khuyên dùng để có hỗ trợ GPU/TPU)

#### 2. Cách chạy
* Mở các file `.ipynb` trên Google Colab.
* Thay đổi đường dẫn `DATA_PATH` tới thư mục chứa dataset trong Drive của bạn.
* Chạy tuần tự các Cell để huấn luyện hoặc thực hiện Demo.

---

### 📊 Kết quả nghiên cứu
* **Kiến trúc:** Khối MBConv trong EfficientNet giúp tối ưu hóa việc trích xuất đặc trưng mà vẫn giữ được số lượng tham số thấp, phù hợp cho các bài toán Computer Vision hiện đại.
* **Kỹ thuật:** Việc kết hợp đặc trưng từ Deep Learning vào Random Forest giúp mô hình tận dụng được sức mạnh của mạng tích chập và khả năng phân loại mạnh mẽ của Ensemble Learning.

---

### 👤 Thông tin tác giả
* **Họ và tên:** Nguyễn Ngọc Anh Tuấn
* **Đơn vị:** Trường Đại học Công nghệ Thông tin - ĐHQG TP.HCM (UIT)
* **Lĩnh vực quan tâm:** Computer Vision, TinyML, Edge AI.

---
<p align="right">(<a href="#top">back to top</a>)</p>
