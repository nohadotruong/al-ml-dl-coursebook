import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def plot_data_overview(df_raw):
    print("\n=== Data Info ===")
    print(df_raw.info())

    print("\n=== Missing Values ===")
    missing_counts = df_raw.isnull().sum()
    print(missing_counts[missing_counts > 0])

    if missing_counts.any():
        plt.figure(figsize=(10, 4))
        sns.heatmap(df_raw.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Values Heatmap")
        plt.show()

    print("\n=== Numeric Summary ===")
    print(df_raw.describe())

    num_cols = df_raw.select_dtypes(include=["number"]).columns.tolist()
    cat_cols = df_raw.select_dtypes(include=["object", "category"]).columns.tolist()

    if num_cols:
        print("\n=== Numeric Features Distribution ===")
        df_raw[num_cols].hist(bins=20, figsize=(12, 8))
        plt.show()

    if cat_cols:
        print("\n=== Categorical Features Count ===")
        for col in cat_cols:
            plt.figure(figsize=(6, 4))
            sns.countplot(x=col, data=df_raw)
            plt.title(f"Count of {col}")
            plt.xticks(rotation=45)
            plt.show()


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
