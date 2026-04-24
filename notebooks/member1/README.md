CÔNG VIỆC:
- **Công việc chung (Data Augmentation):** Thực hiện Data Augmentation trên tập Birds-525 (cân bằng
  150 lớp bằng các phép xoay, lật, phóng to...). Xây dựng pipeline dữ liệu chuẩn để cả nhóm dùng chung.
- **Trích xuất đặc trưng truyền thống:** Cài đặt HOG (Histogram of Oriented Gradients) để bắt hình dáng
  chim.
- **Trích xuất đặc trưng Học sâu:** Cài đặt VGG16 (loại bỏ lớp Fully Connected) để rút trích vector đặc
  trưng.
- **Mô hình phân loại:** Sử dụng Random Forest (kết hợp Grid Search tối ưu siêu tham số) cho cả đặc
  trưng HOG và VGG16

HƯỚNG DẪN:
Download 2 file .pkl tại link đây: xxxxxxxxxxx (Chờ mai tao úp, hết 4g rồi :)))), di chuyển 2 file đó cùng vị trí với file app_final.py và label_map.json
CÁCH CHẠY app_final.py: python app_final.py
