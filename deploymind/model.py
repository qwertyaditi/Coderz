import joblib

# Load the trained model
model = joblib.load("model.pkl")

def predict_risk(input_data):
    risk_score = model.predict_proba([input_data])[0][1]
    return risk_score