import os
import sys
import pyautogui
import time

NEXT_IMAGE = "imgs/next.png"   # nút "Tiếp"
END_IMAGE = "imgs/end.png"     # nút "Kết thúc luyện thi" (nền xanh)
END_HOVER_IMAGE = "imgs/end_hover.png"  # nút khi hover (nền trắng)
WRONG_IMAGE = "imgs/wrong.png" # nút "luyện câu sai"

# Trên Mac Retina, locateOnScreen trả về tọa độ pixel (2x), click() dùng logical points → chia cho scale
RETINA_SCALE = 2 if sys.platform == "darwin" else 1


def _click_at(x, y):
    """Click tại (x, y); trên macOS tự chia cho RETINA_SCALE để khớp tọa độ."""
    if RETINA_SCALE != 1:
        x, y = x / RETINA_SCALE, y / RETINA_SCALE
    pyautogui.click(x, y)


def click_image(image_path, confidence=0.7, grayscale=True, region=None):
    """Tìm ảnh trên màn hình và click vào giữa. Trả về True nếu tìm thấy.
    region: (left, top, width, height) để tìm trong vùng nhất định, hoặc None = toàn màn hình."""
    try:
        kwargs = dict(confidence=confidence, grayscale=grayscale)
        if region is not None:
            kwargs["region"] = region
        location = pyautogui.locateOnScreen(image_path, **kwargs)
        if location:
            x, y = pyautogui.center(location)
            _click_at(x, y)
            return True
    except pyautogui.ImageNotFoundException:
        pass
    return False


def has_next_button():
    """Kiểm tra còn nút 'Tiếp' trên màn hình không."""
    try:
        location = pyautogui.locateOnScreen(
            NEXT_IMAGE,
            confidence=0.7,
            grayscale=True
        )
        return location is not None
    except pyautogui.ImageNotFoundException:
        return False


def scroll_to_bottom():
    """Cuộn xuống dưới cùng (nhiều lần để chắc chắn)."""
    for _ in range(12):
        pyautogui.scroll(-5)  # âm = cuộn xuống (trên hầu hết hệ điều hành)
        time.sleep(0.02)
    print("  Đã cuộn xuống dưới cùng")


def scroll_up():
    """Cuộn lên để tìm nút Kết thúc luyện thi."""
    for _ in range(12):
        pyautogui.scroll(5)  # dương = cuộn lên
        time.sleep(0.02)
    print("  Đã cuộn lên")


def has_end_button():
    """Kiểm tra có nút Kết thúc luyện thi trên màn hình không (cùng cách tìm như nút Tiếp)."""
    for img in [END_IMAGE, END_HOVER_IMAGE]:
        if not os.path.isfile(img):
            continue
        try:
            location = pyautogui.locateOnScreen(img, confidence=0.7, grayscale=True)
            if location:
                return True
        except pyautogui.ImageNotFoundException:
            pass
    return False


def find_end_and_press_enter():
    """Cuộn lên, nếu thấy nút Kết thúc luyện thi thì ấn Enter (không click chuột)."""
    scroll_up()
    time.sleep(0.4)
    if has_end_button():
        pyautogui.press("enter")
        return True
    return False


def move_cursor_to_corner():
    """Di chuột ra góc màn hình (trên-trái) để không đè lên nút, tránh ảnh hưởng detect."""
    pyautogui.moveTo(20, 20, duration=0.2)
    time.sleep(0.15)


def _click_wrong_with_log():
    """Tìm nút Luyện câu sai, log vị trí và vị trí click, rồi click."""
    print("  [Luyện câu sai] Đang tìm nút...")
    try:
        location = pyautogui.locateOnScreen(
            WRONG_IMAGE,
            confidence=0.7,
            grayscale=True
        )
        if location:
            left, top, width, height = location
            x, y = pyautogui.center(location)
            print(f"  [Luyện câu sai] Tìm thấy nút.")
            print(f"  [Luyện câu sai] Vị trí (left, top, width, height): ({left}, {top}, {width}, {height})")
            print(f"  [Luyện câu sai] Vị trí click (từ locate): ({x}, {y})")
            _click_at(x, y)
            click_x = x / RETINA_SCALE if RETINA_SCALE != 1 else x
            click_y = y / RETINA_SCALE if RETINA_SCALE != 1 else y
            print(f"  [Luyện câu sai] Đã click tại (sau scale): ({click_x}, {click_y})")
            time.sleep(0.7)
        else:
            print("  [Luyện câu sai] Không tìm thấy nút (locate trả về None).")
    except pyautogui.ImageNotFoundException:
        print("  [Luyện câu sai] Không tìm thấy nút (ImageNotFoundException).")


def run_for_key(key):
    """Chạy chu trình cho một phím (1, 2, 3, 4): nhấn phím -> cuộn xuống -> Tiếp (mũi tên phải) -> Kết thúc -> Luyện câu sai."""
    print(f"Đang xử lý phím {key}...")
    pyautogui.press(key)
    time.sleep(0.8)  # đợi giao diện load
    scroll_to_bottom()
    time.sleep(0.2)

    # Lặp: nếu còn nút "Tiếp" thì nhấn mũi tên phải rồi chọn đáp án bằng phím tương ứng
    while has_next_button():
        pyautogui.press("right")
        print("  Nhấn mũi tên phải (Tiếp)")
        time.sleep(0.25)
        pyautogui.press(key)  # chọn đáp án (phím 1, 2, 3 hoặc 4)
        print(f"  Chọn đáp án phím {key}")
        time.sleep(0.2)
        scroll_to_bottom()  # luôn cuộn xuống sau khi chọn đáp án
        time.sleep(0.5)

    # Hết "Tiếp" -> cuộn lên, thấy nút Kết thúc thì ấn Enter
    if find_end_and_press_enter():
        print("  Đã ấn Enter (Kết thúc luyện thi)")
        time.sleep(0.7)
    else:
        print("  Không tìm thấy nút Kết thúc luyện thi")

    # Di chuột ra góc để không đè lên nút Luyện câu sai (dễ detect hơn)
    move_cursor_to_corner()
    # Bấm "Luyện câu sai"
    _click_wrong_with_log()


def main():
    print("Bắt đầu sau 10 giây... (chuyển sang cửa sổ cần thao tác)")
    time.sleep(10)

    for key in ["1", "2", "3", "4"]:
        run_for_key(key)
        time.sleep(0.5)

    print("Đã xong.")


if __name__ == "__main__":
    main()
