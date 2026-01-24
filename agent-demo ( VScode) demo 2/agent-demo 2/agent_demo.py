# agent_demo.py
import requests
import joblib
import numpy as np
import time
import json
import os
import shap
import matplotlib.pyplot as plt

MODEL_PATH = "vertex_model.pkl"
API_URL = "http://127.0.0.1:5000/data"

def fetch_data(api_url=API_URL, timeout=5):
    resp = requests.get(api_url, timeout=timeout)
    resp.raise_for_status()
    return resp.json()

def load_model(path=MODEL_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found: {path}")
    model = joblib.load(path)
    return model

def model_predict(model, features_dict):
    X = np.array([[features_dict["f1"], features_dict["f2"], features_dict["f3"]]])
    pred_prob = model.predict_proba(X)[0, 1] if hasattr(model, "predict_proba") else None
    pred_label = int(model.predict(X)[0])
    return pred_label, float(pred_prob) if pred_prob is not None else None, X

def explain_with_shap(model, X):
    explainer = shap.Explainer(model)
    shap_values = explainer(X)
    return shap_values

def execute_action(pred_label, payload):
    if pred_label == 1:
        action = f"Action: SEND EMAIL to user@example.com. Reason value={payload['value']:.2f}"
    else:
        action = f"Action: UPDATE CRM record id=1234. Reason value={payload['value']:.2f}"
    print(action)
    return action

def main(loop=3, pause=3):
    print("Starting live agent demo. Fetching model and then data from mock API.")
    model = load_model()
    for i in range(loop):
        print(f"\nIteration {i+1}/{loop}: fetching data")
        payload = fetch_data()
        print("Payload:", json.dumps(payload, indent=2))

        pred_label, pred_prob, X = model_predict(model, payload["features"])
        print(f"Model prediction: {pred_label}  probability: {pred_prob}")

        print("Generating SHAP explanation")
        shap_values = explain_with_shap(model, X)
        try:
            shap.plots.waterfall(shap_values[0])
            plt.suptitle(f"SHAP explanation iter {i+1}")
            plt.show(block=False)
            print("Showing SHAP waterfall plot. Close plot window to continue the demo or wait 2 seconds.")
            time.sleep(2)
            plt.close()
        except Exception as e:
            print("Could not render SHAP plot in this environment:", e)

        action = execute_action(pred_label, payload)

        audit_record = {
            "timestamp": payload["timestamp"],
            "features": payload["features"],
            "prediction": pred_label,
            "prediction_prob": pred_prob,
            "action": action
        }
        print("Audit record:", json.dumps(audit_record, indent=2))
        time.sleep(pause)

    print("Demo finished")

if __name__ == "__main__":
    main(loop=5, pause=2)
