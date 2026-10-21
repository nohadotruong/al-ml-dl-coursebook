import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# --- Fill missing values ---
def fill_missing_numeric(df, col, strategy="median"):
    if strategy == "median":
        df[col] = df[col].fillna(df[col].median())
    elif strategy == "mean":
        df[col] = df[col].fillna(df[col].mean())
    return df


def fill_missing_categorical(df, col, strategy="mode"):
    if strategy == "mode":
        df[col] = df[col].fillna(df[col].mode()[0])
    elif strategy == "unknown":
        df[col] = df[col].fillna("Unknown")
    return df


# --- Scale numeric columns ---
def scale_numeric(df, col):
    scaler = StandardScaler()
    df[col + "_scaled"] = scaler.fit_transform(df[[col]])
    return df


# --- Encode categorical columns ---
def encode_categorical(df, col):
    ohe = OneHotEncoder(sparse_output=False)
    encoded = ohe.fit_transform(df[[col]])
    encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out([col]))
    df = pd.concat([df, encoded_df], axis=1)
    df = df.drop(col, axis=1)
    return df


# --- Feature engineering ---
def feature_engineering(df):
    # Family size & alone
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

    # Extract Title from Name
    df["Title"] = df["Name"].str.extract("([A-Za-z]+)\.", expand=False)
    rare_titles = [
        "Lady",
        "Countess",
        "Capt",
        "Col",
        "Don",
        "Dr",
        "Major",
        "Rev",
        "Sir",
        "Jonkheer",
    ]
    df["Title"] = df["Title"].replace(rare_titles, "Other")

    # Fare bands
    df["FareBand"] = pd.qcut(df["Fare"], 4, labels=False)

    return df


# --- Drop unnecessary columns ---
def drop_columns(df, cols):
    return df.drop(cols, axis=1)


# --- Full preprocessing pipeline ---
def preprocess_titanic(df):
    # 1️⃣ Fill missing values
    df = fill_missing_numeric(df, "Age")
    df = fill_missing_categorical(df, "Embarked")

    # 2️⃣ Feature engineering
    df = feature_engineering(df)

    # 3️⃣ Scale numeric columns
    df = scale_numeric(df, "Age")
    df = scale_numeric(df, "Fare")

    # 4️⃣ Encode categorical columns
    df = encode_categorical(df, "Sex")
    df = encode_categorical(df, "Embarked")
    df = encode_categorical(df, "Title")

    # 5️⃣ Drop columns not needed
    df = drop_columns(df, ["Cabin", "Ticket", "Name"])

    return df
