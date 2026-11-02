"""
Experiment: Evaluate classification models using Confusion Matrix, ROC Curve and AUC Score
Cyber Security Context: Classify network traffic as Normal (0) or Attack (1)

Required libraries:
pip install pandas scikit-learn matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    roc_curve,
    auc,
    roc_auc_score
)

# ---------------------------------------------------------
# 1. Load cyber security dataset
# ---------------------------------------------------------
df = pd.read_csv("cyber_classification_eval_dataset.csv")

print("First five rows of dataset:")
print(df.head())

# ---------------------------------------------------------
# 2. Separate input features and target label
# ---------------------------------------------------------
# X contains traffic features such as packet count, bytes, failed logins, etc.
# y contains class label:
# 0 = Normal traffic
# 1 = Attack traffic
X = df.drop("attack", axis=1)
y = df["attack"]

# ---------------------------------------------------------
# 3. Split dataset into training and testing sets
# ---------------------------------------------------------
# stratify=y keeps equal proportion of Normal and Attack records
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# ---------------------------------------------------------
# 4. Define classification models
# ---------------------------------------------------------
models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression())
    ]),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

# ---------------------------------------------------------
# 5. Train, predict and evaluate each model
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))

for model_name, model in models.items():
    print("\n" + "=" * 60)
    print("Model:", model_name)

    # Train model
    model.fit(X_train, y_train)

    # Predict class labels
    y_pred = model.predict(X_test)

    # Predict probability score for Attack class
    y_score = model.predict_proba(X_test)[:, 1]

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    print("\nConfusion Matrix:")
    print(cm)

    # Classification Report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["Normal", "Attack"]))

    # AUC Score
    auc_score = roc_auc_score(y_test, y_score)
    print("AUC Score:", round(auc_score, 3))

    # Save confusion matrix image
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Normal", "Attack"]
    )
    disp.plot()
    plt.title(f"Confusion Matrix - {model_name}")
    plt.savefig(f"confusion_matrix_{model_name.replace(' ', '_').lower()}.png")
    plt.close()

    # ROC Curve
    fpr, tpr, thresholds = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)

    plt.plot(fpr, tpr, label=f"{model_name} AUC = {roc_auc:.3f}")

# ---------------------------------------------------------
# 6. Plot and save combined ROC curve
# ---------------------------------------------------------
plt.plot([0, 1], [0, 1], linestyle="--", label="Random Guess")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for Cyber Attack Classification")
plt.legend()
plt.grid(True)
plt.savefig("roc_curve_models.png")
plt.show()
