# Inference and Deployment Reference

## Problem Classification

Before answering, identify which category the issue falls into:

| Category | Signals |
|---|---|
| Accuracy issue | Wrong predictions, low mAP, false positives/negatives |
| Speed issue | Low FPS, high latency, timeout |
| Memory issue | OOM, CUDA out of memory, swap usage |
| IO bottleneck | CPU-bound dataloader, camera stall |
| Preprocessing mismatch | Wrong resize, wrong normalization, BGR/RGB swap |
| Train/inference distribution mismatch | Good val, bad real-world |

## Factors to Consider

- FPS, latency, throughput requirements
- Camera input pipeline (GStreamer, V4L2, USB vs. CSI)
- Preprocessing cost (resize, normalize, pad)
- Post-processing cost (NMS, decode, draw)
- Confidence threshold and NMS IoU setting
- Input resolution vs. training resolution
- GPU/CPU memory budget
- Jetson power mode (maxn vs. 10W)
- TensorRT engine build settings (FP16, INT8, dynamic shape)
- ONNX export settings (opset, dynamic axes)
- Production-line stability (latency spikes, thermal throttling)

## Jetson-Specific Checklist

```bash
# Check power mode
sudo nvpmodel -q
sudo jetson_clocks --show

# Check GPU memory
tegrastats

# Check TensorRT version
python -c "import tensorrt; print(tensorrt.__version__)"

# Verify PyTorch + CUDA
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

## TensorRT Conversion Checklist

1. Export to ONNX with correct opset (typically 11 or 17)
2. Verify ONNX with `onnxruntime` before TensorRT conversion
3. Build engine with correct precision (FP16 recommended for Jetson)
4. Profile with `trtexec` to verify latency
5. Validate output matches PyTorch baseline within tolerance
