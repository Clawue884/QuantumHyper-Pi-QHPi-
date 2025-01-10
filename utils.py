import pandas as pd
import numpy as np

# Normalize data
def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

# Denormalize data
def denormalize_data(normalized_data, original_data):
    return normalized_data * (np.max(original_data) - np.min(original_data)) + np.min(original_data)

# Load and preprocess dataset
def preprocess_dataset(file_path):
    data = pd.read_csv(file_path)
    data['price'] = normalize_data(data['price'])
    return data

if __name__ == "__main__":
    processed_data = preprocess_dataset("data/price_data.csv")
    print(processed_data.head())


---
