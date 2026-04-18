- **Công việc chung (Demo Application):** Xây dựng giao diện web Demo (bằng Gradio hoặc Streamlit)
  cho phép tải ảnh lên và nhận dự đoán từ các mô hình tốt nhất của nhóm.
- **Trích xuất đặc trưng truyền thống:** Cài đặt LBP (Local Binary Pattern) hoặc SURF để bắt đặc trưng kết
  cấu lông chim.
- **Trích xuất đặc trưng Học sâu:** Cài đặt OpenAI-CLIP (Mô hình đa phương thức). Sử dụng Image Encoder để trích xuất zero-shot embedding.
- **Mô hình phân loại:** Sử dụng Custom Neural Network (hoặc Random Forest, tùy bạn này chọn) để huấn luyện đầu ra cho CLIP và LBP.
