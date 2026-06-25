# Industrial Defect Detection Reference

## Method Selection

| Scenario | Preferred Approach |
|---|---|
| Defects have clear labels and bounding boxes | YOLO or object detection |
| Defects require precise shape | Instance segmentation |
| Defects are rare or hard to label | Anomaly detection (PatchCore, FastFlow) |
| Surface texture varies heavily | Feature-based + deep anomaly method |
| Real-time production line (>30 FPS) | Lightweight detector or TensorRT deployment |
| Very small defects (<10px) | High-res crop + dedicated small-object model |

## Pipeline Structure

When proposing a detection pipeline, always include all seven stages:

1. **Image acquisition** — camera spec, lighting setup, trigger mode
2. **Preprocessing** — denoise, normalize, crop, resize
3. **Detection method** — chosen model and rationale
4. **Decision rule** — threshold, ensemble, fallback logic
5. **Evaluation metrics** — precision, recall, F1, FPR at target TPR
6. **Failure cases** — where the method is expected to struggle
7. **Deployment concerns** — latency, operator review, alert workflow

## Production Constraints to Prioritize

- Lighting stability and reflection/glare control
- Camera angle consistency and lens distortion
- Motion blur at production speed
- Sample aging and surface contamination variation
- Annotation consistency across labelers
- Defect size distribution (micro vs. macro defects)
- False positive cost vs. false negative cost — clarify with user
- Threshold stability under distribution shift
- Operator review workflow integration

## Common Failure Root Causes

| Failure | Root Cause |
|---|---|
| High false positive rate | Lighting inconsistency or low threshold |
| High false negative rate | Threshold too high or missing training examples |
| Good lab, poor line performance | Distribution shift (lighting, speed, angle) |
| Model degraded over time | Sample aging not in training set |
| Inconsistent results same part | Camera trigger timing or vibration |
