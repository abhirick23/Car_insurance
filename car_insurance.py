# -*- coding: utf-8 -*-
"""bank_marketting

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17ZYRljG9BZmP8s4zMBL_QPUtRClfcxOC
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/gdrive/')
# %cd /gdrive

ls

cd /gdrive/MyDrive/insurance

ls

"""# Importing Libraries"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier as rf
import warnings
warnings.filterwarnings("ignore")

"""# Uploading Dataset"""

df_train=pd.read_csv('carInsurance_train.csv')
df_train.head()

df_test=pd.read_csv('carInsurance_test.csv')
df_test.head()

df_train.info()

df_test.info()

df_train.describe()

"""# EDA"""

df_train.isna().sum()

df_test.isna().sum()

df_train['Job'].fillna(df_train['Job'].mode()[0], inplace=True)
df_train['Outcome'].fillna(df_train['Outcome'].mode()[0], inplace=True)
df_train['Communication'].fillna(df_train['Communication'].mode()[0], inplace=True)
df_train['Education'].fillna(df_train['Education'].mode()[0], inplace=True)

df_test['Job'].fillna(df_test['Job'].mode()[0], inplace=True)
df_test['Outcome'].fillna(df_test['Outcome'].mode()[0], inplace=True)
df_test['Communication'].fillna(df_test['Communication'].mode()[0], inplace=True)
df_test['Education'].fillna(df_test['Education'].mode()[0], inplace=True)

df_train.isna().sum().sum()

df_test.isna().sum().sum()

df_train.columns

df_train.CarInsurance.value_counts()

columns = df_train.columns
binary_cols = []
remain_cols=[]
for col in columns:
    if df_train[col].value_counts().shape[0] == 2:
        binary_cols.append(col)
    else:
      remain_cols.append(col)

binary_cols

remain_cols

sns.countplot("CarLoan", data=df_train)

sns.countplot("Marital", data=df_train)

sns.countplot("Job", data=df_train)

sns.countplot("Education", data=df_train)

sns.countplot("Communication", data=df_train)

sns.countplot("LastContactMonth", data=df_train)

sns.countplot("Outcome", data=df_train)

Marital_numeric = { 'single':0,'married':1,'divorced':2}
df_train.Marital.replace(Marital_numeric, inplace=True)

Education_numeric = { 'tertiary':0,'primary':1,'secondary':2}
df_train.Education.replace(Education_numeric, inplace=True)

Communication_numeric = { 'telephone':0,'cellular':1}
df_train.Communication.replace(Communication_numeric, inplace=True)

LastContactMonth_numeric = { 'jan':0,'feb':1,'mar':2,'apr':3,'may':4,'jun':5,'jul':6,'aug':7,'sep':8,'oct':9,'nov':10,'dec':11}
df_train.LastContactMonth.replace(LastContactMonth_numeric, inplace=True)

Outcome_numeric = { 'failure':0,'other':1,'success':2}
df_train.Outcome.replace(Outcome_numeric, inplace=True)

Job_numeric = { 'management':0,'blue-collar':1,'student':2 ,'technician':3,'admin.':4,'services':5 ,'self-employed':6,'retired':7,'housemaid':8,'entrepreneur':9,'unemployed':10}
df_train.Job.replace(Job_numeric, inplace=True)

Marital_numeric = { 'single':0,'married':1,'divorced':2}
df_test.Marital.replace(Marital_numeric, inplace=True)
Education_numeric = { 'tertiary':0,'primary':1,'secondary':2}
df_test.Education.replace(Education_numeric, inplace=True)
Communication_numeric = { 'telephone':0,'cellular':1}
df_test.Communication.replace(Communication_numeric, inplace=True)
LastContactMonth_numeric = { 'jan':0,'feb':1,'mar':2,'apr':3,'may':4,'jun':5,'jul':6,'aug':7,'sep':8,'oct':9,'nov':10,'dec':11}
df_test.LastContactMonth.replace(LastContactMonth_numeric, inplace=True)
Outcome_numeric = { 'failure':0,'other':1,'success':2}
df_test.Outcome.replace(Outcome_numeric, inplace=True)
Job_numeric = { 'management':0,'blue-collar':1,'student':2 ,'technician':3,'admin.':4,'services':5 ,'self-employed':6,'retired':7,'housemaid':8,'entrepreneur':9,'unemployed':10}
df_test.Job.replace(Job_numeric, inplace=True)

corrmat = df_train.corr()
fig = plt.figure(figsize = (12, 9))
sns.heatmap(corrmat, vmax = .8, square = True)
plt.show()

fig, ax = plt.subplots(4, 2, figsize = (15, 13))
sns.boxplot(x= df_train["HHInsurance"], ax = ax[0,0])
sns.distplot(df_train['HHInsurance'], ax = ax[0,1])
sns.boxplot(x= df_train["DaysPassed"], ax = ax[1,0])
sns.distplot(df_train['DaysPassed'], ax = ax[1,1])
sns.boxplot(x= df_train["NoOfContacts"], ax = ax[2,0])
sns.distplot(df_train['NoOfContacts'], ax = ax[2,1])
sns.boxplot(x= df_train["PrevAttempts"], ax = ax[3,0])
sns.distplot(df_train['PrevAttempts'], ax = ax[3,1])
plt.tight_layout()

