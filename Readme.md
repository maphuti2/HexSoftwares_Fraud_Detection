# Fraud Dectection

# Credit Card Fraud Detection API

This project is a Flask-based application designed for detecting credit card fraud. It uses a machine learning model to predict whether a transaction is fraudulent based on transaction features. The system includes data preprocessing, model training, and a RESTful API for predictions.

---

## Project Structure

- **app/**:
  - **preprocess.py**: Prepares and scales the input data for the machine learning model by removing unnecessary features and applying scaling.
  - **model.py**: Contains functions for training and saving the machine learning model, as well as loading the trained model.
  - ****init**.py**: Initializes the Flask application and registers API routes.
  - **routes.py**: Defines the RESTful API endpoint for handling prediction requests.
- **train.py**: Script to load data, preprocess it, and train the model.
- **main.py**: Entry point for starting the Flask application.
- **data/**: Directory for storing the input dataset (e.g., `sample_creditcard.csv`).
- **model.pkl**: Saved trained machine learning model.

---

## Setup Instructions

### Prerequisites

1. Ensure Python (>=3.8) is installed on your system.
2. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```
