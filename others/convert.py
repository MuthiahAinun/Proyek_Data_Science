import pandas as pd
import sqlite3

df_pred = pd.read_csv("predictions.csv")
df_feat = pd.read_csv("top_10_feature_importance.csv")

conn = sqlite3.connect("predicted_resign.db")
df_pred.to_sql("predictions", conn, if_exists="replace", index=False)
df_feat.to_sql("feature_importance", conn, if_exists="replace", index=False)
conn.close()
