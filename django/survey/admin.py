from django.contrib import admin
from .models import SurveyInfo

class SurveyInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'Pregnancies', 'result', 'isTrain', 'isTest','isNotInput')
    list_filter = ('isTrain', 'isTest','isNotInput')

admin.site.register(SurveyInfo, SurveyInfoAdmin)