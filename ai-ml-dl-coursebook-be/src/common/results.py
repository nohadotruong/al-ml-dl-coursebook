import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def print_results(results, y_true_val, y_true_test):
    data = {}
    for model_name, res in results.items():
        metrics = {}
        y_val = res["y_pred_val"]
        y_test = res["y_pred_test"]

        metrics["MAE_val"] = mean_absolute_error(y_true_val, y_val)
        metrics["MSE_val"] = mean_squared_error(y_true_val, y_val)
        metrics["R2_val"] = r2_score(y_true_val, y_val)

        metrics["MAE_test"] = mean_absolute_error(y_true_test, y_test)
        metrics["MSE_test"] = mean_squared_error(y_true_test, y_test)
        metrics["R2_test"] = r2_score(y_true_test, y_test)

        if "best_alpha" in res:
            metrics["best_alpha"] = res["best_alpha"]

        data[model_name] = metrics

    df_results = pd.DataFrame(data).T.round(3)
    print("\n=== Model Performance Summary ===")
    print(df_results)
    return df_results
