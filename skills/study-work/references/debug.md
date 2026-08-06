# Debugging

## Protocol

Cause. Wrong behavior. Minimal fix. Verification.

## Isolation

1. Reproduce with smallest input.
2. Inspect shape, dtype, device, range, and path at boundaries.
3. Disable multiprocessing, augmentation, mixed precision, and optional acceleration.
4. Verify one component at a time.
5. Restore optimizations after correctness.

## First Checks

- Shape mismatch: print shapes around each transform and module.
- Dtype mismatch: inspect input and target dtype.
- Device mismatch: model, input, target, and cached tensors must match.
- NaN loss: inspect input range, labels, divisions, AMP, and gradient norm.
- CUDA OOM: inspect batch, activation size, retained graph, and buffers.
- Wrong metric: inspect `train()`, `eval()`, threshold, reduction, and aggregation.
- Dataloader hang: set `num_workers=0`.
- OpenCV read failure: verify path, existence, permissions, and Unicode handling.
- Wrong color: verify BGR/RGB order.
- Checkpoint failure: verify architecture, key prefix, strictness, and version.

Keep original error text exact.
