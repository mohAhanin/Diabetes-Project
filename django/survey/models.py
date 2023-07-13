from cgitb import reset
from django.db import models
import pandas as pd
from django.contrib.auth.models import User


# Create your models here.

class SurveyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Pregnancies = models.IntegerField()
    Glucose = models.IntegerField()
    BloodPressure = models.IntegerField()
    Insulin = models.IntegerField()
    DiabetesPedigreeFunction = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField() 
    Age = models.IntegerField()
    result = models.BooleanField(default=False)

    def BMI(self):
        return self.weight // (self.height * self.height)

    def ConvertToDataFrame():
        Info = SurveyInfo.objects.all().values()
        df = pd.DataFrame.from_records(Info)
        return df

    def __str__(self):
        return str(self.user.username)