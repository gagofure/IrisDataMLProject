import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

def test_model(model_path):
    # Load the model
    model = joblib.load(model_path)
    
    # Load the Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Predict
    predictions = model.predict(X)
    
    # Check accuracy
    accuracy = accuracy_score(y, predictions)
    print(f"Model Accuracy: {accuracy:.4f}")
    
    # Define an acceptable accuracy threshold
    acceptable_accuracy = 0.90
    
    if accuracy < acceptable_accuracy:
        raise ValueError(f"Model accuracy of {accuracy:.4f} is below acceptable threshold of {acceptable_accuracy:.4f}")

if __name__ == "__main__":
    test_model('model.pkl')
