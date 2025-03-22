import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(data, scaler=None):
    data = data.drop(['Time'], axis=1, errors='ignore')

    if scaler is None:
        scaler = StandardScaler()
        data = scaler.fit_transform(data)
    else:
        data = scaler.transform(data)

    return data, scaler