# Deployment

## Separate

- Model-only latency
- End-to-end latency
- Throughput
- Memory
- I/O
- Accuracy drift
- Compatibility

## Required Benchmark

```text
Hardware:
Software versions:
Power mode:
Precision:
Input shape:
Batch size:
Warm-up iterations:
Measured iterations:
Model latency p50/p95:
End-to-end latency p50/p95:
Throughput:
Peak memory:
Temperature and duration:
Accuracy delta:
```

## Optimize in Order

1. Confirm preprocessing and output parity.
2. Profile camera, decode, preprocess, transfer, model, and post-process separately.
3. Remove copies and unnecessary synchronization.
4. Validate FP16.
5. Use INT8 only with representative calibration and accuracy checks.
6. Tune shapes, batching, and asynchronous stages.
7. Stress-test thermal and long-duration stability.

For ONNX and TensorRT, verify exporter, opset, operators, shape profiles, parser logs, and target-runtime compatibility.
