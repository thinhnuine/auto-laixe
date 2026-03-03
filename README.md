# Auto Click – Ôn luyện tự động

## Cài đặt

```bash
cd auto-click
python3 -m venv venv
source venv/bin/activate   # macOS/Linux. Windows: venv\Scripts\activate
pip install pyautogui
```

Nếu thiếu thư viện ảnh:

```bash
pip install opencv-python pillow
```

## Cách chạy

### auto_press.py — Ôn luyện (phím 1–4, Tiếp, Kết thúc, Luyện câu sai)

```bash
python auto_press.py
```

Script đợi 10 giây rồi bắt đầu. Chuyển sang cửa sổ trang ôn luyện trước khi hết 10 giây.

### script.py — Popup + reload Brave

```bash
python script.py
```

Nhận diện popup (`imgs/popup.png`), click giữa màn hình, tự reload Brave lúc 00:05.
