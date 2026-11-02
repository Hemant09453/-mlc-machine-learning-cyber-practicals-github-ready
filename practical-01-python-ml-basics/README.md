# Practical 01 - Python and Machine Learning Basics

## Aim

Set up a Python machine-learning environment and use NumPy, Pandas,
Matplotlib, and scikit-learn to load, explore, visualise, and classify a
small cyber-security dataset.

## Dataset

`basic_cyber_dataset.csv` contains 5 teaching records with 11 columns:

| Column | Meaning |
|---|---|
| `connection_id` | Record identifier |
| `duration_ms` | Connection duration in milliseconds |
| `src_bytes` / `dst_bytes` | Bytes sent and received |
| `failed_logins` | Failed login attempts |
| `packet_count` | Number of packets |
| `error_count` | Protocol/connection errors |
| `suspicious_score` | Hand-crafted risk score |
| `is_encrypted` | Encrypted-traffic flag |
| `label` | Normal or attack traffic |

## Files

| File | Purpose |
|---|---|
| `python-ml-basics.ipynb` | Main notebook |
| `basic_cyber_dataset.csv` | Input dataset |
| `report.pdf` | Submitted lab report with observations and outputs |

## What the Notebook Does

1. Imports the standard data stack (`numpy`, `pandas`, `matplotlib`, `sklearn`).
2. Loads the CSV and prints the first rows, shape, columns, data types, summary statistics, missing values, and class distribution.
3. Draws a bar chart of normal vs attack traffic.
4. Uses NumPy to calculate mean, minimum, and maximum connection duration.
5. Selects features, splits the data 70/30, and trains a `DecisionTreeClassifier`.
6. Compares predicted and actual labels and prints the accuracy score.

## How to Run

From the repository root:

```bash
python -m venv .venv
# Windows
.venv\Scripts\Activate.ps1
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
jupyter lab
```

Open `practical-01-python-ml-basics/python-ml-basics.ipynb` and run all cells.

## Expected Output

- Dataset previews and summary tables
- A bar chart of the two traffic classes
- NumPy duration statistics
- Predicted vs actual labels
- A decision-tree accuracy score

## Notes

The dataset is intentionally tiny and is meant to demonstrate the workflow,
not to produce a meaningful security model. Notebook outputs were cleared
before publishing; the submitted `report.pdf` contains the recorded results.
