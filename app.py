# app.py
from flask import Flask, request, jsonify
import numpy as np
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Create a simple model on startup (for demonstration)
model = RandomForestClassifier(n_estimators=10)

# Train with toy data
model.fit(np.array([[0, 0], [0, 1], [1, 0], [1, 1]]), [0, 1, 1, 0])


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = data.get('features', [])
    
    # Convert to numpy array
    features_array = np.array(features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features_array).tolist()
    
    return jsonify({'prediction': prediction})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

