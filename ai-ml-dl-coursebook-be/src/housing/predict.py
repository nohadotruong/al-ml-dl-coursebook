import os, pickle
import pandas as pd


def housing_predict(data_new, model_folder="models/"):
    print("\n=== PREDICT VALUE ===\n")

    if not isinstance(data_new, dict):
        print("\n=== PREDICT VALUE FAILED ===\n")
        raise ValueError("data_new phải là dict với key là tên cột, value là giá trị")

    example_model_path = os.path.join(model_folder, os.listdir(model_folder)[0])
    with open(example_model_path, "rb") as f:
        example_model = pickle.load(f)

    preprocess = example_model.named_steps["prep"]
    num_cols = preprocess.transformers_[0][2]
    cat_cols = preprocess.transformers_[1][2]
    all_cols = num_cols + cat_cols

    missing_cols = [col for col in all_cols if col not in data_new]
    if missing_cols:
        print("\n=== PREDICT VALUE FAILED ===\n")
        raise ValueError(f"Thiếu giá trị cho các cột: {missing_cols}")

    df_new = pd.DataFrame([data_new], columns=all_cols)

    predictions = {}
    for file_name in os.listdir(model_folder):
        if file_name.endswith(".pkl"):
            model_name = file_name.replace(".pkl", "")
            model_path = os.path.join(model_folder, file_name)
            with open(model_path, "rb") as f:
                model = pickle.load(f)
            pred = model.predict(df_new)
            predictions[model_name] = round(pred[0], 2)
            print(f"{model_name} predicts: {round(pred[0], 2)}")

    print("\n=== PREDICT VALUE SUCCESSFULLY ===\n")

    return predictions
