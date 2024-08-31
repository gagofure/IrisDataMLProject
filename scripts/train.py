import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import argparse

def train_model(input_dir, output_path):
    # Load preprocessed data
    X_train = pd.read_csv(f'{input_dir}/X_train.csv').values
    y_train = pd.read_csv(f'{input_dir}/y_train.csv').values.ravel()
    
    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Save model
    joblib.dump(model, output_path)
    print(f"Model saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', type=str, required=True, help='Directory containing preprocessed data')
    parser.add_argument('--output-path', type=str, required=True, help='Path to save the trained model')
    args = parser.parse_args()
    
    train_model(args.input_dir, args.output_path)
