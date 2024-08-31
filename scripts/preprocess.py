import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import argparse
import os

def preprocess_data(output_dir):
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scaling features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Save preprocessed data
    os.makedirs(output_dir, exist_ok=True)
    pd.DataFrame(X_train_scaled, columns=iris.feature_names).to_csv(os.path.join(output_dir, 'X_train.csv'), index=False)
    pd.DataFrame(X_test_scaled, columns=iris.feature_names).to_csv(os.path.join(output_dir, 'X_test.csv'), index=False)
    pd.DataFrame(y_train, columns=['species']).to_csv(os.path.join(output_dir, 'y_train.csv'), index=False)
    pd.DataFrame(y_test, columns=['species']).to_csv(os.path.join(output_dir, 'y_test.csv'), index=False)

    print(f"Preprocessed data saved to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=str, required=True, help='Directory to save the preprocessed data')
    args = parser.parse_args()
    
    preprocess_data(args.output_dir)
