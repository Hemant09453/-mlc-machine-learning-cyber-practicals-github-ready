# Practical 02 - Data Preprocessing

## Aim

Prepare a raw network-security dataset for machine learning by removing
duplicates, handling missing values, encoding categorical features, and
normalising numeric features.

## Dataset

`network_security_dataset.csv` contains 20 connection records with:

`connection_id`, `protocol`, `service`, `src_bytes`, `dst_bytes`, `duration`,
`packet_count`, `login_attempts`, `flag`, and `label`.

The CSV deliberately contains a few missing values and mixed data types so
that the cleaning steps are visible.

## Files

| File | Purpose |
|---|---|
| `data-preprocessing.ipynb` | Main notebook |
| `network_security_dataset.csv` | Raw input dataset |
| `report.pdf` | Submitted lab report |

## Preprocessing Pipeline

1. Remove duplicate rows.
2. Check missing values in every column.
3. Fill numeric gaps with the column mean:
   `src_bytes`, `dst_bytes`, `duration`, `packet_count`, `login_attempts`.
4. Fill categorical gaps with the column mode:
   `protocol`, `service`, `flag`.
5. Label-encode the categorical features and the target label.
6. Scale numeric features to the 0-1 range with `MinMaxScaler`.
7. Print the cleaned dataset.

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

Open `practical-02-data-preprocessing/data-preprocessing.ipynb` and run the
cells in order.

## Expected Output

- The original dataset
- Missing-value counts
- A fully numeric, normalised dataset ready for a model

## Notes

- `LabelEncoder` is used separately for each categorical column. For a larger
  project, use a `ColumnTransformer` pipeline so encoding and scaling are fit
  only on training data and reused for test data.
- Notebook outputs were cleared before publishing; the report contains the
  recorded results.
