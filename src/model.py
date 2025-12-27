import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from .features import extract_features

class PhishingDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        
    def train(self, data_path):
        """
        Trains the model using data from the CSV file at data_path.
        Expected CSV columns: 'url', 'label' (0 for legitimate, 1 for phishing)
        """
        print(f"Loading data from {data_path}...")
        df = pd.read_csv(data_path)
        
        # Extract features
        print("Extracting features...")
        features_list = []
        for url in df['url']:
            features_list.append(extract_features(url))
            
        X = pd.DataFrame(features_list)
        y = df['label']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train
        print("Training model...")
        self.model.fit(X_train, y_train)
        
        # Evaluate
        print("Evaluating model...")
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.4f}")
        print(classification_report(y_test, y_pred))
        
    def predict(self, url):
        """
        Predicts whether a URL is phishing or legitimate.
        Returns: 'Phishing' or 'Legitimate'
        """
        features = extract_features(url)
        features_df = pd.DataFrame([features])
        prediction = self.model.predict(features_df)[0]
        return "Phishing" if prediction == 1 else "Legitimate"
        
    def save_model(self, path):
        joblib.dump(self.model, path)
        print(f"Model saved to {path}")
        
    def load_model(self, path):
        self.model = joblib.load(path)
        print(f"Model loaded from {path}")
