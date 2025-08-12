from django import forms
from .utils import get_skill_choices, get_interest_choices

QUALIFICATION_CHOICES = [
    ('Bachelors', 'Bachelors'),
    ('Masters', 'Masters'),
    ('PhD', 'PhD'),
]

class CareerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    age = forms.IntegerField(label='Age', min_value=22)
    qualification = forms.ChoiceField(
        label='Qualification', 
        choices=QUALIFICATION_CHOICES,
        widget=forms.Select
    )
    skills = forms.ChoiceField(
        label='Skills',
        widget=forms.Select,
        choices=get_skill_choices()
    )
    interests = forms.ChoiceField(
        label='Interests',
        widget=forms.Select,
        choices=get_interest_choices()
    )
