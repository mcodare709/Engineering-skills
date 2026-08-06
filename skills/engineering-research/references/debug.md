# Debug Reference

## Protocol

錯誤原因 → 對應程式行為 → minimal fix → verification command。

不要先逐行解釋正常流程；先定位最可能的 failure point。保留使用者提供的原始 error message、function name、path 與 line number。

## Isolation Order

1. Reproduce with the smallest input.
2. Print shape、dtype、device、range and path at system boundaries.
3. Disable multiprocessing、augmentation、mixed precision or optional acceleration.
4. Verify one component at a time.
5. Re-enable optimizations after correctness is confirmed.

## PyTorch / Python

| Symptom | Check first |
|---|---|
| Shape mismatch | Print `.shape` before and after each transform/module boundary |
| dtype mismatch | Input/loss target dtype and implicit casts |
| Device mismatch | Model, input, target and cached tensors on same device |
| NaN loss | Input range, bad label, divide by zero, AMP overflow, gradient explosion |
| CUDA OOM | Batch size, activation size, retained graph, unused tensors |
| Wrong metric | `train()` vs `eval()`, threshold, reduction and aggregation |
| Dataloader hang | Set `num_workers=0`, inspect dataset exception and path |
| Checkpoint load failure | Key prefix, architecture config, strictness and version |

## OpenCV

| Symptom | Check first |
|---|---|
| `cv2.imread` returns `None` | Path, Unicode handling, file existence, permissions |
| Color is wrong | BGR/RGB conversion and normalized channel order |
| Size mismatch | HWC/CHW order, resize and padding recovery |
| `VideoCapture` fails | `.isOpened()`, backend, device index, codec and permissions |
| Geometry is wrong | Coordinate convention, crop offset, affine direction |

## CUDA / Jetson

| Symptom | Check first |
|---|---|
| CUDA unavailable | PyTorch build, JetPack/CUDA compatibility, container runtime |
| TensorRT build error | Unsupported operator, shape profile, precision and parser log |
| Thermal throttling | `tegrastats`, power mode, clocks and cooling |
| Version conflict | JetPack, CUDA, cuDNN, TensorRT, Python and framework matrix |

## Minimal Commands

```bash
python -c "import torch; print(torch.__version__, torch.version.cuda, torch.cuda.is_available())"
python -c "import cv2; print(cv2.__version__)"
nvidia-smi
tegrastats  # Jetson only
```
