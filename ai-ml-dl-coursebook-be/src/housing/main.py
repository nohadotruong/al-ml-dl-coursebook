import pandas as pd
from src.housing.config import RAW_DATA, MODEL_SAVE_DIR, LABEL_COL
from src.common.visualizer import plot_data_overview, plot_model_results
from src.common.spliter import split_data
from src.common.cleaner import normal_preprocessing
from models.regression_models import (
    train_dummy_model,
    train_linear_model,
    train_ridge_model,
)
from src.common.results import print_results
from src.common.saver import save_models
from src.housing.predict import housing_predict


def run_pipeline(raw_data_path, label_col):
    df_raw = pd.read_csv(raw_data_path)
    X_raw = df_raw.drop(label_col, axis=1)
    y_raw = df_raw[label_col]

    plot_data_overview(df_raw)

    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X_raw, y_raw, 0.2, 0.1)

    preprocess = normal_preprocessing(X_train, num_strategy="mean", scale_numeric=True)

    mean_dummy_res = train_dummy_model(
        preprocess, X_train, y_train, X_val, X_test, strategy="mean"
    )
    median_dummy_res = train_dummy_model(
        preprocess, X_train, y_train, X_val, X_test, strategy="median"
    )
    linear_res = train_linear_model(preprocess, X_train, y_train, X_val, X_test)
    ridge_res = train_ridge_model(preprocess, X_train, y_train, X_val, X_test)

    results = {
        "Dummy (Mean)": mean_dummy_res,
        "Dummy (Median)": median_dummy_res,
        "Linear": linear_res,
        "Ridge": ridge_res,
    }

    print_results(results, y_val, y_test)
    plot_model_results(results, y_val, y_test)
    save_models(results, MODEL_SAVE_DIR)


run_pipeline(RAW_DATA, LABEL_COL)
data_sample = {
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41.0,
    "total_rooms": 880.0,
    "total_bedrooms": 129.0,
    "population": 322.0,
    "households": 126.0,
    "median_income": 8.3252,
    "ocean_proximity": "NEAR BAY",
}

housing_predict(data_sample, MODEL_SAVE_DIR)
