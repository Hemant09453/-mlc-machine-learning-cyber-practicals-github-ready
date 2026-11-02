# Practical 09 - Model Evaluation (Confusion Matrix, ROC, AUC)

## Aim

Evaluate two classification models on a cyber-security dataset using a
confusion matrix, ROC curves, and the AUC score.

## Dataset

`cyber_classification_eval_dataset.csv` contains 30 network-traffic records:

| Feature | Meaning |
|---|---|
| `duration_ms` | Connection duration |
| `packet_count` | Number of packets |
| `failed_login_attempts` | Failed login count |
| `src_bytes` / `dst_bytes` | Bytes sent/received |
| `urgent_packets` | Urgent TCP packets |
| `protocol_tcp` / `protocol_udp` | Protocol flags |
| `attack` | `0` = normal, `1` = attack |

## Files

| File | Purpose |
|---|---|
| `model-evaluation-roc-auc.ipynb` | Main notebook |
| `evaluate_classification_models_cyber.py` | Standalone script |
| `cyber_classification_eval_dataset.csv` | Input dataset |
| `report.pdf` | Submitted lab report with results |

## What the Notebook Does

1. Loads the dataset and separates `attack` from the features.
2. Splits 70/30 with stratification.
3. Defines two models:
   - Logistic Regression with `StandardScaler`
   - Random Forest (100 trees)
4. Trains each model and predicts labels plus attack probabilities.
5. Prints the confusion matrix and classification report.
6. Saves a confusion-matrix image for each model.
7. Plots ROC curves and prints the AUC score.

## How to Run

Notebook:

```bash
pip install -r requirements.txt
jupyter lab
```

Open `practical-09-model-evaluation/model-evaluation-roc-auc.ipynb` and run all
cells.

Script:

```bash
python evaluate_classification_models_cyber.py
```

## Expected Output

- Confusion matrices for both models
- Precision, recall, F1-score for normal and attack classes
- AUC score per model
- ROC curve plot comparing both models
- Saved PNG confusion-matrix images

## Notes

- **Accuracy alone is misleading** for imbalanced security data. Pay attention
  to recall for the attack class and to false negatives.
- AUC measures ranking quality across all thresholds; the confusion matrix
  describes one chosen threshold.
- Notebook outputs were cleared before publishing. The report contains the
  recorded results.
