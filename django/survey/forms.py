from django import forms
from .models import SurveyInfo

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyInfo
        fields = ['pregnancies','glucose','bloodPressure','insulin',
        'diabetesPedigreeFunction','weight','height','Age',]
        labels = {
            'pregnancies': '  تعداد بارداری  ',
            'glucose': 'گلوکز',
            'bloodPressure': 'فشار خون',
            'skinThickness': 'ضخامت پوست',
            'insulin': 'انسولین',
            'diabetesPedigreeFunction': 'تاریخچه ی دیابت',
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