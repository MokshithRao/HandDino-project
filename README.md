# 🦖 HandDino – Play Chrome Dino Game with Hand Gestures

HandDino is a fun and interactive computer vision project that allows you to control the Chrome Dinosaur Game using real-time **hand gestures** via your webcam. Built using **OpenCV**, **NumPy**, and **pyautogui**, it detects specific hand positions and triggers a jump action.

---

## 🎮 How It Works

- Launches your webcam
- Detects your hand movement using MediaPipe or OpenCV
- Triggers a `space` key press when a specific gesture (e.g., hand raised, thumb and pinky detected) is recognized
- You can play the Chrome Dino game hands-free!

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt

Execution
Run the program and switch over to chrome and open chrome://dino Keep your hand within the rectangle as you start. Move your hand to make the dino jump.
