# Industrial Defect Detection

## Method Fit

- Clear labeled defects: detection.
- Precise shape: segmentation.
- Rare or unknown defects: anomaly detection.
- Stable product pose: registration plus ROI inspection.
- Variable pose: detection or feature alignment first.
- Tiny defects: high-resolution crop or tiling.
- Strict real time: lightweight model plus target-hardware optimization.

## Pipeline

1. Camera, lens, lighting, exposure, trigger
2. Geometric normalization
3. Preprocessing
4. Inspection model
5. Decision rule
6. Evaluation
7. Deployment and drift monitoring

## Split

Split by product, lot, date, machine, or acquisition condition. Keep near-duplicate frames of same part in one split. Use separate threshold-calibration data.

## Metrics

- Defect-level recall and precision
- Part-level false reject and false accept
- False positives per part
- Recall by defect size and severity
- FPR at target TPR
- Threshold stability across conditions
- Operator review rate
- Cost-weighted FP/FN

Always inspect lighting, reflection, angle, motion blur, contamination, material drift, sample aging, and annotation consistency.
