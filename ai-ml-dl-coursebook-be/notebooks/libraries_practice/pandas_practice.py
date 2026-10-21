import pandas as pd

df = pd.read_csv(
    r"D:\JOB\CodeDream\AI-ML-DL-Course\server\data\titanic-ml-from-disaster\raw\train.csv"
)

# Top 5 rows
print(df.head())

# Convert top 5 rows from DataFrame to String
print(df.head().to_string())

# Show a concise summary of the DataFrame, including:
# 1. Number of rows and columns.
# 2. Column names.
# 3. Data types of each column
# 4. Number of non-null values per column
# 5. Memory usage of the DataFrame.
print(df.info())

# Provides statistical summary of numeric columns: count, mean, std, min, max, quartiles.
print(df.describe())

# Computes correlation matrix between numeric columns to see relationships.
print(df.corr())

# Access by Column (Single or Multiple)
print(df["Name"])
print(df[["PassengerId", "Name"]])

# Access by row and column labels
print(df.loc[0, "Name"])

# Access by row and column index numbers
print(df.iloc[1:3, 0:2])

# Remove rows (or columns) that contain NaN (missing values)
df_clean = df.dropna()
print(df_clean.head())

# Replace NaN values with a specified value (mean, median, constant)
df_filled = df.fillna({"Age": df["Age"].mean(), "Ticket": df["Ticket"].mean()})
