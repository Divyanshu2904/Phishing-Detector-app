# feature_extractor.py
import re
from urllib.parse import urlparse
import socket

def extract_features(url):
    """
    Very simple feature extractor for demo:
    - url length
    - has_https (1/0)
    - count of dots in hostname
    - has_at_symbol (1/0)
    - domain_is_ip (1/0)
    Return a list of numeric features.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # normalize if user forgot http

    parsed = urlparse(url)
    hostname = parsed.hostname or ''
    features = []
    # feature 1: url length
    features.append(len(url))
    # feature 2: https presence
    features.append(1 if parsed.scheme == 'https' else 0)
    # feature 3: count of '.' in hostname
    features.append(hostname.count('.'))
    # feature 4: presence of @
    features.append(1 if '@' in url else 0)
    # feature 5: domain is IP
    is_ip = 0
    try:
        socket.inet_aton(hostname)
        is_ip = 1
    except Exception:
        is_ip = 0
    features.append(is_ip)

    # pad to fixed length (example 10) for model compatibility; replace with real features later
    while len(features) < 10:
        features.append(0)
    return features
