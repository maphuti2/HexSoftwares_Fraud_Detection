import pandas as pd
from sklearn.model_selection import train_test_split
from app.preprocess import preprocess_data
from app.model import train_model


data = pd.read_csv('data/sample_creditcard.csv')
X = data.drop(['Class'], axis=1)
y = data['Class']


X, scaler = preprocess_data(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
train_model(X_train, y_train)