sns.set(rc={'figure.figsize':(11.7,8.27)})
cData_attr = df_train.iloc[:, 0:7]
sns.pairplot(cData_attr, diag_kind='kde')

X = df_train.drop(['CarInsurance', 'CallStart',	'CallEnd'], axis = 1)
Y = df_train["CarInsurance"]
x_Data = X.values
y_Data = Y.values

#Q = df_test.drop(['CarInsurance', 'CallStart',	'CallEnd'], axis = 1)
#W = df_test["CarInsurance"]
#q_Data = Q.values
#w_Data = W.values

#X_train=x_Data
#y_train=y_Data
#X_test=q_Data
#y_test=w_Data

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_Data, y_Data, test_size = 0.2, random_state = 42)

"""# Naive Bayes"""

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,y_train)

model.score(X_test,y_test)

from sklearn.model_selection import cross_val_score
print(cross_val_score(GaussianNB(),X_train, y_train, cv=5))

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

pred = model.predict(X_train) 
accuracy_score(y_train, pred)

confusion_matrix(y_train, pred)

predicted_test = model.predict(X_test)
p=accuracy_score(y_test, predicted_test)

from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score

print(classification_report(y_test, predicted_test))

cma = confusion_matrix(y_test, predicted_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap=plt.cm.Blues, alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Random forest Classifier"""

clf_forest = rf(n_estimators=100, max_depth=10)
clf_forest.fit(X_train, y_train)

pred = clf_forest.predict(X_train)
accuracy_score(y_train, pred)

confusion_matrix(y_train, pred)

pred_test = clf_forest.predict(X_test)
q=accuracy_score(y_test, pred_test)

from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score

print(classification_report(y_test, pred_test))

cma = confusion_matrix(y_test, pred_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="coolwarm_r", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Decision Tree Classifier"""

from sklearn import tree

clf = tree.DecisionTreeClassifier()
 clf = clf.fit(X_train, y_train)

pred1 = clf.predict(X_train)
accuracy_score(y_train, pred1)

confusion_matrix(y_train, pred1)

pred1_test = clf.predict(X_test)
r=accuracy_score(y_test, pred1_test)

print(classification_report(y_test, pred1_test))

cma = confusion_matrix(y_test, pred1_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="coolwarm_r", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Logistic Regression"""

from sklearn.linear_model import LogisticRegression  
clf= LogisticRegression(random_state=0)  
clf.fit(X_train, y_train)

pred_LR= clf.predict(X_train)
accuracy_score(y_train, pred_LR)

confusion_matrix(y_train, pred_LR)

pred_LR_test = clf.predict(X_test)
s=accuracy_score(y_test, pred_LR_test)

print(classification_report(y_test, pred_LR_test))

cma = confusion_matrix(y_test, pred_LR_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="coolwarm_r", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Support Vector Machine"""

from sklearn.svm import SVC  
classifier = SVC(kernel='linear', random_state=0)  
classifier.fit(X_train, y_train)

pred_SVM= classifier.predict(X_train)
accuracy_score(y_train, pred_SVM)

confusion_matrix(y_train, pred_SVM)

pred_SVM_test = classifier.predict(X_test)
t=accuracy_score(y_test, pred_SVM_test)

print(classification_report(y_test, pred_SVM_test))

cma = confusion_matrix(y_test, pred_SVM_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="prism", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Neural networks"""

from sklearn.neural_network import MLPClassifier

clf= MLPClassifier(solver='lbfgs', alpha=1e-5,
           hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X_train, y_train)

pred_NN= clf.predict(X_train)
accuracy_score(y_train, pred_NN)

confusion_matrix(y_train, pred_NN)

pred_NN_test = clf.predict(X_test)
u=accuracy_score(y_test, pred_NN_test)

print(classification_report(y_test, pred_NN_test))

cma = confusion_matrix(y_test, pred_NN_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="prism", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# XGBOOST"""

import xgboost as xgb

xgb = xgb.XGBClassifier()
xgb.fit(X_train,y_train)

pred_XGB= xgb.predict(X_train)
accuracy_score(y_train, pred_XGB)

confusion_matrix(y_train, pred_XGB)

pred_XGB_test = xgb.predict(X_test)
v=accuracy_score(y_test, pred_XGB_test)

print(classification_report(y_test, pred_XGB_test))

cma = confusion_matrix(y_test, pred_XGB_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="prism", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Comparative predicting"""

import numpy as np
import matplotlib.pyplot as plt
# creating the dataset
data = {'NB':p, 'RF':q, 'DT':r,'LR':s,'SVM':t,'NN':u,'XGB':v}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 6))
# creating the bar plot
plt.bar(courses, values, color ='crimson',
		width = 0.4)
plt.xlabel("Algorithms")
plt.ylabel("Accuracy")
plt.title("Comparitive analysis of algorithm on the basis of the acccuracy")
plt.show()

activities = ['NB', 'RF', 'DT', 'LR','SVM','NN','XGB'] 
# portion covered by each label
slices = [p,q,r,s,t,u,v]
 
# color for each label
colors = ['red', 'blue', 'green','yellow','purple','black','crimson']
 
# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
        startangle=90, shadow = True, explode = (0, 0, 0.1,0,0,0.1,0),
        radius = 1.2, autopct = '%1.1f%%')
 
# plotting legend
plt.legend()
 
# showing the plot
plt.show()