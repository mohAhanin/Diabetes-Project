from django.shortcuts import render
from .forms import SurveyForm

def surveyView(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
        return render(request, 'survey/end.html', {'form': form})
    else:
        form = SurveyForm()
        return render(request, 'survey/survey.html', {'form': form})
    