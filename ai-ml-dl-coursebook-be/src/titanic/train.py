# src/titanic/train.py
import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.titanic.config import DATA_PROCESSED, MODEL_DIR


def train_models():
    # --- Load processed data ---
    df = pd.read_csv(DATA_PROCESSED)
    X = df.drop("Survived", axis=1)
    y = df["Survived"]

    # --- Split train/validation 80/20 ---
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # --- Define models ---
    models = {
        "Dummy": DummyClassifier(strategy="most_frequent"),
        "LogisticRegression": LogisticRegression(max_iter=2000, random_state=42),
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
    }

    results = {}
    best_f1 = -1
    best_model = None
    best_name = None

    os.makedirs(MODEL_DIR, exist_ok=True)

    # --- Train & Evaluate on validation ---
    for name, model in models.items():
        model.fit(X_train, y_train)

        # Validation metrics
        y_val_pred = model.predict(X_val)
        val_acc = accuracy_score(y_val, y_val_pred)
        val_prec = precision_score(y_val, y_val_pred, zero_division=0)
        val_rec = recall_score(y_val, y_val_pred, zero_division=0)
        val_f1 = f1_score(y_val, y_val_pred, zero_division=0)

        results[name] = {
            "val": {
                "Accuracy": val_acc,
                "Precision": val_prec,
                "Recall": val_rec,
                "F1": val_f1,
            }
        }

        print(f"--- {name} ---")
        print(
            f"Validation : Acc={val_acc:.4f}, Prec={val_prec:.4f}, Rec={val_rec:.4f}, F1={val_f1:.4f}\n"
        )

        # Save model
        joblib.dump(model, os.path.join(MODEL_DIR, f"{name}.pkl"))

        # Track best model (by F1 on validation)
        if val_f1 > best_f1:
            best_f1 = val_f1
            best_model = model
            best_name = name

    # Save best model
    if best_model is not None:
        joblib.dump(best_model, os.path.join(MODEL_DIR, "best_model.pkl"))
        print(f"Best model: {best_name} saved as best_model.pkl (F1={best_f1:.4f})\n")

    return results


if __name__ == "__main__":
    train_models()
