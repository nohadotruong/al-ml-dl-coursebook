from lesson_1.config import (
    HOUSING_DATA,
    HOUSING_LABEL_COL,
    HOUSING_MODEL_DIR,
    TITANIC_TRAIN_DATA,
    TITANIC_TEST_DATA,
    TITANIC_SUBMISSIONS_DATA,
    TITANIC_LABEL_COL,
    TITANIC_MODEL_DIR,
)
import pandas as pd
from common.spliter import split_data
from sklearn.model_selection import train_test_split
from common.visualizer import plot_data_overview, plot_model_results
from common.cleaner import normal_preprocessing
from models.regression_models import train_dummy_model
from common.results import print_results
from common.saver import save_models


def housing_pipeline(raw_data_path, label_col, model_save_dir):
    df_raw = pd.read_csv(raw_data_path)
    X_raw = df_raw.drop(label_col, axis=1)
    y_raw = df_raw[label_col]

    plot_data_overview(df_raw)

    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X_raw, y_raw, 0.2, 0.1)

    preprocess = normal_preprocessing(X_train, num_strategy="mean", scale_numeric=True)

    mean_dummy_res = train_dummy_model(
        preprocess, X_train, y_train, X_val, X_test, strategy="mean"
    )
    mode_dummy_res = train_dummy_model(
        preprocess, X_train, y_train, X_val, X_test, strategy="most_frequent"
    )

    results = {
        "Dummy (Mean)": mean_dummy_res,
        "Dummy (Mode)": mode_dummy_res,
    }

    print_results(results, y_val, y_test)
    plot_model_results(results, y_val, y_test)
    save_models(results, model_save_dir)


def titanic_pipeline(
    train_data_path,
    test_data_path,
    submission_data_path,
    label_col,
    model_save_col,
):
    df_train = pd.read_csv(train_data_path)
    X_raw_train = df_train.drop([label_col, "PassengerId", "Cabin"], axis=1)
    y_raw_train = df_train[label_col]

    X_train, X_val, y_train, y_val = train_test_split(
        X_raw_train, y_raw_train, test_size=0.2, random_state=42
    )

    df_test = pd.read_csv(test_data_path)
    df_sub = pd.read_csv(submission_data_path)

    df_test = df_test.merge(df_sub, on="PassengerId")
    X_test = df_test.drop(["PassengerId", "Cabin", "Survived"], axis=1)
    y_test = df_test["Survived"]

    plot_data_overview(X_train)

    preprocess = normal_preprocessing(X_train, num_strategy="mean", scale_numeric=True)

    X_train_prep = preprocess.fit_transform(X_train)
    X_val_prep = preprocess.transform(X_val)
    X_test_prep = preprocess.transform(X_test)

    num_cols = preprocess.transformers_[0][2]
    cat_cols = (
        preprocess.transformers_[1][2] if len(preprocess.transformers_) > 1 else []
    )
    ohe = (
        preprocess.transformers_[1][1].named_steps["ohe"]
        if len(preprocess.transformers_) > 1
        else None
    )
    if ohe:
        cat_ohe_cols = ohe.get_feature_names_out(cat_cols)
    else:
        cat_ohe_cols = []

    all_cols = num_cols + list(cat_ohe_cols)

    X_train_df = pd.DataFrame(X_train_prep, columns=all_cols, index=X_train.index)
    X_val_df = pd.DataFrame(X_val_prep, columns=all_cols, index=X_val.index)
    X_test_df = pd.DataFrame(X_test_prep, columns=all_cols, index=X_test.index)

    X_train_df.to_csv("X_train_preprocessed.csv", index=False)
    X_val_df.to_csv("X_val_preprocessed.csv", index=False)
    X_test_df.to_csv("X_test_preprocessed.csv", index=False)


titanic_pipeline(
    TITANIC_TRAIN_DATA,
    TITANIC_TEST_DATA,
    TITANIC_SUBMISSIONS_DATA,
    TITANIC_LABEL_COL,
    TITANIC_MODEL_DIR,
)
