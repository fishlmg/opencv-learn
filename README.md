# OpenCV 学习练习

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8.svg)](https://opencv.org/)

OpenCV 计算机视觉基础与实战练习集合，每个脚本对应一个独立的视觉技术点，可直接运行、便于对照学习。

## 🗂 练习内容

| 文件 | 技术点 |
| --- | --- |
| `opencv-test/blur.py` | 图像模糊（均值/高斯/中值/双边滤波） |
| `opencv-test/contours.py` | 轮廓检测与绘制 |
| `opencv-test/corner.py` | 角点检测（Harris / 亚像素角点） |
| `opencv-test/hsv.py` | HSV 颜色空间与颜色分割 |
| `opencv-test/qrcode.py` | 二维码检测与识别 |
| `opencv-test/template.py` | 模板匹配 |
| `basics.py` | 阈值、轮廓近似与面积（读取仓库根目录的 `1.png`） |

## 🚀 快速开始

```bash
pip install -r requirements.txt

# 在仓库根目录按需运行单个练习
python opencv-test/contours.py
python opencv-test/hsv.py
python opencv-test/qrcode.py
python basics.py
```

`basics.py` 需要自行准备根目录下的 `1.png`。`opencv-test/` 里的脚本读取 `./img/` 下的图片（相对当前工作目录）。

## 📦 依赖

OpenCV、NumPy——详见 [requirements.txt](requirements.txt)。

`torch` 只给下方「非本仓主题」的显存脚本使用，跑 OpenCV 练习可以不装。

## 🧰 非本仓主题

`utils/free.py` 与 `utils/FreeGPUMen.py` 是 PyTorch / NVIDIA 显存清理片段，与 OpenCV 练习无关，仅归档在 [utils/](utils/README.md)。用途和风险见该目录说明。

## 📝 说明

测试图片素材不包含在仓库中（`.gitignore` 已排除 `*.jpg` / `*.jpeg` / `*.png` 与 `opencv-test/img/`），可自行准备图片放入对应路径后运行。

## 📄 许可证

[MIT License](LICENSE)
