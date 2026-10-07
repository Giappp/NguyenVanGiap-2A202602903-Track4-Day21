# Báo cáo Day 6: [ĐIỀN tên đề tài ngắn]

> Thay **mọi** ô có chữ ĐIỀN nằm trong ngoặc vuông bằng nội dung của bạn, xoá luôn cả dấu ngoặc vuông. Lệnh `python tools/check_submission.py` sẽ báo FAIL nếu còn sót bất kỳ chỗ nào.

- **Họ tên:** Nguyễn Văn Giáp
- **MSSV:** 2A202602903
- **Lớp:** AI20K-T4
- **Link repo:** https://github.com/Giappp/NguyenVanGiap-2A202602903-Track4-Day21
- **Topic:** A - LiDAR-camera projection QA
- **Dataset:** data/kitti_mini
- **Các frame đã dùng:** 000008, 000011, 000049

> Hãy viết ngắn: mỗi mục từ 3 đến 8 dòng, ưu tiên số liệu và hình ảnh.

## 1. Claim

Một câu khẳng định kỹ thuật có thể kiểm chứng. Ví dụ: *"Lệch yaw 1° làm 12% điểm LiDAR rơi ra khỏi vật thể ở 30 m, phát hiện được bằng edge-alignment score với ngưỡng X."*

Trên ba frame KITTI `000008`, `000011`, `000049`, yaw drift tăng từ 0° lên 3° làm tỷ lệ trung bình theo frame của điểm LiDAR thuộc vật thể nằm trong 2D box giảm từ 99.44% xuống 62.18%; frame `000011` giảm còn 21.23%.

## 2. Evidence

Bảng hoặc plot số liệu, kèm ảnh/video demo. Ghi rõ đường dẫn file trong `results/`.

| Yaw drift | Điểm vật thể trong 2D box, trung bình 3 frame | Thấp nhất theo frame | Ghi chú |
|---|---|---|---|
| 0° | 99.44% | 99.25% | Baseline |
| 0.5° | 96.30% | 91.88% | Bắt đầu giảm ở frame `000011` |
| 1° | 89.85% | 77.44% | Khác biệt giữa các frame rõ hơn |
| 2° | 75.00% | 45.44% | Frame `000011` giảm mạnh |
| 3° | 62.18% | 21.23% | Frame `000011` là trường hợp nhạy nhất |

Metric là tỷ lệ trong các điểm thuộc 3D box GT và còn được chiếu vào ảnh, có pixel nằm trong 2D box GT. Giá trị trung bình là macro average trên ba frame; CSV lưu từng frame. Số điểm trong ảnh lần lượt khoảng 17.2–20.0 nghìn/frame và thay đổi ít theo sweep.

CSV: `results/yaw_perturb_sweep.csv`; biểu đồ: `results/figures/yaw_sweep.png`.

![yaw sweep](../results/figures/yaw_sweep.png)

## 3. Failure case

Nêu khi nào hệ thống hoặc phương pháp fail, vì sao fail, và liên hệ tới lớp nào trong 6 lớp debug: I/O, Geometry, Time, Preprocess, Model, Metric.

Ở frame `000011`, yaw drift `+3°` làm tỷ lệ điểm LiDAR thuộc vật thể nằm trong 2D box giảm từ `99.45%` (yaw `0°`) xuống `21.23%`; số điểm vật thể còn trong ảnh giảm từ 725 xuống 537. Điểm trong ảnh tổng thể gần như không đổi (19,946 → 19,948), nên lỗi chủ yếu là điểm trên vật thể bị chiếu lệch khỏi box, không phải mất toàn bộ điểm khỏi FOV. Đây là failure có chủ ý do **Geometry**: extrinsic sai trong khi box nhãn giữ nguyên. Số liệu chi tiết nằm ở `results/yaw_perturb_sweep.csv`.

![So sánh baseline và yaw drift 3 độ ở frame 000011](../results/figures/fail_02_yaw_3deg_000011.png)

## 4. Khuyến nghị nếu triển khai thật

Use-case cụ thể (ADAS / robot / drone), trade-off và bước tiếp theo.

[ĐIỀN]

## 5. Cách chạy lại

Các lệnh tái tạo lại toàn bộ kết quả từ repo sạch.

```bash
[ĐIỀN]
```

## 6. Khai báo sử dụng AI

Ghi rõ đã dùng công cụ AI nào, dùng vào việc gì, và bạn đã tự kiểm chứng kết quả đó bằng cách nào. Nếu không dùng AI, ghi "Không sử dụng". Xem quy định ở `RULES.md` mục 2.

| Công cụ | Dùng cho việc gì | Bạn đã kiểm chứng thế nào |
|---|---|---|
| ChatGPT | Tìm hiểu công thức, code mẫu triển khai | chạy pytest và đọc tài liệu do chatgpt cung cấp để kiểm chứng sự thật |
