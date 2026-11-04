# 非本仓主题：PyTorch 显存缓存释放片段，与 OpenCV 练习无关。
# unused_variable 需换成实际不再使用的张量名，否则会 NameError。
import torch
del unused_variable
torch.cuda.empty_cache()
