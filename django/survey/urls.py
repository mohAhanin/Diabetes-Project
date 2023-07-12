from django.urls import path
from .views import surveyView

urlpatterns = [
    path('', surveyView, name='survey'),
]