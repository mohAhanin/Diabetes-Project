from django.contrib import admin
from .models import SurveyInfo

class SurveyInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'Pregnancies', 'result', 'isTrain', 'isTest')
    list_filter = ('isTrain', 'isTest')

admin.site.register(SurveyInfo, SurveyInfoAdmin)