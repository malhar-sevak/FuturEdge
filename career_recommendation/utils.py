import pandas as pd
def encode_skills(selected_skills):
    """
    Encode selected skills as a binary vector matching the order of all unique skills in the dataset.
    Returns a list of 0/1.
    """
    df = pd.read_csv('career_recommendation/AI-based Career Recommendation System.csv')
    all_skills = sorted(df['Skills'].dropna().unique())
    return [1 if skill in selected_skills else 0 for skill in all_skills]

def encode_interests(selected_interests):
    """
    Encode selected interests as a binary vector matching the order of all unique interests in the dataset.
    Returns a list of 0/1.
    """
    df = pd.read_csv('career_recommendation/AI-based Career Recommendation System.csv')
    all_interests = sorted(df['Interests'].dropna().unique())
    return [1 if interest in selected_interests else 0 for interest in all_interests]

# def get_csv_path():
#     return os.path.join(settings.BASE_DIR, 'career_recommendation', 'AI-based Career Recommendation System.csv')

def get_skill_choices():
    df = pd.read_csv('career_recommendation/AI-based Career Recommendation System.csv')
    unique_skills = sorted(df['Skills'].dropna().unique())
    return [(Skills, Skills) for Skills in unique_skills]

def get_interest_choices():
    df = pd.read_csv('career_recommendation/AI-based Career Recommendation System.csv')
    unique_interests = sorted(df['Interests'].dropna().unique())
    return [(Interests, Interests) for Interests in unique_interests]
