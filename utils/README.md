# 非本仓主题

这里的脚本与 OpenCV 学习无关，是误放进来的 PyTorch / NVIDIA 显存清理片段，只作归档，不是本仓库的练习内容。

| 文件 | 作用 |
| --- | --- |
| `free.py` | 调用 `torch.cuda.empty_cache()`，尝试释放 PyTorch 缓存的显存。其中的 `unused_variable` 要换成实际不再使用的张量名，否则会 `NameError`。 |
| `FreeGPUMen.py` | 用 `fuser` 查找占用 `/dev/nvidia*` 的进程并 `kill -9`。会强制结束这些进程，请谨慎运行。 |

OpenCV 练习本身不需要 PyTorch。只有运行上述脚本时才安装 `torch`（见仓库根目录的 `requirements.txt`）。
