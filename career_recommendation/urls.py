from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('career_recommendation/', views.recommend_view, name='career_recommendation'),
    path('career_history/', views.career_history, name='career_history'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/', views.courses_view, name='courses'),
    path('contact/', views.contact_us, name='contact'),
]