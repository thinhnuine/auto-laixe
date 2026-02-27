
---

````markdown
# Brave Auto Reload & Popup Click Bot

Automation script for Brave Browser that:

- Detects a popup using image recognition
- Clicks the center of the screen when popup appears
- Automatically reloads the page at 00:05 daily
- Runs continuously (24/7)

Built with Python + PyAutoGUI for macOS.

---

## 🚀 Features

- 🔍 Detect popup via image (`popup.png`)
- 🖱 Click center of screen (instead of popup)
- 🔄 Auto reload at exactly 00:05
- 🔁 Continuous loop monitoring
- 🍎 Optimized for macOS using AppleScript
- 🛡 Safe error handling (won’t crash if popup not found)

---

## 🛠 Requirements

- macOS
- Python 3.9+
- Brave Browser installed
- Single monitor recommended

---

## 📦 Installation

### 1️⃣ Clone repository

```bash
git clone <your-repo-url>
cd auto-click
````

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install pyautogui opencv-python
```

---

## 🔐 macOS Permission Setup (IMPORTANT)

Go to:

System Settings
→ Privacy & Security
→ Accessibility

Enable access for:

* Terminal
  or
* VSCode
  or
* PyCharm

Without this permission, the script cannot control mouse and keyboard.

You may also need to enable:

Privacy & Security → Screen Recording

---

## 📂 Project Structure

```
auto-click/
│
├── script.py
├── popup.png
└── README.md
```

Make sure `popup.png` matches exactly the popup shown on your screen.

---

## ▶️ How to Run

Activate virtual environment (if using):

```bash
source venv/bin/activate
```

Run script:

```bash
python script.py
```

After running:

* Script will monitor screen every second
* If popup appears → click center of screen
* At 00:05 → reload Brave tab
* Loop continues forever

---

## 🧠 How It Works

1. `pyautogui.locateOnScreen()` scans for `popup.png`
2. If detected:

   * Focus Brave using AppleScript
   * Click screen center
3. Every second:

   * Check system time
   * If time == 00:05 → trigger reload (CMD + R)

---

## ⚙️ Configuration

Change popup image file:

```python
POPUP_IMAGE = "popup.png"
```

Adjust image detection confidence:

```python
confidence=0.7
```

Increase if false positives occur.
Decrease if detection is too strict.

---

## 🖥 Running 24/7 (Optional)

You can:

* Keep terminal open
* Or use `nohup`:

```bash
nohup python script.py &
```

* Or use `tmux`
* Or create macOS Launch Agent

---

## 🛠 Troubleshooting

### ❌ Popup not detected

* Make sure popup image resolution matches screen
* Try lowering confidence (e.g., 0.6)
* Ensure Brave window is visible

### ❌ Script not clicking

Check macOS permissions:

* Accessibility
* Screen Recording

Restart terminal after enabling permissions.

### ❌ Reload not working

Ensure Brave is the active browser.
Script uses AppleScript to trigger CMD+R.

---

## ⚠️ Limitations

* Designed for macOS only
* Not optimized for multi-monitor setup
* Requires Brave window to be visible
* Uses screen-based automation (not DOM-based)

```
# auto-laixe
