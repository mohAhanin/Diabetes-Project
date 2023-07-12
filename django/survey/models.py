from django.db import models
import pandas as pd

# Create your models here.

class SurveyInfo(models.Model):
    pregnancies = models.IntegerField()
    glucose = models.IntegerField()
    bloodPressure = models.IntegerField()
    skinThickness = models.IntegerField()
    insulin = models.IntegerField()
    diabetesPedigreeFunction = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField() 
    Age = models.IntegerField()

    def BMI(self):
        return self.weight // (self.height * self.height)

    def ConvertToDataFrame():
        Info = SurveyInfo.objects.all().values()
        df = pd.DataFrame.from_records(Info)
        return df
