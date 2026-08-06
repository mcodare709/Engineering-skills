# Model Training Reference

## Required Evidence

優先從使用者已提供的 log、curve、config、dataset statistics 與 code 判斷。若資料不足，明確列出假設，但仍先提供最可能的診斷。

至少確認：

- Train/validation loss and metric curves
- Dataset size、class distribution、label quality
- Train/validation/test split method
- Input resolution and preprocessing
- Batch size、learning rate、optimizer、scheduler
- Augmentation configuration
- Checkpoint selection criterion
- Random seed and environment version

## Diagnosis Order

1. **Data and labels** — missing samples、annotation error、class imbalance、duplicate data
2. **Split** — leakage、same product/lot across splits、distribution mismatch
3. **Metric implementation** — train/eval mode、threshold、aggregation unit
4. **Loss behavior** — scale、weighting、NaN/Inf、gradient magnitude
5. **Optimization** — learning rate、optimizer、scheduler、warmup、batch size
6. **Augmentation** — unrealistic transform、train/test mismatch
7. **Model capacity** — underfitting、overfitting、frozen layer、bad initialization
8. **Post-processing** — confidence threshold、NMS、decode、resize recovery

## Failure Patterns

| Symptom | Likely cause | Verify |
|---|---|---|
| Train and val both poor | Underfitting, bad labels, preprocessing mismatch | Overfit a tiny subset |
| Train improves, val degrades | Overfitting or split mismatch | Inspect leakage and per-group metrics |
| Loss oscillates | LR too high, unstable batch statistics | Plot LR and gradient norm |
| Loss plateaus early | LR too low, frozen parameters, weak signal | Check parameter updates |
| Low loss but poor metric | Loss/metric mismatch or post-processing error | Evaluate raw outputs |
| Good val, poor production | Domain shift | Build line-condition validation set |
| NaN/Inf | Bad input, divide by zero, overflow, exploding gradient | Check tensors and gradient norm |

## Minimal Verification Experiments

1. Overfit 8–32 samples without augmentation.
2. Compare one batch before and after preprocessing.
3. Confirm every trainable parameter receives gradient.
4. Evaluate the same checkpoint with fixed seed and threshold.
5. Report metrics by class, defect size, product, lot and acquisition condition.

## Reproducibility Record

Record at minimum:

```text
Git commit:
Dataset version:
Split manifest:
Random seed:
Framework/CUDA version:
Model config:
Optimizer/scheduler:
Augmentation:
Best-checkpoint rule:
Evaluation command:
```
