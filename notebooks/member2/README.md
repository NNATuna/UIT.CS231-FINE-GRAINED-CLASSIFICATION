- Công việc chung (Evaluation & Metrics): Viết script tính toán các độ đo: Accuracy, Precision,Recall,Macro F1.Vẽ Ma trận nhầm lẫn (Confusion Matrix) để phân tích lỗi sâu các loài chim hay bị nhầm với
nhau.
- Trích xuất đặc trưng truyền thống: Cài đặt Color Histogram (trích xuất phân bố màu sắc lông chim).
- Trích xuất đặc trưng Học sâu: Cài đặt Vision Transformer (ViT-B/16) để trích xuất vector embedding
768 chiều.
- **Mô hình phân loại:** Thiết kế và huấn luyện Custom Neural Network (mạng Conv1D + MaxPool1D +
Linear layer) để phân loại dựa trên vector của ViT và Color Histogram.