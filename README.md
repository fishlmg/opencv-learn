# OpenCV 学习练习

OpenCV 基础与实战练习集合，覆盖模糊、轮廓、角点、HSV 颜色空间、模板匹配、二维码识别等常用视觉技术。

## 文件结构

```
├── free.py / FreeGPUMen.py   # GPU 显存清理工具
├── test.py                   # 基础测试
└── opencv-test/
    ├── blur.py               # 图像模糊
    ├── contours.py           # 轮廓检测
    ├── corner.py             # 角点检测
    ├── hsv.py                # HSV 颜色空间
    ├── qrcode.py             # 二维码识别
    └── template.py           # 模板匹配
```

## 快速开始

```bash
pip install -r requirements.txt
python opencv-test/contours.py
```

测试图片素材不包含在仓库中（`.gitignore` 已排除）。
