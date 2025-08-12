import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Load data
csv_path = 'career_recommendation/AI-based Career Recommendation System.csv'
df = pd.read_csv(csv_path)
df = df.fillna('')

# Encode qualification
qualification_map = {'Bachelors': 0, 'Masters': 1, 'PhD': 2}
df['Qualification'] = df['Qualification'].map(qualification_map)

# Get all unique skills and interests
all_skills = sorted(set(skill for skills in df['Skills'] for skill in str(skills).split(';')))
all_interests = sorted(set(interest for interests in df['Interests'] for interest in str(interests).split(';')))

# One-hot encode skills and interests
for skill in all_skills:
    df[f'skill_{skill}'] = df['Skills'].apply(lambda x: int(skill in str(x).split(';')))
for interest in all_interests:
    df[f'interest_{interest}'] = df['Interests'].apply(lambda x: int(interest in str(x).split(';')))

# Features and target
feature_cols = ['Age', 'Qualification'] + [f'skill_{s}' for s in all_skills] + [f'interest_{i}' for i in all_interests]
X = df[feature_cols]
y = df['Career']  # Assuming 'Career' is the target column

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save model and feature info
joblib.dump({'model': clf, 'skills': all_skills, 'interests': all_interests, 'qualification_map': qualification_map}, 'career_recommendation/career_model.pkl')

print('Model trained and saved!')


# Define file paths (relative)
CSV_PATH = 'career_recommendation/AI-based Career Recommendation System.csv'
MODEL_PATH = 'career_recommendation/career_model.pkl'

# Load dataset
df = pd.read_csv(CSV_PATH)

# Clean and preprocess
df = df.dropna(subset=['Education', 'Skills', 'Interests', 'Recommended_Career'])
df['Skills'] = df['Skills'].apply(lambda x: x.split(','))
df['Interests'] = df['Interests'].apply(lambda x: x.split(','))

X = df[['Education', 'Skills', 'Interests']]
y = df['Recommended_Career']

# Encode features
education_encoder = OneHotEncoder(handle_unknown='ignore')
X_education = education_encoder.fit_transform(X[['Education']]).toarray()

skill_binarizer = MultiLabelBinarizer()
X_skills = skill_binarizer.fit_transform(X['Skills'])

interest_binarizer = MultiLabelBinarizer()
X_interests = interest_binarizer.fit_transform(X['Interests'])

# Combine features
X_processed = np.hstack((X_education, X_skills, X_interests))

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.3, random_state=15)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=15)
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump({
    'model': model,
    'education_encoder': education_encoder,
    'skill_binarizer': skill_binarizer,
    'interest_binarizer': interest_binarizer
}, MODEL_PATH)

print("✅ Model trained and saved at:", MODEL_PATH)
