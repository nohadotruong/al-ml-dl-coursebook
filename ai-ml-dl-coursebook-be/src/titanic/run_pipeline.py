import os
import pandas as pd
from src.titanic.preprocessing import preprocess_titanic
from src.titanic.config import DATA_RAW, DATA_PROCESSED


def run_pipeline(data_raw=DATA_RAW, data_processed=DATA_PROCESSED):
    """Load raw data, preprocess, and save processed CSV."""
    # Load raw CSV
    df_raw = pd.read_csv(data_raw)

    # Preprocess
    df_processed = preprocess_titanic(df_raw)

    # Make sure output folder exists
    os.makedirs(os.path.dirname(data_processed), exist_ok=True)

    # Save processed CSV
    df_processed.to_csv(data_processed, index=False)

    print("Preprocessing complete. Processed file saved at:", data_processed)


if __name__ == "__main__":
    run_pipeline()
