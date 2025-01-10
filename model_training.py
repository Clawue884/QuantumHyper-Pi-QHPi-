import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import numpy as np
import pandas as pd

# Load dataset
def load_data(file_path, sequence_length=50):
    data = pd.read_csv(file_path)
    prices = data['price'].values
    X, y = [], []
    for i in range(len(prices) - sequence_length):
        X.append(prices[i:i+sequence_length])
        y.append(prices[i+sequence_length])
    return np.array(X), np.array(y)

# Build LSTM model
def build_model(input_shape):
    model = Sequential([
        LSTM(128, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(64),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# Training process
def train_model(data_path, model_save_path):
    X, y = load_data(data_path)
    X = X.reshape((X.shape[0], X.shape[1], 1))  # Reshape for LSTM

    model = build_model((X.shape[1], 1))
    model.fit(X, y, epochs=50, batch_size=32, validation_split=0.2)
    model.save(model_save_path)
    print(f"Model saved to {model_save_path}")

if __name__ == "__main__":
    train_model("data/price_data.csv", "models/price_predictor.h5")


---
