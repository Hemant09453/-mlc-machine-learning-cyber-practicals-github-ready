"""
Experiment: Adversarial Attacks, Model Poisoning, Evasion Techniques,
and Ethical Challenges in ML-Based Cyber Defense

Dataset:
    adversarial_cyber_dataset.csv

Label meaning:
    0 = Normal traffic
    1 = Attack traffic

This program demonstrates:
1. Training a baseline ML cyber defense model.
2. Evasion attack: modifying malicious samples at test time to fool the model.
3. Model poisoning: corrupting training labels to reduce model performance.
4. Ethical discussion points printed at the end.
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------
df = pd.read_csv("adversarial_cyber_dataset.csv")

print("First five records of dataset:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nClass distribution:")
print(df["label"].value_counts())


# --------------------------------------------------
# 2. Separate features and label
# --------------------------------------------------
X = df.drop("label", axis=1)
y = df["label"]

feature_names = X.columns.tolist()


# --------------------------------------------------
# 3. Split dataset into training and testing parts
# --------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.30,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# 4. Normalize numerical features
# --------------------------------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# --------------------------------------------------
# 5. Train baseline cyber defense model
# --------------------------------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train_scaled, y_train)

baseline_predictions = model.predict(X_test_scaled)

print("\n================ BASELINE MODEL ================")
print("Accuracy:", accuracy_score(y_test, baseline_predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, baseline_predictions))
print("\nClassification Report:")
print(classification_report(y_test, baseline_predictions))


# --------------------------------------------------
# 6. Evasion attack simulation
# --------------------------------------------------
"""
Evasion attack means the attacker changes malicious test samples
slightly so that they look closer to normal traffic.

In this safe simulation, attack samples are not converted into real attacks.
Only numeric feature values are shifted toward the average normal traffic profile.
"""

X_test_evasion = X_test.copy()

normal_profile = X_train[y_train == 0].mean()

attack_indices = y_test[y_test == 1].index

for idx in attack_indices:
    # Move malicious samples 35% closer to normal traffic pattern
    X_test_evasion.loc[idx, feature_names] = (
        0.65 * X_test_evasion.loc[idx, feature_names] +
        0.35 * normal_profile[feature_names]
    )

X_test_evasion_scaled = scaler.transform(X_test_evasion)
evasion_predictions = model.predict(X_test_evasion_scaled)

print("\n================ EVASION ATTACK TEST ================")
print("Accuracy after evasion:", accuracy_score(y_test, evasion_predictions))
print("\nConfusion Matrix after evasion:")
print(confusion_matrix(y_test, evasion_predictions))
print("\nClassification Report after evasion:")
print(classification_report(y_test, evasion_predictions))


# --------------------------------------------------
# 7. Model poisoning attack simulation
# --------------------------------------------------
"""
Model poisoning means the attacker corrupts training data.
Here, we simulate poisoning by flipping some attack labels to normal labels.

Example:
Original: attack traffic labelled as 1
Poisoned: some attack traffic wrongly labelled as 0

This teaches the model incorrect patterns and reduces trustworthiness.
"""

y_train_poisoned = y_train.copy()

attack_train_indices = y_train_poisoned[y_train_poisoned == 1].index

np.random.seed(42)
poison_count = int(0.20 * len(attack_train_indices))
poisoned_indices = np.random.choice(
    attack_train_indices,
    size=poison_count,
    replace=False
)

y_train_poisoned.loc[poisoned_indices] = 0

poisoned_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

poisoned_model.fit(X_train_scaled, y_train_poisoned)

poisoned_predictions = poisoned_model.predict(X_test_scaled)

print("\n================ MODEL POISONING TEST ================")
print("Accuracy after poisoning:", accuracy_score(y_test, poisoned_predictions))
print("\nConfusion Matrix after poisoning:")
print(confusion_matrix(y_test, poisoned_predictions))
print("\nClassification Report after poisoning:")
print(classification_report(y_test, poisoned_predictions))


# --------------------------------------------------
# 8. Feature importance
# --------------------------------------------------
importance = pd.DataFrame({
    "feature": feature_names,
    "importance": model.feature_importances_
}).sort_values(by="importance", ascending=False)

print("\n================ FEATURE IMPORTANCE ================")
print(importance)


# --------------------------------------------------
# 9. Ethical discussion points
# --------------------------------------------------
print("\n================ ETHICAL CHALLENGES ================")
print("1. Use adversarial ML experiments only in controlled lab environments.")
print("2. Do not use evasion knowledge to bypass real security systems.")
print("3. Protect training datasets from unauthorized modification.")
print("4. Avoid collecting personal or sensitive user data unnecessarily.")
print("5. Explainable and auditable ML models are important in cyber defense.")
print("6. Human verification is required before taking serious actions like blocking users.")
