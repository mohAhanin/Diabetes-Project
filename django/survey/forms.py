from django import forms
from .models import SurveyInfo

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyInfo
        fields = '__all__'
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