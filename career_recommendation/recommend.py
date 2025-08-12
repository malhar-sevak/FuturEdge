
import joblib
import os
import numpy as np
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, 'career_recommendation', 'career_model.pkl')
model_data = joblib.load(MODEL_PATH)
model = model_data['model']
education_encoder = model_data['education_encoder']
skill_binarizer = model_data['skill_binarizer']
interest_binarizer = model_data['interest_binarizer']

def preprocess_input(education, skill, interest):
    # All inputs are single values (not lists)
    # Encode education
    X_education = education_encoder.transform([[education]]).toarray()
    # Encode skill and interest as lists for binarizer
    X_skills = skill_binarizer.transform([[skill]])
    X_interests = interest_binarizer.transform([[interest]])
    # Combine features
    X_processed = np.hstack((X_education, X_skills, X_interests))
    return X_processed

def recommend_career(education, skill, interest):
    X_processed = preprocess_input(education, skill, interest)
    probabilities = model.predict_proba(X_processed)[0]
    classes = model.classes_
    top_indices = np.argsort(probabilities)[::-1][:3]
    top_careers = [(classes[i], round(probabilities[i] * 100, 2)) for i in top_indices]
    return top_careers
