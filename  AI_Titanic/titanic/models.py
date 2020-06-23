from django.db import models
import joblib
import numpy as np
# from sklearn.externals import joblib

def predict(input_data):
    model = joblib.load('./titanic/Classification/titanic.pkl')
    input_data = np.array(input_data)
    answer = model.predict(input_data)
    return answer
