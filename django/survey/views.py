from django.shortcuts import render
from .forms import SurveyForm
from .loadFile import *
from django.shortcuts import render
from .models import SurveyInfo
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
#---------------------------------------------------------------
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
#---------------------------------------------------------------
def landing(request):
    return render(request, 'survey/landing.html')
#---------------------------------------------------------------
def Loadfile(request):
    save_csv_data_to_db("survey/Diabetes.csv.csv")
    return render(request, 'survey/landing.html')
#---------------------------------------------------------------  
def predictionView(request):
    knn = KNeighborsClassifier(n_neighbors=36)
    userInfo = request.user.survey

    # surveyInfo = SurveyInfo.objects.exclude(id= userInfo.id)
    surveyInfo = SurveyInfo.objects.filter(isTrain = True)
    print(surveyInfo.count())

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

    # print(new_data)
    df = pd.DataFrame(data,columns=['Pregnancies', 'Glucose',
     'BloodPressure', 'Insulin', 'weight', 'DiabetesPedigreeFunction', 
     'Age','result'])

    x=df.drop(['result'],axis=1) 
    y=df['result']


    xtrain, xtest, ytrain, ytest = train_test_split(x, y,test_size=0.3, random_state=132)


    knn.fit(xtrain,ytrain)


    p = knn.predict([[userInfo.Pregnancies, userInfo.Glucose, userInfo.BloodPressure,
    userInfo.Insulin, userInfo.BMI(), userInfo.DiabetesPedigreeFunction, userInfo.Age]])

    if p == 1:
        result = "Positive"
    else:
        result = "Negative"
        

    return render(request, 'survey/prediction.html', {'result': result})
 
#---------------------------------------------------------------



           