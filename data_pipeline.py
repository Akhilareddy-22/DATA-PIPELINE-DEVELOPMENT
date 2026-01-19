import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Read the raw data
data = pd.read_csv("data.csv")

# 2. Remove duplicate rows
data = data.drop_duplicates()

# 3. Fill missing values
# Numeric columns → fill with mean
for col in data.select_dtypes(include=["int64", "float64"]).columns:
    data[col] = data[col].fillna(data[col].mean())

# Categorical columns → fill with most common value
for col in data.select_dtypes(include=["object"]).columns:
    data[col] = data[col].fillna(data[col].mode()[0])

# 4. Convert text columns into numbers
encoder = LabelEncoder()
for col in data.select_dtypes(include=["object"]).columns:
    data[col] = encoder.fit_transform(data[col])

# 5. Scale numeric columns
scaler = StandardScaler()
num_cols = data.select_dtypes(include=["int64", "float64"]).columns
data[num_cols] = scaler.fit_transform(data[num_cols])

# 6. Save the cleaned data
data.to_csv("cleaned_data.csv", index=False)

print("✅ Data pipeline completed successfully")
