import joblib
import numpy as np

# Load model and metadata
model_data = joblib.load('career_recommendation/career_model.pkl')
clf = model_data['model']
all_skills = model_data['Skills']
all_interests = model_data['Interests']
qualification_map = model_data['qualification_map']

def predict_career(age, qualification, selected_skills, selected_interests, top_n=3):
    # Encode qualification
    qualification_num = qualification_map.get(qualification, 0) if isinstance(qualification, str) else qualification

    # One-hot encode skills and interests
    skill_vector = [1 if skill in selected_skills else 0 for skill in all_skills]
    interest_vector = [1 if interest in selected_interests else 0 for interest in all_interests]

    # Build feature vector
    features = [age, qualification_num] + skill_vector + interest_vector
    features = np.array(features).reshape(1, -1)

    # Predict probabilities
    probs = clf.predict_proba(features)[0]
    classes = clf.classes_
    top_indices = np.argsort(probs)[::-1][:top_n]
    top_careers = [(classes[i], probs[i]) for i in top_indices]
    return top_careers
