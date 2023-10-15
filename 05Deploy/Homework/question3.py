import pickle
import os

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

customer = {"job": "retired", "duration": 445, "poutcome": "success"}
pred = single_pred(customer, dv, model)

print('prediction: %.3f' % pred)
if pred >= 0.5:
    print('Get Credit: High')
else:
    print('Get Credit: Low')
