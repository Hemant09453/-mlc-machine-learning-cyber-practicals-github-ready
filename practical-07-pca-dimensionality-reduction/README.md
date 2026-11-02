# Practical 07 - PCA for Dimensionality Reduction

## Aim

Apply Principal Component Analysis (PCA) to reduce the dimensionality of
high-dimensional cyber-security data and visualise the reduced feature space.

## Files

| File | Purpose |
|---|---|
| `screenshots/` | PCA plots, explained variance, and visualisations |
| `report.pdf` | Submitted lab report |
| `report.docx` | Editable report source |

## What the Practical Covers

- The curse of dimensionality
- Standardisation before PCA
- Covariance / eigenvalues and eigenvectors (concept)
- Explained variance and scree plots
- Selecting the number of principal components
- Visualising data in 2D using the first two PCs
- Trade-off between compression and information loss

The experiment was done in the virtual lab. This folder preserves the report
and screenshots.

## How to Reproduce

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_csv("your_dataset.csv")
X = df.select_dtypes("number")
X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total explained:", pca.explained_variance_ratio_.sum())

plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Visualisation")
plt.show()
```

## Expected Observations

- Standardisation is required because PCA is variance-based.
- PC1 captures the most variance, followed by PC2.
- A 2D plot can reveal clusters/separability that are hard to see in high dimensions.
- Retaining a few components can preserve most of the information while reducing complexity.

## Notes

Refer to the screenshots and `report.pdf` for the exact dataset used and the
recorded observations from the virtual-lab session.
