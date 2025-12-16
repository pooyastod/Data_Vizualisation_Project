import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Load data
df = pd.read_excel("dataviz.xlsx")

# Drop non-numeric / unwanted columns
df = df.drop(columns=["cnt", "cycle"], errors="ignore")

# Correlation matrix
corr = df.select_dtypes(include=[np.number]).corr()

# Green → white → red colormap
cmap = LinearSegmentedColormap.from_list(
    "green_white_red", ["red", "white", "green"]
)

# Plot
plt.figure(figsize=(10, 8))
plt.imshow(corr, cmap=cmap, vmin=-1, vmax=1)
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Between Variables", pad=20)
plt.tight_layout()
plt.show()