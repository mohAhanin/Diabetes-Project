from django.urls import path
from .views import *

urlpatterns = [
    path('survey/', surveyView, name='survey'),
    path('', landing, name='landing'),
]