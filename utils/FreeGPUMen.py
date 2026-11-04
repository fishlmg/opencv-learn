# 非本仓主题：强制结束占用 NVIDIA 设备的进程，与 OpenCV 练习无关。请谨慎运行。
import os
result = os.popen("fuser -v /dev/nvidia*").read()
results = result.split()
for pid in results:
    os.system(f"kill -9 {int(pid)}")