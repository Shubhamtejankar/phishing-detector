import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
from feature_extraction import extract_features

# Create model folder
if not os.path.exists("model"):
    os.makedirs("model")

# Load dataset
data = pd.read_csv("dataset.csv")

# Extract features
X = data['url'].apply(extract_features).tolist()
y = data['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model/model.pkl")

print("Model trained and saved!")