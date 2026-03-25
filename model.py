import pandas as pd
import os
import json
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor

# --- 1. RELOAD FRESH DATA (To fix numerical values issue) ---
df = pd.read_csv("data/data.csv")
df['Price Date'] = pd.to_datetime(df['Price Date'], errors='coerce')
df['Year'] = df['Price Date'].dt.year
df['Month'] = df['Price Date'].dt.month
df['Day'] = df['Price Date'].dt.day
df = df.dropna(subset=['Modal_Price']).drop('Price Date', axis=1)

# --- 2. ENCODE & CREATE MAPPING ---
label_encoders = {}
preprocessing_mapping = {}
text_columns = ['STATE', 'District Name', 'Market Name', 'Commodity', 'Variety', 'Grade']

for col in text_columns:
    le = LabelEncoder()
    df[col] = df[col].fillna('Unknown').astype(str)

    # Fit on original names
    le.fit(df[col])

    # Create the mapping { "Punjab": 0, "Haryana": 1 }
    mapping = {str(name): int(index) for index, name in enumerate(le.classes_)}
    preprocessing_mapping[col] = mapping

    # Transform the dataframe
    df[col] = le.transform(df[col])
    label_encoders[col] = le

# Save the Human-Readable JSON immediately
if not os.path.exists('artifacts'): os.makedirs('artifacts')
with open('artifacts/preprocessing.json', 'w') as f:
    json.dump(preprocessing_mapping, f, indent=4)
print("JSON saved with actual names!")

# --- 3. GRID SEARCH (Replacing Optuna for stability) ---
X = df[['STATE', 'District Name', 'Market Name', 'Commodity', 'Variety', 'Grade', 'Year', 'Month', 'Day']].fillna(0)
y = df['Modal_Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# We use restricted parameters to ensure the model stays under 200MB
param_grid = {
    'n_estimators': [100],
    'max_depth': [15, 20],
    'min_samples_leaf': [2, 5]
}

print("Running Grid Search...")
grid_search = GridSearchCV(RandomForestRegressor(random_state=42, n_jobs=-1), param_grid, cv=3)
grid_search.fit(X_train, y_train)

# --- 4. SAVE COMPRESSED LITE MODEL ---
best_model = grid_search.best_estimator_
joblib.dump(best_model, 'artifacts/market_price_model.pkl', compress=3)
print(f"✅ Model Saved! Final Params: {grid_search.best_params_}")


