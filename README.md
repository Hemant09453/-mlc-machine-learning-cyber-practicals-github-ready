# MLC Lab - Machine Learning for Cyber Security

Practical work for **Machine Learning for Cyber Security Lab (23CS702P)**,
Semester 7, B.Tech Computer Science & Engineering (Cyber Security),
St. Vincent Pallotti College of Engineering & Technology, Nagpur.

**Author:** Hemant Marotkar (UID 23015002)  
**GitHub:** [@harshal0002](https://github.com/harshal0002)

---

## Overview

This repository contains ten machine-learning practicals applied to cyber
security problems. Each practical is self-contained and includes the notebook
or script, the dataset used, and the submitted PDF/DOCX report with results
and screenshots.

The work covers the full basic ML workflow:

- Python and data-stack setup
- data cleaning and feature preparation
- supervised classification (Decision Tree, Random Forest, SVM)
- unsupervised learning (hierarchical clustering, DBSCAN)
- dimensionality reduction with PCA
- model evaluation with confusion matrix, ROC and AUC
- adversarial machine learning and ethical considerations

---

## Practicals

| # | Practical | Main concepts | Dataset | Report |
|---|---|---|---|---|
| 01 | [Python and ML basics](./practical-01-python-ml-basics) | NumPy, Pandas, Matplotlib, scikit-learn, Decision Tree | `basic_cyber_dataset.csv` | [PDF](./practical-01-python-ml-basics/report.pdf) |
| 02 | [Data preprocessing](./practical-02-data-preprocessing) | duplicates, missing values, normalization, label encoding | `network_security_dataset.csv` | [PDF](./practical-02-data-preprocessing/report.pdf) |
| 03 | [Malware classification](./practical-03-malware-classification) | Random Forest, label encoding, standard scaling | `malware_dataset.csv` | [PDF](./practical-03-malware-classification/report.pdf) |
| 04 | [Decision Tree vs Random Forest](./practical-04-decision-tree-vs-random-forest) | pipelines, one-hot encoding, model comparison | `ids_dataset.csv`, `ids_dataset_rf_better.csv` | [Part 1](./practical-04-decision-tree-vs-random-forest/report-part1.pdf) / [Part 2](./practical-04-decision-tree-vs-random-forest/report-part2.pdf) |
| 05 | [Hierarchical clustering](./practical-05-hierarchical-clustering) | unsupervised clustering, dendrogram interpretation | virtual-lab dataset | [PDF](./practical-05-hierarchical-clustering/report.pdf) |
| 06 | [SVM phishing classification](./practical-06-svm-phishing) | feature extraction, Support Vector Machine | `phishing_dataset.csv` | [PDF](./practical-06-svm-phishing/report.pdf) |
| 07 | [PCA dimensionality reduction](./practical-07-pca-dimensionality-reduction) | explained variance, lower-dimensional visualisation | high-dimensional cyber data | [PDF](./practical-07-pca-dimensionality-reduction/report.pdf) |
| 08 | [DBSCAN anomaly detection](./practical-08-dbscan-anomaly-detection) | density-based clustering, outlier detection | `network_traffic_anomaly.csv` | [PDF](./practical-08-dbscan-anomaly-detection/report.pdf) |
| 09 | [Model evaluation](./practical-09-model-evaluation) | confusion matrix, ROC curve, AUC score | `cyber_classification_eval_dataset.csv` | [PDF](./practical-09-model-evaluation/report.pdf) |
| 10 | [Adversarial ML](./practical-10-adversarial-ml) | evasion, poisoning, robustness and ethics | `adversarial_cyber_dataset.csv` | [PDF](./practical-10-adversarial-ml/report.pdf) |

Additional practice work is in [`practice-and-notes/`](./practice-and-notes).
The official syllabus is in [`syllabus/`](./syllabus).

---

## Repository structure

```text
mlc-lab/
├── practical-01-python-ml-basics/
├── practical-02-data-preprocessing/
├── practical-03-malware-classification/
├── practical-04-decision-tree-vs-random-forest/
├── practical-05-hierarchical-clustering/
├── practical-06-svm-phishing/
├── practical-07-pca-dimensionality-reduction/
├── practical-08-dbscan-anomaly-detection/
├── practical-09-model-evaluation/
├── practical-10-adversarial-ml/
├── practice-and-notes/
├── syllabus/
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Getting started

### 1. Create a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Open the notebooks

```bash
jupyter lab
```

Open the notebook inside a practical folder and run the cells from top to
bottom. Every notebook reads its dataset from the same folder, so no path
changes are needed.

Standalone Python scripts can be run directly, for example:

```bash
python practical-04-decision-tree-vs-random-forest/compare_dt_rf_ids.py
```

---

## Notes

- Notebook **outputs were cleared** before publishing so that saved logs and
  local machine paths do not leak into the repository. The PDF/DOCX reports
  contain the recorded outputs, plots and observations.
- The included CSV files are small teaching datasets intended for these lab
  exercises. For a larger study, replace them with public datasets such as
  NSL-KDD, CICIDS2017, or a malware/URL dataset.
- If a notebook or script is run from a different working directory, update
  the dataset path at the top of the file.

---

## Ethical use

This material is for education and defensive security only. Do not use the
datasets, models, or techniques against systems or networks without explicit
permission. The adversarial-ML practical is intended to help defenders
understand and mitigate attacks, not to cause harm.

---

## License

Released under the [MIT License](./LICENSE).
