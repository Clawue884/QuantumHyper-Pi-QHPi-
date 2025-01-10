import tensorflow as tf
import numpy as np

# Load model and predict
def predict_price(model_path, recent_prices):
    model = tf.keras.models.load_model(model_path)
    recent_prices = np.array(recent_prices).reshape((1, len(recent_prices), 1))  # Reshape for LSTM
    prediction = model.predict(recent_prices)
    return prediction[0][0]

if __name__ == "__main__":
    recent_prices = [314.1, 314.15, 314.16, 314.17, 314.18]  # Example data
    prediction = predict_price("models/price_predictor.h5", recent_prices)
    print(f"Predicted price: ${prediction:.2f}")


---
