"""
Experiment: Build and compare Decision Tree and Random Forest models on an IDS dataset.
Dataset file expected: ids_dataset.csv

This sample CSV is inspired by KDD/NSL-KDD style features:
- protocol_type, service, flag are categorical network features
- numeric fields describe traffic volume and connection statistics
- label is the target: normal or attack
"""

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier


# 1. Load IDS dataset
DATASET_PATH = "ids_dataset.csv"
df = pd.read_csv(DATASET_PATH)

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# 2. Separate input features and target label
X = df.drop("label", axis=1)
y = df["label"]

# 3. Identify categorical and numerical columns
categorical_features = ["protocol_type", "service", "flag"]
numerical_features = [col for col in X.columns if col not in categorical_features]

# 4. Preprocessing:
#    - OneHotEncoder converts text features into numbers
#    - StandardScaler normalizes numerical features
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", StandardScaler(), numerical_features),
    ]
)

# 5. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y,
)

# 6. Create Decision Tree model pipeline
decision_tree_model = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        ("classifier", DecisionTreeClassifier(random_state=42, max_depth=5)),
    ]
)

# 7. Create Random Forest model pipeline
random_forest_model = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42,
                max_depth=5,
            ),
        ),
    ]
)

# 8. Train both models
decision_tree_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)

# 9. Make predictions on test data
dt_predictions = decision_tree_model.predict(X_test)
rf_predictions = random_forest_model.predict(X_test)

# 10. Evaluate both models
dt_accuracy = accuracy_score(y_test, dt_predictions)
rf_accuracy = accuracy_score(y_test, rf_predictions)

print("\n================ MODEL COMPARISON ================")
print(f"Decision Tree Accuracy : {dt_accuracy:.2f}")
print(f"Random Forest Accuracy : {rf_accuracy:.2f}")

print("\nDecision Tree Confusion Matrix:")
print(confusion_matrix(y_test, dt_predictions))

print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, rf_predictions))

print("\nDecision Tree Classification Report:")
print(classification_report(y_test, dt_predictions))

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_predictions))

# 11. Simple conclusion
if rf_accuracy > dt_accuracy:
    print("\nConclusion: Random Forest performed better than Decision Tree.")
elif rf_accuracy < dt_accuracy:
    print("\nConclusion: Decision Tree performed better than Random Forest.")
else:
    print("\nConclusion: Both models gave the same accuracy on this sample dataset.")
