"""
Yiduo Feng
Class: CS 677
Date: 04/15/2022
Homework Problem: 4
Description of Problem (just a 1-2 line summary!):
use random forest to predict
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.pipeline import make_pipeline
from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

file_name = "CTG.xls"
sheet = "Raw Data"
#get the data drame
df = pd.read_excel(io=file_name, sheet_name=sheet)
df = pd.DataFrame(df, columns=["MSTV", "Width", "Mode", "Variance", "NSP"])
nsp_2 = []
for i in df['NSP'].values:
    if i == 1:
        nsp_2.append(1)
    else:
        nsp_2.append(0)
#create new column with 0 and 1
df['NSP_2'] = nsp_2
df = df.drop([0, len(df)-1, len(df)-2, len(df)-3])

#get X_train, X_test, Y_train, Y_test
train_0, test_0 = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :4], df.loc[:, "NSP_2"],
                     test_size=0.5, random_state=3)

#initial the variables
d_line = []
best_acc = 0
best_err = 1
best_Nd = []
best_y_pred = []
#find error rate in each N and d
for d in range(1, 6):
    for N in range(1, 11):
        clf = RandomForestClassifier(n_estimators=1, criterion="entropy", max_depth=2)
        clf.fit(X_train, Y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(Y_test,y_pred)
        error_rate = 1 - accuracy
        if error_rate <= best_err :
            best_acc = accuracy
            best_err = error_rate
            best_Nd = [N, d]
            best_y_pred = y_pred
        d_line.append(error_rate)
    label = "d=" + str(d)
    plt.plot(range(1,11), d_line, label=label)
    d_line = []
plt.xticks(range(1, 11))
plt.legend()
plt.show()
#get result
def get_result_4():
    print("Best combination of N and d is", best_Nd)
    print("The accuracy of that is", best_acc)
    print("The error rate of that is", best_err)

mat = confusion_matrix(best_y_pred, Y_test)
#confusion matrix
def get_mat_4():
    print("confusion matrix = ", mat)
    sns.heatmap(mat.T,square=True, annot=True, fmt = 'd', cbar=True,
        xticklabels=["positive", "negative"], yticklabels=["positive", "negative"])
    plt.xlabel('predicted label')
    plt.ylabel('true label')
    plt.show()
#table row
def get_summary_4():
    summary = ["random forest", mat[0][0], mat[1][0], mat[1][1], mat[0][1],
                accuracy, mat[0][0]/(mat[0][0] + mat[0][1]),
               mat[1][1]/(mat[1][1] + mat[1][0])]
    return (summary)