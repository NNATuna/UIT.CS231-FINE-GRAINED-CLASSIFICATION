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

## 🧪 Thí nghiệm: Fine-tuning EfficientNetB0

Thư mục này tập trung vào việc nghiên cứu và đánh giá hiệu quả của **Fine-tuning trên EfficientNetB0** trong bài toán phân loại 150 loài chim.

Mục tiêu chính:
* So sánh các chiến lược **fine-tuning khác nhau**
* Đánh giá tác động của **data augmentation**
* Phân tích sự cân bằng giữa **overfitting** và **generalization**

---

### 🏗️ Kiến trúc & Phương pháp

Mô hình sử dụng:

1. **Backbone:** EfficientNetB0 (pre-trained trên ImageNet)
2. **Chiến lược huấn luyện:**
   * Freeze toàn bộ → train classifier
   * Fine-tune một phần (Block 7)
   * Fine-tune toàn bộ mô hình
3. **Dataset:**
   * Original Dataset
   * Augmented Dataset (tăng cường dữ liệu)

---

### 📂 Cấu trúc thư mục

Các file notebook tương ứng với từng thiết lập thí nghiệm:

#### 🔹 1. Fine-tuning một phần (Block 7)

* **`Eff_FT_block7_ORIG.ipynb`**
  * Fine-tune từ Block 7 trở đi
  * Dataset gốc (không augmentation)
  * Dùng để đánh giá baseline fine-tuning nhẹ

* **`Eff_FT_block7_AUG.ipynb`**
  * Fine-tune từ Block 7
  * Dataset đã augmentation
  * So sánh khả năng cải thiện generalization

---

#### 🔹 2. Fine-tuning toàn bộ mô hình

* **`Eff_FT_full_ORIG.ipynb`**
  * Unfreeze toàn bộ EfficientNetB0
  * Dataset gốc
  * Dễ overfit nhưng học đặc trưng sâu hơn

* **`Eff_FT_full_AUG.ipynb`**
  * Full fine-tuning + augmentation
  * Thiết lập cân bằng giữa bias và variance

---

#### 🔹 3. Training từ đầu với augmentation

* **`Eff_full_train_AUG.ipynb`**
  * Huấn luyện toàn bộ pipeline với dữ liệu augment
  * Không giữ nguyên hoàn toàn weights ban đầu
  * Kiểm tra khả năng học lại đặc trưng

---

### 🚀 Hướng dẫn sử dụng

#### 1. Yêu cầu hệ thống
* Python 3.10+
* TensorFlow / Keras
* NumPy, Matplotlib
* Google Colab (khuyến nghị GPU)

#### 2. Cách chạy
* Mở từng file `.ipynb` trên Colab
* Cập nhật đường dẫn dataset (`DATA_PATH`)
* Chạy tuần tự các cell:
  * Load dữ liệu
  * Build model
  * Train & evaluate

---

### 📊 Nhận xét chính

* **Fine-tuning một phần (Block 7)**:
  * Nhanh, ít overfitting
  * Phù hợp khi dataset không quá lớn

* **Fine-tuning toàn bộ**:
  * Hiệu năng cao hơn nếu có đủ dữ liệu
  * Dễ overfit nếu không có augmentation

* **Data Augmentation**:
  * Cải thiện rõ rệt khả năng tổng quát hóa
  * Đặc biệt hiệu quả với bài toán nhiều lớp

---

### 👤 Thông tin tác giả
* **Họ và tên:** Nguyễn Ngọc Anh Tuấn
* **Đơn vị:** Trường Đại học Công nghệ Thông tin - ĐHQG TP.HCM (UIT)
* **Lĩnh vực quan tâm:** Computer Vision, TinyML, Edge AI

---

<p align="right">(<a href="#top">back to top</a>)</p>