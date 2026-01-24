# train_model.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import accuracy_score
import joblib

def make_sample_dataset(n=2000, seed=42):
    rng = np.random.RandomState(seed)
    f1 = rng.normal(loc=50, scale=15, size=n)
    f2 = rng.normal(loc=0, scale=1, size=n)
    f3 = rng.randint(0, 10, size=n)
    noise = rng.normal(scale=10, size=n)
    y = ((f1 + noise) > 50).astype(int)
    df = pd.DataFrame({"f1": f1, "f2": f2, "f3": f3, "label": y})
    return df

def train_and_save():
    df = make_sample_dataset()
    X = df[["f1", "f2", "f3"]]
    y = df["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = xgb.XGBClassifier(n_estimators=100, max_depth=4, use_label_encoder=False, eval_metric="logloss")
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Trained XGBoost classifier. Test accuracy: {acc:.4f}")

    joblib.dump(model, "vertex_model.pkl")
    print("Saved model to vertex_model.pkl")

if __name__ == "__main__":
    train_and_save()
