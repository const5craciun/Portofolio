from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Projects
    path('projects/', views.projects_index, name='projects'),
    path('projects/nlp/', views.nlp_topic_modeling, name='nlp_topic_modeling'),
    path('projects/ml/', views.ml_predictor, name='ml_predictor'),
]