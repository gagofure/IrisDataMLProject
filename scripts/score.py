import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report
import argparse

def score_model(model_path, X_test_path, y_test_path):
    # Load model
    model = joblib.load(model_path)
    
    # Load test data
    X_test = pd.read_csv(X_test_path).values
    y_test = pd.read_csv(y_test_path).values.ravel()
    
    # Predict
    predictions = model.predict(X_test)
    
    # Evaluate
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    
    print(f"Model Accuracy: {accuracy:.4f}")
    print("Classification Report:")
    print(report)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-path', type=str, required=True, help='Path to the trained model')
    parser.add_argument('--X-test-path', type=str, required=True, help='Path to the test features')
    parser.add_argument('--y-test-path', type=str, required=True, help='Path to the test labels')
    args = parser.parse_args()
    
    score_model(args.model_path, args.X_test_path, args.y_test_path)
