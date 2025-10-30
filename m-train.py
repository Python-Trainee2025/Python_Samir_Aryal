# Import libraries
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Dummy dataset
texts = [
    "Win a free iPhone now!", "Your account has been suspended", "Meeting at 10am tomorrow",
    "Congratulations, you've won a lottery!", "Let's catch up over coffee", "Free entry in a contest",
    "Your invoice is attached", "You have been selected for a prize", "Lunch at 1?", "Urgent: Update your account"
]
labels = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # 1 = spam, 0 = not spam

# Split data
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.3, random_state=42)

# NLP + ML Pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', MultinomialNB())
])

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Inference
new_text = ["Claim your free vacation now!"]
prediction = model.predict(new_text)
print(f"Prediction for '{new_text[0]}':", "Spam" if prediction[0] == 1 else "Not Spam")