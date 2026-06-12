import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("Loading dataset...")

df = pd.read_csv("phishing_site_urls.csv")

# Example preprocessing
df = df.dropna()

df["Label"] = df["Label"].replace({
"good": 0,
"bad": 1
})

# Assuming dataset columns are URL and Label
df["url_length"] = df["URL"].apply(len)
df["dot_count"] = df["URL"].str.count(r"\.")
df["hyphen_count"] = df["URL"].str.count("-")

X = df[["url_length", "dot_count", "hyphen_count"]]
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")
print("Project completed successfully!")
