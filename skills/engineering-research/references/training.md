# Model Training Reference

## Diagnosis Order

When a training problem is reported, diagnose in this order:

1. **Data and labels** — quality, consistency, annotation errors
2. **Split** — leakage, distribution mismatch between train/val/test
3. **Loss and metrics** — are they moving in the expected direction?
4. **Learning rate / optimizer** — too high, too low, wrong scheduler
5. **Augmentation** — too aggressive, mismatched to test distribution
6. **Model capacity** — underfitting vs. overfitting
7. **Post-processing** — threshold, NMS, decode step

## Key Factors to Consider

- Dataset quality and size
- Label consistency and annotation error rate
- Class imbalance and sampling strategy
- Augmentation strategy vs. test domain
- Image resolution and aspect ratio handling
- Batch size and gradient accumulation
- Learning rate schedule (warmup, decay, cosine)
- Optimizer choice (SGD + momentum, AdamW, Adam)
- Loss function design (focal, dice, BCE, CE, MSE, MAE, Perceptual)
- Validation metric stability across epochs
- Checkpoint selection strategy
- Reproducibility (seed, deterministic ops)
- Hardware constraints (VRAM, multi-GPU sync)

## Common Failure Patterns

| Symptom | Likely Cause |
|---|---|
| Loss drops then plateaus | LR too low or data exhausted |
| Loss oscillates | LR too high |
| Val loss diverges from train loss | Overfitting or split leakage |
| mAP low despite low loss | Threshold or NMS misconfiguration |
| NaN loss | LR too high, exploding gradient, bad label |
| Good val, poor real-world | Distribution mismatch |
