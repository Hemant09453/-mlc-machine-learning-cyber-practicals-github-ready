# Name: Hemant Marotkar ,UID: - 23015002 

# Detect outliers/anomalies in network traffic using density-based clustering (DBSCAN)

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, classification_report

# 1. Load the dataset
# The CSV file must be in the same folder as this Python file.
DATA_FILE = Path(__file__).resolve().parent / "network_traffic_anomaly.csv"
df = pd.read_csv(DATA_FILE)

print("First 5 rows of dataset:")
print(df.head())

# 2. Select only numerical features for clustering
# DBSCAN is unsupervised, so we do not use the label column for training.
features = [
    "packet_size",
    "connection_duration",
    "src_bytes",
    "dst_bytes",
    "packet_rate",
    "error_rate"
]

X = df[features]

# 3. Standardize features
# Scaling is important because features such as src_bytes and error_rate
# have very different ranges.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Apply DBSCAN clustering
# eps: radius around a point to search for neighbors
# min_samples: minimum number of nearby points required to form a dense region
model = DBSCAN(eps=1.0, min_samples=3)
df["cluster"] = model.fit_predict(X_scaled)

# In DBSCAN, cluster = -1 means noise/outlier/anomaly.
df["predicted_anomaly"] = df["cluster"].apply(lambda value: "anomaly" if value == -1 else "normal")

# 5. Display clustering result
print("\nDBSCAN clustering result:")
print(df[["packet_size", "connection_duration", "src_bytes", "dst_bytes", "packet_rate", "error_rate", "cluster", "predicted_anomaly"]])

# 6. Compare with actual labels if labels are available
print("\nConfusion Matrix:")
print(confusion_matrix(df["label"], df["predicted_anomaly"], labels=["normal", "anomaly"]))

print("\nClassification Report:")
print(classification_report(df["label"], df["predicted_anomaly"]))

# 7. Reduce dimensions using PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

df["PCA1"] = X_pca[:, 0]
df["PCA2"] = X_pca[:, 1]

# 8. Plot normal points and anomalies
normal_points = df[df["predicted_anomaly"] == "normal"]
anomaly_points = df[df["predicted_anomaly"] == "anomaly"]

plt.figure(figsize=(8, 6))
plt.scatter(normal_points["PCA1"], normal_points["PCA2"], label="Normal")
plt.scatter(anomaly_points["PCA1"], anomaly_points["PCA2"], label="Anomaly", marker="x", s=100)
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("Network Traffic Anomaly Detection using DBSCAN")
plt.legend()
plt.grid(True)
plt.show()

# 9. Save output result to a new CSV file
OUTPUT_FILE = Path(__file__).resolve().parent / "dbscan_anomaly_output.csv"
df.to_csv(OUTPUT_FILE, index=False)
print(f"\nOutput saved as {OUTPUT_FILE.name}")


