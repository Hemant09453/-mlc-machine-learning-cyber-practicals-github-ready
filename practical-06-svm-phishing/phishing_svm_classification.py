# Experiment: Extract features from phishing dataset and apply SVM classification
# Dataset file required: phishing_dataset.csv

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load the phishing dataset
# Each row represents a website/URL and extracted phishing-related features.
df = pd.read_csv("phishing_dataset.csv")

print("First five records of dataset:")
print(df.head())
print("\nDataset information:")
print(df.info())

# 2. Separate input features and output label
# X contains feature columns; y contains class label: phishing or legitimate.
X = df.drop("label", axis=1)
y = df["label"]

# 3. Convert text labels into numeric labels
# legitimate/phishing are converted into 0/1 values for machine learning.
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

print("\nLabel mapping:")
for class_name, encoded_value in zip(label_encoder.classes_, range(len(label_encoder.classes_))):
    print(class_name, "=", encoded_value)

# 4. Split dataset into training and testing data
# 70% data is used for training and 30% for testing.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.30,
    random_state=42,
    stratify=y_encoded
)

# 5. Feature scaling
# SVM is distance-based, so all features should be on a similar scale.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Create and train SVM classifier
# RBF kernel helps classify non-linear patterns in phishing data.
svm_model = SVC(kernel="rbf", C=1.0, gamma="scale", random_state=42)
svm_model.fit(X_train_scaled, y_train)

# 7. Predict labels for test data
y_pred = svm_model.predict(X_test_scaled)

# 8. Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)

print("\nModel Evaluation Results")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(report)

# 9. Test the model using a new sample URL feature record
# Feature order must be same as CSV columns except label.
new_sample = [[90, 1, 1, 1, 1, 5, 1, 1, 4, 1, 7, 1000000]]
new_sample_scaled = scaler.transform(new_sample)
predicted_class = svm_model.predict(new_sample_scaled)
predicted_label = label_encoder.inverse_transform(predicted_class)

print("\nPrediction for new sample website:", predicted_label[0])
