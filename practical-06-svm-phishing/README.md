# Practical 06 - SVM for Phishing URL Classification

## Aim

Extract features from a phishing dataset and apply a Support Vector Machine
(SVM) classifier to distinguish phishing websites from legitimate ones.

## Dataset

`phishing_dataset.csv` contains 30 records with 12 numeric features and a
`label` column:

| Feature | Meaning |
|---|---|
| `url_length` | Length of the URL |
| `has_ip_address` | Use of IP address instead of domain |
| `has_at_symbol` | Presence of `@` |
| `has_hyphen` | Hyphen in domain |
| `prefix_suffix` | Prefix/suffix in domain name |
| `dots_count` | Number of dots in URL |
| `https_token` | Misuse of `https` token |
| `shortening_service` | Use of URL shortener |
| `subdomain_count` | Number of subdomains |
| `has_suspicious_words` | Presence of suspicious keywords |
| `domain_age_days` | Approximate domain age |
| `web_traffic_rank` | Website traffic rank (smaller/larger by dataset convention) |
| `label` | `phishing` or `legitimate` |

## Files

| File | Purpose |
|---|---|
| `svm-phishing-classification.ipynb` | Main notebook |
| `phishing_svm_classification.py` | Standalone script version |
| `phishing_dataset.csv` | Input dataset |
| `report.pdf` | Submitted lab report with results |

## What the Notebook Does

1. Loads the dataset and inspects it.
2. Splits features and labels.
3. Label-encodes the `phishing`/`legitimate` classes.
4. Splits 70/30 with stratification.
5. Standardises features with `StandardScaler` (important for SVM).
6. Trains an SVM with an RBF kernel.
7. Evaluates with accuracy, confusion matrix, and classification report.
8. Classifies a new synthetic sample URL feature vector.

## How to Run

Notebooks:

```bash
pip install -r requirements.txt
jupyter lab
```

Open `practical-06-svm-phishing/svm-phishing-classification.ipynb` and run all
cells.

Script:

```bash
python phishing_svm_classification.py
```

## Expected Output

- Label mapping (e.g. `legitimate = 0`, `phishing = 1`)
- Accuracy percentage
- Confusion matrix
- Precision, recall, F1-score
- Prediction for the new sample

## Notes

SVMs are sensitive to feature scaling, so `StandardScaler` is applied to both
train and test splits. The dataset is small and synthetic for lab purposes.
For real phishing detection, use richer lexical/host-based features and a
properly balanced dataset.
