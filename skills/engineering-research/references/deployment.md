# Inference and Deployment Reference

## Classify the Bottleneck

| Category | Signals |
|---|---|
| Accuracy | Wrong prediction, FP/FN, threshold instability |
| Model latency | Slow forward pass or TensorRT engine |
| End-to-end latency | Camera, preprocessing, transfer, post-processing or display delay |
| Throughput | Pipeline cannot sustain required parts/second |
| Memory | OOM, swap, fragmentation, excessive buffers |
| I/O | Camera stall, disk/network delay, CPU-bound decode |
| Compatibility | ONNX export, unsupported operator, runtime version mismatch |

## Required Production Constraints

- Target hardware and power mode
- Input source, resolution, format and frame rate
- Maximum acceptable p95 latency
- Required throughput/FPS
- Precision target: FP32、FP16、INT8
- GPU/CPU memory budget
- Camera trigger and buffering behavior
- Thermal and long-duration stability
- Accuracy tolerance compared with training framework

## Benchmark Protocol

不要只回報單次 FPS。至少記錄：

```text
Hardware:
Software versions:
Power mode / clocks:
Precision:
Input shape:
Batch size:
Warm-up iterations:
Measured iterations:
Model-only latency p50/p95:
End-to-end latency p50/p95:
Throughput/FPS:
Peak CPU/GPU memory:
Temperature and run duration:
Accuracy delta from baseline:
```

## Optimization Order

1. Confirm preprocessing and output parity with training.
2. Profile camera, decode, preprocess, transfer, model and post-process separately.
3. Remove unnecessary copies and synchronize only when measuring.
4. Use FP16 when supported and validate numerical error.
5. Use INT8 only with representative calibration data and accuracy validation.
6. Tune input shape, batching and asynchronous pipeline.
7. Validate sustained performance under production temperature and load.

## ONNX / TensorRT Checklist

1. Select ONNX opset based on exporter, operator support, ONNX Runtime and target TensorRT compatibility.
2. Run ONNX checker and ONNX Runtime inference before TensorRT conversion.
3. Define static or dynamic shape profiles that match real inputs.
4. Inspect unsupported operators and plugin requirements.
5. Compare outputs against the original framework using fixed inputs and tolerance.
6. Benchmark the final engine on target hardware, not desktop estimates.

## Jetson Commands

```bash
sudo nvpmodel -q
sudo jetson_clocks --show
tegrastats
python -c "import tensorrt; print(tensorrt.__version__)"
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```
