from src.housing.run_pipeline import run_pipeline as housing_pipeline
from src.housing.config import (
    RAW_FILE as HOUSING_RAW,
    PROCESSED_DIR as HOUSING_PROCESSED,
)


def run_housing_pipeline(data_raw=HOUSING_RAW, data_processed_dir=HOUSING_PROCESSED):
    return housing_pipeline(data_raw, data_processed_dir)


def main():
    run_housing_pipeline(HOUSING_RAW, HOUSING_PROCESSED)


if __name__ == "__main__":
    main()
