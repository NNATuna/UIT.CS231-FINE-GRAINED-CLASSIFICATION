- **Công việc chung (B-CNN Architecture):** Xây dựng và huấn luyện mô hình Bilinear CNN (B-CNN) từ
  đầu đến cuối (End-to-End). Đây là kiến trúc đặc thù cho bài toán Fine-Grained, tự trích xuất và phân loại
  mà không cần mô hình Machine Learning riêng biệt.
- **Trích xuất đặc trưng truyền thống:** Cài đặt SIFT (Scale-Invariant Feature Transform) kết hợp Bag of
  Visual Words.
- **Trích xuất đặc trưng Học sâu:** Cài đặt EfficientNetV2 (dòng CNN tiên tiến nhất hiện nay) để rút trích
  vector đặc trưng.
- **Mô hình phân loại (cho SIFT & EfficientNet):** Sử dụng Random Forest để làm "bệ đỡ" so sánh trực
  tiếp với hiệu năng của mạng B-CNN (End-to-End).
