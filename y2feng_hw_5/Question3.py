"""
Yiduo Feng
Class: CS 677
Date: 04/15/2022
Homework Problem: 3
Description of Problem (just a 1-2 line summary!):
use decision tree to predict
"""
import pandas as pd
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
# get the data frame
df = pd.read_excel(io=file_name, sheet_name=sheet)
df = pd.DataFrame(df, columns=["MSTV", "Width", "Mode", "Variance", "NSP"])
nsp_2 = []
for i in df['NSP'].values:
    if i == 1:
        nsp_2.append(1)
    else:
        nsp_2.append(0)
#create new column
df['NSP_2'] = nsp_2
df = df.drop([0, len(df)-1, len(df)-2, len(df)-3])


train_0, test_0 = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :4], df.loc[:, "NSP_2"],
                     test_size=0.5, random_state=3)

# predict the y
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(Y_test,y_pred)

#confusion matrix
mat = confusion_matrix(y_pred, Y_test)
def get_result_3():
    print("accuracy = ", accuracy)
    print("confusion matrix = ", mat)
sns.heatmap(mat.T,square=True, annot=True, fmt = 'd', cbar=True,
    xticklabels=["positive", "negative"], yticklabels=["positive", "negative"])
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()
#table row
def get_summary_3():
    summary = ["decision tree", mat[0][0], mat[1][0], mat[1][1], mat[0][1],
                accuracy, mat[0][0]/(mat[0][0] + mat[0][1]),
               mat[1][1]/(mat[1][1] + mat[1][0])]
    return (summary)