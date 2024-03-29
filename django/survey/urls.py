from django.urls import path
from .views import *


app_name = "survey"

urlpatterns = [
    path('survey/', surveyView, name='surveyView'),
    path('', landing, name='landing'),
    path('aboutUs/', aboutUsView, name='aboutUsView'),
    path('prediction/', predictionView, name='prediction'),
    path('Loadfile/', Loadfile, name='Loadfile'),
    path('OrderingDataForTraining/', OrderingDataForTraining, name='OrderingDataForTraining'),
]