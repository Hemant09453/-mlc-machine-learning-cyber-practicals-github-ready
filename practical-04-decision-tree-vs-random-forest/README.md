# Practical 04 - Decision Tree vs Random Forest

## Aim

Compare a Decision Tree classifier and a Random Forest classifier on an
intrusion-detection dataset, using a reusable preprocessing pipeline.

## Datasets

| File | Records | Purpose |
|---|---|---|
| `ids_dataset.csv` | 40 | Part 1 - baseline comparison |
| `ids_dataset_rf_better.csv` | 50 | Part 2 - dataset where Random Forest performs better |

Both files use the same 17 columns: connection duration, protocol type,
service, flag, byte counts, connection counts, error rates, and derived host
statistics, with a `label` target column.

## Files

| File | Purpose |
|---|---|
| `decision-tree-vs-random-forest.ipynb` | Part 1 notebook |
| `decision-tree-vs-random-forest-part2.ipynb` | Part 2 notebook |
| `compare_dt_rf_ids.py` | Standalone script version |
| `ids_dataset.csv`, `ids_dataset_rf_better.csv` | Input datasets |
| `notes.txt` | Short lab notes |
| `report-part1.pdf`, `report-part2.pdf` | Submitted reports |

## What the Notebooks Do

1. Load the IDS dataset and inspect its shape and first rows.
2. Split features and the `label` target.
3. Build a `ColumnTransformer`:
   - `OneHotEncoder` for `protocol_type`, `service`, and `flag`
   - `StandardScaler` for all numeric columns
4. Wrap the preprocessor and classifier in a scikit-learn `Pipeline`.
5. Train both models with `max_depth=5` and `random_state=42`:
   - `DecisionTreeClassifier`
   - `RandomForestClassifier(n_estimators=100)`
6. Compare accuracy, confusion matrices, and classification reports.
7. Print a conclusion indicating which model performed better.

## How to Run

Notebooks:

```bash
pip install -r requirements.txt
jupyter lab
```

Open either notebook from this folder and run all cells.

Standalone script:

```bash
python compare_dt_rf_ids.py
```

## Expected Output

- Model comparison table with both accuracy scores
- Confusion matrices for both models
- Per-class precision, recall, and F1-score
- An automatic conclusion about which model performed better

## Notes

The two datasets are deliberately small teaching samples. Part 2 shows a case
where the ensemble model benefits from the additional records. Do not treat
the reported accuracy as a real-world IDS benchmark.
