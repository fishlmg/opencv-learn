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
| `test.py` | 基础操作练习 |
| `free.py` / `FreeGPUMen.py` | PyTorch GPU 显存释放工具 |

## 🚀 快速开始

```bash
pip install -r requirements.txt

# 按需运行单个练习
python opencv-test/contours.py
python opencv-test/hsv.py
python opencv-test/qrcode.py
```

## 💡 显存清理小工具

训练后 GPU 显存未释放时，可运行：

```python
# free.py 核心逻辑
import torch
torch.cuda.empty_cache()
```

## 📦 依赖

OpenCV、NumPy、PyTorch（显存工具）—— 详见 [requirements.txt](requirements.txt)

## 📝 说明

测试图片素材不包含在仓库中（`.gitignore` 已排除），可自行准备图片放入对应目录运行。

## 📄 许可证

[MIT License](LICENSE)
