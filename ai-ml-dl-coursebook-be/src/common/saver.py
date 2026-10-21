import os, pickle


def save_models(results, folder_path="models/"):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for model_name, res in results.items():
        model = res["model"]
        file_path = os.path.join(folder_path, f"{model_name}.pkl")
        with open(file_path, "wb") as f:
            pickle.dump(model, f)
        print(f"Saved {model_name} model to {file_path}")
