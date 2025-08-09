# train_dummy_model.py
import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from feature_extractor import extract_features

# create dummy dataset
X = []
y = []
# create some legit samples
legit_urls = [
    "https://google.com", "https://github.com", "https://wikipedia.org"
]
phish_urls = [
    "http://login-paypal.com", "http://123.45.67.89/secure", "http://secure-login-google.com@evil.com"
]

for u in legit_urls:
    X.append(extract_features(u))
    y.append(0)
for u in phish_urls:
    X.append(extract_features(u))
    y.append(1)

X = np.array(X)
y = np.array(y)

clf = RandomForestClassifier(n_estimators=50, random_state=42)
clf.fit(X, y)

joblib.dump(clf, 'model.pkl')
print("Saved model.pkl")
