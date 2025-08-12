
# FuturEdge: Career Path Recommendation System 


A Django-based web application that predicts the top career paths for a user based on their qualification, skills, and interests using Machine Learning (RandomForestClassifier).


## Tech Stack

**Frontend:** Html,CSS,Bootstrap

**Backend:** Django (Python)

**ML Model:** RandomForestClassifier (scikit-learn)

**Database:**  SQLite (default, can be switched to PostgreSQL/MySQL)






## Features

- User-friendly Interface – Collects name, age, qualification, skills, and interests via forms.
- Career Prediction – Returns top 3 career paths with recommendation scores.

- Machine Learning Model – Trained on a dataset of career data using RandomForestClassifier.

- Career History – Stores past recommendations in the database for future reference.

- Courses Page – Suggests relevant courses for each career.

- Admin Panel – Manage users, career history, and courses.

- Responsive UI – Works on desktop, tablet, and mobile.



## Run Locally

Clone the project

```bash
  git clone https://github.com/malhar-sevak/FuturEdge.git
```

Go to the project directory

```bash
  cd FuturEdge
```

Install dependencies

```bash
  pip install pillow //For image support
```

Start the server

```bash
  python manage.py runserver
```


## Documentation

[Django Framework](https://docs.djangoproject.com/en/5.2/)

[RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)


## FAQ

#### why is the recommendation score of too low in most of the career prediction?

As the CSV which is used to train the RandomForestClassifier model for the career prediction contains of many various skills and intrest, the overall accuracy of the model gets divided into several parts.Hence a particular field or tech cannot attain much accuracy. 



## Feedback

If you have any feedback, please reach out to me at malharsevak03@gmail.com

