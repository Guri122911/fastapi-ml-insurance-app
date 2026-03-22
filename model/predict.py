import os
import pickle
import pandas as pd

# load model (correct way)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")

with open(model_path, 'rb') as f:
    model = pickle.load(f)

Model_version = "1.0.1.1"

# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    # Predict the class
    predicted_class = model.predict(df)[0]

    # Get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    
    # Create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }