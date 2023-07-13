import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
#------------------------------------------------------
data = pd.read_csv('Diabetes.csv.csv')
print(type(data))
#------------------------------------------------------
df=pd.DataFrame(data)
#------------------------------------------------------
x=df.drop(['Outcome'],axis=1)
#------------------------------------------------------
y=df['Outcome']
#------------------------------------------------------
xtrain, xtest, ytrain, ytest = train_test_split(x, y,test_size=0.3, random_state=132)
#------------------------------------------------------
knn = KNeighborsClassifier(n_neighbors=36)
knn.fit(xtrain,ytrain)
User=[[0,120,85,24,0,24.2,0.6,23]]
p=knn.predict(User)

print(p[0])