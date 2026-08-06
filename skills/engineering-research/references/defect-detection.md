# Industrial Defect Detection Reference

## Method Selection

| Scenario | Preferred approach |
|---|---|
| Clear defect classes and bounding boxes | Object detection |
| Precise defect shape is required | Semantic/instance segmentation |
| Defects are rare or difficult to enumerate | Anomaly detection |
| Product position is stable | Registration + ROI-specific inspection |
| Product position varies | Detection/feature alignment before inspection |
| Very small defects | High-resolution crop, tiling or dedicated small-object pipeline |
| Strict real-time requirement | Lightweight model plus target-hardware optimization |

## Pipeline Structure

1. **Image acquisition** — camera, lens, lighting, trigger, exposure
2. **Geometric normalization** — registration, crop, distortion correction
3. **Preprocessing** — color conversion, normalization, reflection control
4. **Inspection model** — method and rationale
5. **Decision rule** — threshold, aggregation, fallback and review
6. **Evaluation** — defect-level and part-level metrics
7. **Deployment** — latency, traceability, operator workflow and drift monitoring

## Dataset and Split Rules

- Split by product ID, batch/lot, acquisition date or production condition where relevant.
- Prevent near-duplicate frames of the same part from crossing splits.
- Keep a dedicated threshold-calibration set separate from final test data.
- Record lighting, camera, machine, material and sample-aging metadata.
- Audit annotation consistency across labelers and defect severity levels.

## Metrics

Do not report only image-level accuracy. Select metrics matching production cost:

- Defect-level recall and precision
- Part-level false reject rate and false accept rate
- False positives per image/part
- Recall by defect size and severity
- FPR at target TPR
- Threshold stability across lots and lighting conditions
- Operator review rate
- Cost-weighted FP/FN score when business cost is available

## Production Failure Causes

| Failure | Likely cause |
|---|---|
| High false positive | Lighting/reflection drift, contamination, threshold too low |
| High false negative | Missing defect modes, resolution too low, threshold too high |
| Good lab, poor line | Distribution shift in speed, angle, lighting or material |
| Performance degrades over time | Sample aging, lens contamination, process drift |
| Same part gives inconsistent result | Trigger timing, vibration, auto exposure or registration instability |

## Validation Stress Tests

- Multiple shifts and production days
- Clean and contaminated lens conditions
- Expected exposure and lighting drift
- Product aging and material batches
- Maximum line speed and motion blur
- Borderline defects near acceptance threshold
