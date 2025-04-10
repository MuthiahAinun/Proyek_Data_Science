import pandas as pd
import joblib
import json
import numpy as np

# Load files
pipeline = joblib.load("pipeline.pkl")
model = joblib.load("xgboost_model.pkl")
with open("optimal_treshold.json", "r") as f:
    threshold = json.load(f)["optimal_threshold"]

# Load employee data
df = pd.read_csv("employee_data.csv")
X = df.drop(columns=["Attrition"], errors='ignore')  # jika ada target, drop dulu

# Preprocess
X_processed = pipeline.transform(X)

# Predict
y_proba = model.predict_proba(X_processed)[:, 1]
y_pred = (y_proba >= threshold).astype(int)

# Tambahkan ke DataFrame
df["Attrition_Predicted"] = y_pred
df["Probability"] = y_proba

# Simpan ke CSV
df.to_csv("predictions.csv", index=False)
print("File predictions.csv berhasil dibuat.")
