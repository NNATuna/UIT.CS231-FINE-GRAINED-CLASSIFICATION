- **Công việc chung (Data Augmentation):** Thực hiện tăng cường dữ liệu cho tập Birds-525 nhằm cân bằng dữ liệu giữa 150 lớp bằng các phép xoay, lật, thay đổi độ sáng,... Đồng thời xây dựng pipeline dữ liệu chuẩn để cả nhóm sử dụng chung.

- **Xây dựng backbone trích xuất đặc trưng:** Cài đặt mô hình VGG16 pretrained trên ImageNet để trích xuất đặc trưng từ ảnh chim.

- **Xây dựng mô hình phân loại:**
- 1. Kết hợp backbone VGG16 với classifier head gồm GlobalAveragePooling2D, Dropout và Dense Softmax để thực hiện phân loại loài chim.
  2. Kết hợp backbone VGG16 với mô hình phân loại randomforest, tìm bộ tham số tốt nhất bằng gridsearch để thực hiện phân loại loài chim
