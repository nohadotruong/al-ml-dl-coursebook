import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"D:\JOB\CodeDream\AI-ML-DL-Course\server\data\california-housing\raw\california-housing.csv"
)

# Fill missing values for total_bedrooms
df["total_bedrooms"].fillna(df["total_bedrooms"].median(), inplace=True)

# Set Seaborn style
sns.set(style="whitegrid", palette="pastel")

# 1️⃣ Histogram – Distribution of median_house_value
plt.figure(figsize=(8, 4))
sns.histplot(df["median_house_value"], bins=30, kde=True, color="skyblue")
plt.title("Histogram: Median House Value")
plt.xlabel("House Value ($)")
plt.ylabel("Frequency")
plt.show()

# 2️⃣ Scatter plot – Median Income vs Median House Value
plt.figure(figsize=(8, 4))
sns.scatterplot(
    x="median_income", y="median_house_value", data=df, hue="ocean_proximity", alpha=0.6
)
plt.title("Scatter: Income vs House Value")
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.legend(title="Ocean Proximity")
plt.show()

# 3️⃣ Boxplot – House Value by Ocean Proximity
plt.figure(figsize=(8, 4))
sns.boxplot(x="ocean_proximity", y="median_house_value", data=df, palette="Set2")
plt.title("Boxplot: House Value by Ocean Proximity")
plt.xlabel("Ocean Proximity")
plt.ylabel("Median House Value")
plt.show()

# 4️⃣ Violin plot – Distribution of Median House Value by Ocean Proximity
plt.figure(figsize=(8, 4))
sns.violinplot(x="ocean_proximity", y="median_house_value", data=df, palette="Set3")
plt.title("Violin Plot: House Value by Ocean Proximity")
plt.xlabel("Ocean Proximity")
plt.ylabel("Median House Value")
plt.show()

# 5️⃣ Pairplot – Relationship between selected numeric features
sns.pairplot(df[["median_income", "median_house_value", "population", "households"]])
plt.suptitle("Pairplot: Numeric Relationships", y=1.02)
plt.show()

# 6️⃣ Heatmap – Correlation matrix of numeric columns
plt.figure(figsize=(8, 6))
corr = df.select_dtypes(include="number").corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap: Correlation Matrix")
plt.show()

# 7️⃣ Bar plot – Average House Value by Ocean Proximity
avg_house_value = (
    df.groupby("ocean_proximity")["median_house_value"].mean().reset_index()
)
plt.figure(figsize=(8, 4))
sns.barplot(
    x="ocean_proximity", y="median_house_value", data=avg_house_value, palette="muted"
)
plt.title("Bar Plot: Avg House Value by Region")
plt.xlabel("Ocean Proximity")
plt.ylabel("Average House Value")
plt.show()
