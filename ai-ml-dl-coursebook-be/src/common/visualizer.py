import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def plot_data_overview(df_raw):
    num_cols = df_raw.select_dtypes(include=["number"]).columns.tolist()
    cat_cols = df_raw.select_dtypes(include=["object"]).columns.tolist()

    print("\n=== Plotting numeric features histogram ===")
    df_raw[num_cols].hist(bins=20, figsize=(6, 6))
    plt.show()

    if cat_cols:
        for col in cat_cols:
            plt.figure(figsize=(6, 6))
            sns.countplot(x=col, data=df_raw)
            plt.title(f"Count plot of {col}")
            plt.show()


import matplotlib.pyplot as plt


def plot_model_results(results, y_true_val, y_true_test):
    for model_name, res in results.items():
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # 1 hàng, 2 cột

        # Validation
        axes[0].scatter(y_true_val, res["y_pred_val"], alpha=0.5)
        axes[0].plot(
            [y_true_val.min(), y_true_val.max()],
            [y_true_val.min(), y_true_val.max()],
            "r--",
        )
        axes[0].set_xlabel("True Value (Validation)")
        axes[0].set_ylabel("Predicted Value")
        axes[0].set_title(f"{model_name} - Validation")

        # Test
        axes[1].scatter(y_true_test, res["y_pred_test"], alpha=0.5)
        axes[1].plot(
            [y_true_test.min(), y_true_test.max()],
            [y_true_test.min(), y_true_test.max()],
            "r--",
        )
        axes[1].set_xlabel("True Value (Test)")
        axes[1].set_ylabel("Predicted Value")
        axes[1].set_title(f"{model_name} - Test")

        plt.tight_layout()  # căn chỉnh khoảng cách
        plt.show()
