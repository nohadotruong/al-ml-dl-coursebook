from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import pandas as pd


def normal_preprocessing(
    X_train: pd.DataFrame,
    num_strategy: str = "median",
    cat_strategy: str = "most_frequent",
    scale_numeric: bool = True,
):
    num_cols = X_train.select_dtypes(include=["number"]).columns.tolist()
    cat_cols = X_train.select_dtypes(include=["object", "category"]).columns.tolist()
    bool_cols = X_train.select_dtypes(include=["bool"]).columns.tolist()

    transformers = []

    if num_cols:
        num_steps = [("imputer", SimpleImputer(strategy=num_strategy))]

        if scale_numeric:
            num_steps.append(("scaler", StandardScaler()))

        num_pipeline = Pipeline(num_steps)
        transformers.append(("num", num_pipeline, num_cols))

    if cat_cols:
        cat_pipeline = Pipeline(
            [
                ("imputer", SimpleImputer(strategy=cat_strategy, fill_value="missing")),
                ("ohe", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
            ]
        )
        transformers.append(("cat", cat_pipeline, cat_cols))

        transformers.append(("bool", "passthrough", bool_cols))

    preprocess = ColumnTransformer(transformers)

    return preprocess
