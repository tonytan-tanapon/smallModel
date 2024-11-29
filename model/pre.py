from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# Sample data
X_train = ["I love this!", "This is amazing", "I hate this!", "Terrible experience"]
y_train = [1, 1, 0, 0]  # 1 = Positive, 0 = Negative

# Create a simple pipeline
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", LogisticRegression())
])

# Train the model
model.fit(X_train, y_train)

# Save the model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "./model/model.pkl")
