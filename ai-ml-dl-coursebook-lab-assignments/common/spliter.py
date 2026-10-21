from sklearn.model_selection import train_test_split


def split_data(X_raw, y_raw, val_ratio=0.2, test_ratio=0.1):
    X_temp, X_test, y_temp, y_test = train_test_split(
        X_raw, y_raw, test_size=test_ratio, random_state=42
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=val_ratio / (1 - test_ratio), random_state=42
    )
    return X_train, X_val, X_test, y_train, y_val, y_test
