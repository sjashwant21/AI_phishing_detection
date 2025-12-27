import re
from urllib.parse import urlparse
import tldextract

def extract_features(url):
    """
    Extracts features from a URL for phishing detection.
    Returns a dictionary of features.
    """
    features = {}
    
    # 1. URL Length
    features['url_length'] = len(url)
    
    # 2. Domain Length
    extracted = tldextract.extract(url)
    domain = extracted.domain
    features['domain_length'] = len(domain)
    
    # 3. Count of special characters
    features['count_at'] = url.count('@')
    features['count_hyphen'] = url.count('-')
    features['count_dot'] = url.count('.')
    features['count_percent'] = url.count('%')
    features['count_question'] = url.count('?')
    features['count_equal'] = url.count('=')
    features['count_slash'] = url.count('/')
    
    # 4. HTTPS check
    parsed = urlparse(url)
    features['is_https'] = 1 if parsed.scheme == 'https' else 0
    
    # 5. IP Address in URL (Simple regex for IPv4)
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    features['has_ip'] = 1 if re.search(ip_pattern, url) else 0
    
    # 6. Suspicious keywords
    suspicious_keywords = ['login', 'verify', 'update', 'account', 'secure', 'banking', 'confirm']
    features['has_suspicious_keyword'] = 1 if any(keyword in url.lower() for keyword in suspicious_keywords) else 0
    
    # 7. Count of digits
    features['count_digits'] = sum(c.isdigit() for c in url)
    
    return features
