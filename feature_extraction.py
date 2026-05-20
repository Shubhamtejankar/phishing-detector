import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    parsed = urlparse(url)

    # Length of URL
    features.append(len(url))

    # Number of dots
    features.append(url.count('.'))

    # Has IP address
    features.append(1 if re.match(r"\d+\.\d+\.\d+\.\d+", parsed.netloc) else 0)

    # Has HTTPS
    features.append(1 if parsed.scheme == "https" else 0)

    # Suspicious words
    suspicious_words = ['login', 'verify', 'secure', 'bank', 'account', 'update']
    features.append(1 if any(word in url.lower() for word in suspicious_words) else 0)

    return features