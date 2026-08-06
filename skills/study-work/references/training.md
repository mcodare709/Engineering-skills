# Training

## Diagnose in Order

1. Data and labels
2. Split and leakage
3. Metric implementation
4. Loss behavior
5. Optimizer and learning rate
6. Augmentation
7. Model capacity
8. Post-processing

## Minimum Evidence

- Train and validation curves
- Dataset size and class distribution
- Split method and group boundaries
- Input preprocessing and resolution
- Batch size, optimizer, scheduler, learning rate
- Augmentation
- Checkpoint rule
- Seed and software versions

## Fast Tests

- Overfit 8 to 32 samples without augmentation.
- Compare raw and preprocessed batch.
- Confirm every trainable parameter gets gradient.
- Evaluate one checkpoint with fixed seed and threshold.
- Report metrics by class, size, product, lot, and condition.

## Interpret

- Train and validation both poor: underfitting, bad labels, bad preprocessing.
- Train improves, validation degrades: overfitting or split mismatch.
- Low loss, poor metric: objective or post-processing mismatch.
- Good validation, poor production: domain shift.
- NaN or Inf: bad input, division error, overflow, or exploding gradient.
