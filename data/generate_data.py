import pandas as pd
import random

def generate_dummy_data(output_path):
    print(f"Generating dummy data to {output_path}...")
    
    legitimate_urls = [
        "https://www.google.com", "https://www.youtube.com", "https://www.facebook.com",
        "https://www.amazon.com", "https://www.wikipedia.org", "https://www.twitter.com",
        "https://www.instagram.com", "https://www.linkedin.com", "https://www.reddit.com",
        "https://www.netflix.com", "https://www.microsoft.com", "https://www.apple.com",
        "https://stackoverflow.com", "https://github.com", "https://medium.com",
        "https://www.nytimes.com", "https://www.cnn.com", "https://www.bbc.com",
        "https://www.weather.com", "https://www.paypal.com"
    ]
    
    phishing_urls = [
        "http://secure-login-paypal.com.account-update.info",
        "http://verify-your-account-apple.com.security-check.net",
        "http://google-drive-shared-file.com.login-required.xyz",
        "http://amazon-order-confirmation.com.track-your-package.biz",
        "http://facebook-security-alert.com.verify-identity.org",
        "http://bank-of-america-login.com.secure-banking.net",
        "http://netflix-payment-update.com.account-hold.info",
        "http://instagram-verified-badge.com.apply-now.xyz",
        "http://linkedin-job-offer.com.view-details.biz",
        "http://microsoft-support.com.fix-your-pc.net",
        "http://192.168.1.1/login.html",
        "http://account-update-required.com/login",
        "http://verify-identity-now.com/secure",
        "http://win-iphone-free.com/claim",
        "http://urgent-action-required.com/verify"
    ]
    
    data = []
    
    # Add legitimate URLs (label 0)
    for url in legitimate_urls:
        data.append({'url': url, 'label': 0})
        
    # Add phishing URLs (label 1)
    for url in phishing_urls:
        data.append({'url': url, 'label': 1})
        
    # Generate some variations to increase dataset size slightly
    for i in range(50):
        if i % 2 == 0:
            base = random.choice(legitimate_urls)
            data.append({'url': base + f"/page{i}", 'label': 0})
        else:
            base = random.choice(phishing_urls)
            data.append({'url': base + f"?id={i}", 'label': 1})
            
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} samples.")

if __name__ == "__main__":
    generate_dummy_data("d:/coding/phishing_detection/data/dataset.csv")
