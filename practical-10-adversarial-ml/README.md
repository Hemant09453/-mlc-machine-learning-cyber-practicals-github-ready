# Practical 10 - Adversarial Machine Learning

## Aim

Study adversarial attacks against ML-based cyber-defence models, including
evasion, model poisoning, and the ethical challenges of deploying ML in
security.

## Dataset

`adversarial_cyber_dataset.csv` contains 240 records with eight columns:

`duration`, `src_bytes`, `dst_bytes`, `packet_count`, `failed_logins`,
`same_srv_rate`, `serror_rate`, and `label` (`0` = normal, `1` = attack).

## Files

| File | Purpose |
|---|---|
| `adversarial-ml.ipynb` | Main notebook |
| `adversarial_ml_cyber_defense.py` | Standalone script |
| `adversarial_cyber_dataset.csv` | Input dataset |
| `report.pdf` | Submitted lab report with results |

## What the Notebook Does

1. Loads the dataset and checks class distribution.
2. Splits the data 70/30 with stratification.
3. Standardises the features.
4. Trains a baseline Random Forest cyber-defence model.
5. Reports baseline accuracy, confusion matrix, and classification report.
6. **Evasion simulation:** shifts attack samples 35% toward the average normal
   traffic profile, then re-scores the model to show accuracy degradation.
7. **Poisoning simulation:** corrupts a portion of training labels and
   retrains to show the effect of contaminated training data.
8. Discusses defensive strategies and ethical constraints.

## How to Run

Notebook:

```bash
pip install -r requirements.txt
jupyter lab
```

Open `practical-10-adversarial-ml/adversarial-ml.ipynb` and run all cells.

Script:

```bash
python adversarial_ml_cyber_defense.py
```

## Expected Output

- Baseline vs post-evasion accuracy
- Baseline vs poisoned-model accuracy
- Confusion matrices and classification reports
- Commentary on robustness and ethics

## Notes

- The attacks are **controlled simulations** on a local teaching dataset. No
  real system is targeted.
- Evasion changes test-time features; poisoning changes training labels. Keep
  the two concepts distinct in the report.
- Possible defences to discuss: adversarial training, input validation,
  feature-space anomaly detection, model monitoring, and retraining with
  vetted data.

## Ethical Use

This practical is for understanding and improving defensive ML. Do not use
adversarial techniques against systems you do not own or lack permission to
test.
