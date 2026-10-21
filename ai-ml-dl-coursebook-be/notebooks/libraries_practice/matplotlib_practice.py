import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read csv file
df = pd.read_csv(
    r"D:\JOB\CodeDream\AI-ML-DL-Course\server\data\california-housing\raw\california-housing.csv"
)

# Check data
print(df.head())
print(df.info())
print(df.describe())
print(df["total_rooms"])


# Fill missing values (for total_bedrooms)
df["total_bedrooms"].fillna(df["total_bedrooms"].median(), inplace=True)

# Create figure with multiple subplots
fig, axes = plt.subplots(3, 3, figsize=(18, 15))
fig.suptitle("California Housing Data – All Chart Types", fontsize=18)

# 1️⃣ Line plot: Median Income over rows
axes[0, 0].plot(df.index[:100], df["median_income"][:100], color="blue", marker="o")
axes[0, 0].set_title("Line Plot: Median Income")
axes[0, 0].set_xlabel("Index")
axes[0, 0].set_ylabel("Median Income")

# 2️⃣ Bar chart: Average house value by Ocean Proximity
avg_house_value = df.groupby("ocean_proximity")["median_house_value"].mean()
axes[0, 1].bar(avg_house_value.index, avg_house_value.values, color="orange")
axes[0, 1].set_title("Bar Chart: Avg House Value by Region")
axes[0, 1].set_xlabel("Ocean Proximity")
axes[0, 1].set_ylabel("Median House Value")

# 3️⃣ Histogram: Distribution of Median House Value
axes[0, 2].hist(df["median_house_value"], bins=30, color="green", edgecolor="black")
axes[0, 2].set_title("Histogram: House Value Distribution")
axes[0, 2].set_xlabel("Median House Value")
axes[0, 2].set_ylabel("Frequency")

# 4️⃣ Boxplot: House Value by Ocean Proximity
categories = df["ocean_proximity"].unique()
data = [df[df["ocean_proximity"] == cat]["median_house_value"] for cat in categories]
axes[1, 0].boxplot(data, labels=categories, patch_artist=True)
axes[1, 0].set_title("Boxplot: House Value by Region")
axes[1, 0].set_ylabel("Median House Value")

# 5️⃣ Scatter plot: Population vs Median Income
axes[1, 1].scatter(df["population"], df["median_income"], color="purple", alpha=0.5)
axes[1, 1].set_title("Scatter: Population vs Income")
axes[1, 1].set_xlabel("Population")
axes[1, 1].set_ylabel("Median Income")

# 6️⃣ Pie chart: Proportion of Ocean Proximity
counts = df["ocean_proximity"].value_counts()
axes[1, 2].pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90)
axes[1, 2].set_title("Pie Chart: Ocean Proximity Distribution")

# 7️⃣ Area chart: Cumulative population (line filled)
axes[2, 0].fill_between(
    df.index[:200], df["population"][:200].cumsum(), color="skyblue", alpha=0.5
)
axes[2, 0].set_title("Area Chart: Cumulative Population")
axes[2, 0].set_xlabel("Index")
axes[2, 0].set_ylabel("Cumulative Population")

# 8️⃣ Stacked bar chart: Total rooms vs total bedrooms by first 10 rows
axes[2, 1].bar(df.index[:10], df["total_rooms"][:10], label="Total Rooms")
axes[2, 1].bar(
    df.index[:10],
    df["total_bedrooms"][:10],
    bottom=df["total_rooms"][:10],
    label="Total Bedrooms",
)
axes[2, 1].set_title("Stacked Bar: Rooms vs Bedrooms")
axes[2, 1].set_xlabel("Index")
axes[2, 1].set_ylabel("Count")
axes[2, 1].legend()

# 9️⃣ Heatmap: Correlation matrix of numeric columns
corr = df.select_dtypes(include=np.number).corr()
im = axes[2, 2].imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
axes[2, 2].set_xticks(range(len(corr.columns)))
axes[2, 2].set_yticks(range(len(corr.columns)))
axes[2, 2].set_xticklabels(corr.columns, rotation=45, ha="right")
axes[2, 2].set_yticklabels(corr.columns)
axes[2, 2].set_title("Heatmap: Correlation Matrix")
fig.colorbar(im, ax=axes[2, 2], fraction=0.046, pad=0.04)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
