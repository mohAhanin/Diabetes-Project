from operator import truediv
from xmlrpc.client import boolean
from django.shortcuts import render
from .forms import SurveyForm
from .loadFile import *
from django.shortcuts import render
from .models import SurveyInfo
from sklearn.neighbors import KNeighborsClassifier
from django.core.exceptions import ObjectDoesNotExist
#---------------------------------------------------------------
def surveyView(request):
    try:
        if request.user.survey is not None:
            return predictionView(request)
    except ObjectDoesNotExist:
        pass
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
        return render(request, 'survey/survey.html', {'form': form})
    else:
        form = SurveyForm()
        return render(request, 'survey/survey.html', {'form': form})
#---------------------------------------------------------------
def aboutUsView(request):
    return render(request, 'survey/aboutUs.html')
#---------------------------------------------------------------
def landing(request):
    return render(request, 'survey/landing.html')
#---------------------------------------------------------------
def Loadfile(request):
    save_csv_data_to_db("survey/Diabetes.csv.csv")
    return render(request, 'survey/landing.html')
#---------------------------------------------------------------  
def predictionView(request):
    userInfo = request.user.survey

    surveyInfo = SurveyInfo.objects.filter(isTrain = True)

    data = list(surveyInfo.values_list('Pregnancies', 'Glucose',
     'BloodPressure', 'Insulin', 'weight', 'DiabetesPedigreeFunction', 
     'Age','result'))

    new_data = []

    for tpl in data:
        new_tpl = []
        for item in tpl:
            if item == True:
                new_tpl.append(1)
            elif item == False:
                new_tpl.append(0)
            else:
                new_tpl.append(item)
        new_data.append(tuple(new_tpl))


    df = pd.DataFrame(data,columns=['Pregnancies', 'Glucose',
     'BloodPressure', 'Insulin', 'weight', 'DiabetesPedigreeFunction', 
     'Age','result'])

    x=df.drop(['result'],axis=1) 
    y=df['result']


    knn = KNeighborsClassifier(n_neighbors=36)
    knn.fit(x,y)


    p = knn.predict([[userInfo.Pregnancies, userInfo.Glucose, userInfo.BloodPressure,
    userInfo.Insulin, userInfo.BMI(), userInfo.DiabetesPedigreeFunction, userInfo.Age]])




    result = True
    if p[0]:
        userInfo.result = True
        result = True
    else:
        userInfo.result = False
        result = False

    print("-------------------------------")      
    print(p)
    return render(request, 'survey/prediction.html', {'result': result})
 
#---------------------------------------------------------------



           