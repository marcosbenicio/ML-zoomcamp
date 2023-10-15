import pickle
import os
from flask import Flask, request, jsonify

# request: To get the content of a POST request
# jsonsify: To respond with JSON (dictionary)

# Preditiction for a single customer
def single_pred(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]


# Paths
filepath_dv = 'dv.bin'
filepath_model = 'model1.bin'

# Load dictionary vectorizer
if os.path.exists(filepath_dv):
    with open(filepath_dv, 'rb') as f_dv:
        dv = pickle.load(f_dv)
else:
    print(f"File {filepath_dv} not found.")

# Load model
if os.path.exists(filepath_model):
    with open(filepath_model, 'rb') as f_model:
        model = pickle.load(f_model)
else:
    print(f"File {filepath_model} not found.")

app = Flask('churn')
# Registers the /predict route, and assigns it to the predict function
@app.route('/predict', methods=['POST'])
def predict():
    customer =  request.get_json()
    pred = single_pred(customer, dv, model)
    result = {'Credit probability': float(pred)}
    return jsonify(result)

if __name__ == '__main__':
    #To test it, open the browser and type 'localhost:9696/predict'
    app.run(debug=True, host='0.0.0.0', port=9696)