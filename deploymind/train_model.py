import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load CSV and clean header names
df = pd.read_csv("deploy_data.csv", encoding="utf-8-sig")
df.columns = df.columns.str.strip()  # Remove extra spaces

# ✅ Debug: Print the column names to see what's wrong
print("🔍 CSV Columns Found:", df.columns.tolist())

# Continue with training
X = df.drop(columns=["failed"])
y = df["failed"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")
