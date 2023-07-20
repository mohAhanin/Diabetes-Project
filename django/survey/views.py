from operator import truediv
from xmlrpc.client import boolean
from django.shortcuts import render
from .forms import SurveyForm
from .loadFile import *
from django.shortcuts import render
from .models import SurveyInfo
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
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
def OrderingDataForTraining(request):

    surveyInfo = SurveyInfo.objects.filter(isTrain = True) | SurveyInfo.objects.filter(isTest = True)
    SurveyInfo.objects.filter(isTest = True).update(isTest=False)


    data = list(surveyInfo.values_list('id', 'Pregnancies','result'))

    df = pd.DataFrame(data,columns=['id', 'Pregnancies','result'])

    x = df.drop(['result'],axis=1) 
    y = df['result']


    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

    SurveyInfo.objects.filter(id__in = X_test['id']).update(isTrain=False, isTest=True)
    SurveyInfo.objects.filter(id__in = X_train['id']).update(isTrain=True, isTest=False)

        

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
# from sklearn import svm
# from sklearn.preprocessing import StandardScaler

# def predictionViewOnD(request):
#     #---------------------------------------
#     #Read info from db
#     userInfo = request.user.survey

#     surveyInfo = SurveyInfo.objects.filter(isTrain = True)

#     data = list(surveyInfo.values_list('Pregnancies', 'Glucose',
#      'BloodPressure', 'Insulin', 'weight', 'DiabetesPedigreeFunction', 
#      'Age','result'))

#     new_data = []

#     for tpl in data:
#         new_tpl = []
#         for item in tpl:
#             if item == True:
#                 new_tpl.append(1)
#             elif item == False:
#                 new_tpl.append(0)
#             else:
#                 new_tpl.append(item)
#         new_data.append(tuple(new_tpl))

#     #---------------------------------------
#     #SVM

#     df = pd.DataFrame(data,columns=['Pregnancies', 'Glucose',
#      'BloodPressure', 'Insulin', 'weight', 'DiabetesPedigreeFunction', 
#      'Age','result'])

#     x = data.iloc[:, :7]
#     y = data["result"]

#     X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.75, random_state=0)

#     # Normalize Features
#     scaler = StandardScaler()
#     scaler.fit(X_train)
#     X_train = scaler.transform(X_train)

#     # Using the best model
#     model = svm.SVC(kernel='rbf')
#     model.fit(X_train, y_train)


#     patient = np.array([[userInfo.Pregnancies, userInfo.Glucose, userInfo.BloodPressure,
#     userInfo.Insulin, userInfo.BMI(), userInfo.DiabetesPedigreeFunction, userInfo.Age]])
    
#     # Normalize the data with the values used in the training set
#     patient = scaler.transform(patient)
        
#     predbest = model.predict(patient)
#     predbest[0]

#     #---------------------------------------
#     result = True
#     if predbest[0]:
#         userInfo.result = True
#         result = True
#     else:
#         userInfo.result = False
#         result = False


#     return render(request, 'survey/prediction.html', {'result': result})


           