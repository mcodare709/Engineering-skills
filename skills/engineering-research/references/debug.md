# Debug Reference

## Protocol

Cause → why → minimal fix → corrected code (if multi-location)

State the error source first. Do not describe what the code does before explaining what is wrong.

## PyTorch / Python

| Symptom | Check first |
|---|---|
| Shape error | Print `.shape` before and after every transform |
| dtype mismatch | `target.long()`, `input.float()` |
| Device mismatch | `.to(device)` on both model and tensor |
| NaN loss | LR too high, bad label, divide by zero in loss |
| CUDA OOM | Batch size, gradient accumulation, `del` unused tensors |
| Wrong metric | Train mode vs eval mode, `torch.no_grad()` missing |
| Dataloader hang | `num_workers=0` to isolate, then increase |

## OpenCV

| Symptom | Check first |
|---|---|
| `None` returned | Path wrong, file missing, permission issue |
| Color looks wrong | BGR vs RGB — add `cv2.cvtColor` or `[:, :, ::-1]` |
| Size mismatch | Check `img.shape` — HWC not CHW |
| VideoCapture fails | Check `.isOpened()`, try different backend |

## CUDA / Jetson

| Symptom | Check first |
|---|---|
| CUDA not available | `torch.cuda.is_available()`, check PyTorch build |
| TensorRT error | ONNX opset mismatch, dynamic shape not declared |
| Thermal throttle | `sudo jetson_clocks`, check `tegrastats` |
| Version conflict | `pip show torch`, `nvcc --version`, JetPack version |

## Minimal Verification Commands

```bash
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
python -c "import cv2; print(cv2.__version__)"
nvidia-smi
tegrastats  # Jetson only
```
