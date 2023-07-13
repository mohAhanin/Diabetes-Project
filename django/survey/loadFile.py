import pandas as pd
from .models import SurveyInfo

def save_csv_data_to_db(csv_file_path):
    df = pd.read_csv(csv_file_path)

    for index, row in df.iterrows():
        survey_info = SurveyInfo(
            Pregnancies=row['Pregnancies'],
            Glucose=row['Glucose'],
            BloodPressure=row['BloodPressure'],
            Insulin=row['Insulin'],
            DiabetesPedigreeFunction=row['DiabetesPedigreeFunction'],
            height=1,
            weight=row['BMI'],
            Age=row['Age'],
            result=row['Outcome'] == 1,
            isTrain = True
        )

        survey_info.save()