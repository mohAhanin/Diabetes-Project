from django import forms
from .models import SurveyInfo

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyInfo
        fields = ['Pregnancies','Glucose','BloodPressure','Insulin',
        'DiabetesPedigreeFunction','weight','height','Age',]
        labels = {
            'Pregnancies': '  تعداد بارداری  ',
            'Glucose': 'گلوکز',
            'BloodPressure': 'فشار خون',
            'Insulin': 'انسولین',
            'DiabetesPedigreeFunction': 'تاریخچه ی دیابت',
            'weight': 'وزن',
            'height': 'قد',
            'Age': 'سن'
        }
    def save(self, commit=True):
        instance = super(SurveyForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance