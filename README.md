# SVG Filter Generator (Desktop App)

A cross-platform desktop application that converts any target color into an equivalent **CSS `filter`** value usable for SVG icons or images.

This project is a **Python + PyQt port** of the original web-based version by **Sosuke**.

---

## ✨ Features

* Convert HEX color → CSS `filter`
* Real-time preview (Target vs Result)
* Loss score & detailed accuracy info
* Cross-platform: **Linux / Windows / macOS**
* Portable build via **PyInstaller**

---

## 🖼 Preview

> <img width="438" height="443" alt="image" src="https://github.com/user-attachments/assets/ec74f77a-e228-411f-989a-4c89ebc53d73" />


---

## 🚀 Getting Started

### 1️⃣ Clone repository

```bash
git clone https://github.com/risky2k1/SVG-Filter.git
cd SVG-Filter
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate  # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run application

```bash
python main.py
```

---

## 📦 Build Standalone App

### Linux / macOS

```bash
pyinstaller build.spec
```

### Windows

```bash
pyinstaller build.spec
```

Executable will be available in:

```
dist/
```

---

## 🧠 How It Works

The app computes a combination of CSS filters (`invert`, `sepia`, `saturate`, `hue-rotate`, `brightness`, `contrast`) that approximates a target color when applied to a black SVG.

Accuracy is measured using:

* **Loss score**
* **Detailed RGB deviation (lossDetail)**

Lower loss = closer color match.

---

## 🔗 Original Algorithm & Reference

The core algorithm was **originally derived and explained by MultiplyByZer0** on Stack Overflow:

* 🧠 Original explanation & solution:
  [https://stackoverflow.com/questions/42966641](https://stackoverflow.com/questions/42966641)

* 👤 Author profile:
  [https://stackoverflow.com/users/2688027/multiplybyzer0](https://stackoverflow.com/users/2688027/multiplybyzer0)

The solution was later **adapted and demonstrated on the web by Sosuke**, who converted the algorithm into an interactive JavaScript tool:

* 🌐 CodePen demo:
  [https://codepen.io/sosuke/pen/Pjoqqp](https://codepen.io/sosuke/pen/Pjoqqp)

> As stated by Sosuke himself, the implementation was inspired by and credits the original Stack Overflow solution by **MultiplyByZer0**, with slight modifications to focus on HEX colors and practical usage.

This repository is a **desktop (PyQt) adaptation of the web demo**, and **does not claim authorship of the original algorithm**.

---

## 🛡 License

MIT License

Copyright (c) 2026 Pham Minh Tuan

---

## 📌 Notes

* `.venv/`, `dist/`, `build/` are ignored via `.gitignore`
* Python ≥ 3.9 recommended

---
