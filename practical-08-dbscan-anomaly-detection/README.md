# Practical 08 - DBSCAN Anomaly Detection

## Aim

Use density-based clustering (DBSCAN) to detect anomalies in network-traffic
data and visualise the results with PCA.

## Dataset

`network_traffic_anomaly.csv` contains 26 records with:

| Feature | Meaning |
|---|---|
| `packet_size` | Packet size |
| `connection_duration` | Connection duration |
| `src_bytes` / `dst_bytes` | Bytes sent/received |
| `packet_rate` | Packet rate |
| `error_rate` | Error rate |
| `label` | `normal` or `anomaly` (used only for evaluation) |

`dbscan_anomaly_output.csv` is the generated output with cluster labels and
PCA coordinates.

## Files

| File | Purpose |
|---|---|
| `dbscan-anomaly-detection.ipynb` | Main notebook |
| `dbscan_anomaly_detection.py` | Standalone script |
| `network_traffic_anomaly.csv` | Input dataset |
| `dbscan_anomaly_output.csv` | Generated output |
| `report.pdf` | Final submitted report |
| `report-draft.pdf`, `report.docx` | Draft/report sources |
| `screenshots/` | Clustering evidence |

## What the Notebook Does

1. Loads the traffic dataset.
2. Selects six numeric features (labels are excluded from training).
3. Standardises features with `StandardScaler`.
4. Runs `DBSCAN(eps=1.0, min_samples=3)`.
5. Treats cluster `-1` as an anomaly and labels all other clusters as normal.
6. Compares predictions with the ground-truth label using a confusion matrix
   and classification report.
7. Reduces the feature space to two dimensions with PCA and plots normal vs
   anomaly points.
8. Saves the result to `dbscan_anomaly_output.csv`.

## How to Run

Notebook:

```bash
pip install -r requirements.txt
jupyter lab
```

Open `practical-08-dbscan-anomaly-detection/dbscan-anomaly-detection.ipynb`
and run all cells.

Script:

```bash
python dbscan_anomaly_detection.py
```

## Expected Output

- Cluster assignments for every record
- Anomaly/normal prediction column
- Confusion matrix and classification report
- PCA scatter plot with anomalies marked as `x`
- Regenerated `dbscan_anomaly_output.csv`

## Notes

- DBSCAN is unsupervised: the `label` column is used only for evaluation, not
  for fitting.
- `eps` and `min_samples` strongly affect the number of anomalies. Try a small
  parameter sweep if you want to discuss sensitivity in the report.
- The dataset is small, so the confusion matrix is illustrative rather than a
  production benchmark.
