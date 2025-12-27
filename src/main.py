import argparse
import os
import sys

# Add the parent directory to sys.path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.model import PhishingDetector

def main():
    parser = argparse.ArgumentParser(description="AI Phishing Detection System")
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Train command
    train_parser = subparsers.add_parser('train', help='Train the model')
    train_parser.add_argument('--data', required=True, help='Path to dataset CSV')
    train_parser.add_argument('--model-out', default='model.pkl', help='Path to save trained model')
    
    # Predict command
    predict_parser = subparsers.add_parser('predict', help='Predict if a URL is phishing')
    predict_parser.add_argument('--url', required=True, help='URL to analyze')
    predict_parser.add_argument('--model-in', default='model.pkl', help='Path to load trained model')
    
    args = parser.parse_args()
    
    detector = PhishingDetector()
    
    if args.command == 'train':
        detector.train(args.data)
        detector.save_model(args.model_out)
        
    elif args.command == 'predict':
        if os.path.exists(args.model_in):
            detector.load_model(args.model_in)
            result = detector.predict(args.url)
            print(f"Prediction for {args.url}: {result}")
        else:
            print(f"Error: Model file {args.model_in} not found. Train the model first.")
            
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
