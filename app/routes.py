from flask import Blueprint, request, jsonify
import pandas as pd
from .model import load_model
from .preprocess import preprocess_data

routes = Blueprint('routes', __name__)
model = load_model()

@routes.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = pd.DataFrame([data['features']])
    features, _ = preprocess_data(features)
    prediction = model.predict(features)
    return jsonify({'fraud': bool(prediction[0])})