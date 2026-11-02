# Practical 05 - Hierarchical Clustering

## Aim

Apply hierarchical (agglomerative) clustering to unlabelled cyber-security
data and interpret the resulting dendrogram.

## Files

| File | Purpose |
|---|---|
| `screenshots/` | Dendrogram and cluster plots from the virtual lab |
| `report.pdf` | Submitted lab report |
| `report.docx` | Editable report source |

## What the Practical Covers

- Distance measures (Euclidean, Manhattan)
- Linkage methods (single, complete, average, Ward)
- Building and reading a dendrogram
- Choosing a cut height to form clusters
- Interpreting clusters without ground-truth labels

The experiment was completed in the virtual lab; this folder preserves the
report and the evidence screenshots. The original notebook was not included
in the source folder.

## How to Reproduce

A minimal Python version using the same workflow:

```python
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv("your_dataset.csv")
X = StandardScaler().fit_transform(df.select_dtypes("number"))

Z = linkage(X, method="ward")
dendrogram(Z)
plt.title("Hierarchical Clustering Dendrogram")
plt.show()
```

## Expected Observations

- The dendrogram shows the order in which records merge.
- A horizontal cut produces the final cluster count.
- Ward linkage usually gives compact, balanced clusters on scaled data.
- Clustering quality depends heavily on feature selection and scaling.

## Notes

The report is the authoritative record of the experiment. Notebook outputs
were not available for this practical, so the screenshots and PDF are the
submitted evidence.
