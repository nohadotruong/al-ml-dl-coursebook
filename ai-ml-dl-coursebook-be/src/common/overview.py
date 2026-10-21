import pandas as pd
import matplotlib.pyplot as plt


def visualization(df, title="Data Overview"):
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    # 1. Data types pie chart
    dtype_counts = df.dtypes.value_counts()

    # 2. Numeric describe (multi-bar chart)
    describe_stats = df[numeric_cols].describe().T
    describe_stats = describe_stats[["mean", "std", "min", "25%", "50%", "75%", "max"]]

    # 3. Missing values (all columns)
    null_summary = df.isnull().sum().to_frame(name="Null Count")
    null_summary["Null %"] = df.isnull().mean() * 100

    # --- Plot with gridspec ---
    fig = plt.figure(figsize=(13, 6))
    fig.suptitle(title, fontsize=18)
    gs = fig.add_gridspec(2, 4, height_ratios=[1, 2], hspace=1)

    # 1. Data types pie chart (top-left)
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.pie(
        dtype_counts.values,
        labels=dtype_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["skyblue", "lightgreen", "salmon"],
    )
    ax0.set_title("Data Types Distribution", fontsize=16)

    # 2. Missing values (top-right) - show all columns
    ax1 = fig.add_subplot(gs[0, 1:])
    ax1.bar(null_summary.index, null_summary["Null Count"], color="orange")
    ax1.set_title("Missing Values per Column", fontsize=16)
    ax1.set_ylabel("Count")
    ax1.tick_params(axis="x", rotation=22)

    # 3. Numeric describe (bottom row, span both columns)
    ax2 = fig.add_subplot(gs[1, :])
    describe_stats.plot(kind="bar", ax=ax2, width=0.8)
    ax2.set_title("Numeric Columns - Summary Statistics", fontsize=16)
    ax2.set_ylabel("Value")
    ax2.legend(title="Statistic")
    ax2.tick_params(axis="x", rotation=22)

    plt.tight_layout()
    plt.show()


def overview(df, title="DATA OVERVIEW"):
    print(f"\n--- {title} ---")
    print(f"\n- Data shape: {df.shape}")
    print(f"\n- Data columns:\n{df.columns}")
    print(f"\n- Data types:\n{df.dtypes}")
    print(f"\n- Data info:")
    print(df.info())
    print(f"\n- Data describe:\n{df.describe()}")

    null_counts = df.isnull().sum()
    null_percentage = (null_counts / len(df)) * 100
    null_summary = df.isnull().sum().to_frame(name="Null Count")
    null_summary["Null %"] = null_percentage
    print(f"\n- Missing values per column:\n{null_summary}")

    visualization(df, title)
