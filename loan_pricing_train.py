import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the dataset
data = pd.read_csv("loan_pricing_data.csv")

# Define features and target
features = ["Country", "Company", "BaseRate", "Inflation", "GDP", "RegulationScore", "LoanAmount", "LoanTerm"]
target = "LoanRate"

X = data[features]
y = data[target]

# Preprocessing
categorical_features = ["Country", "Company"]
numerical_features = ["BaseRate", "Inflation", "GDP", "RegulationScore", "LoanAmount", "LoanTerm"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", StandardScaler(), numerical_features)
    ])

# Create pipeline with preprocessing and model
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "loan_pricing_model.pkl")

print("Model successfully trained and saved to loan_pricing_model.pkl")