from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Hello, CI/CD Pipeline is working!'}), 200


@app.route('/predict', methods=['POST'])
def predict():
    # Dummy response for ML model prediction (to be replaced with actual model)
    return jsonify({'prediction': 'Sample Prediction'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
