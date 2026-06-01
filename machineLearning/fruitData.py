import pandas as pd
from sklearn.preprocessing import LabelEncoder as enc
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

dataset = pd.read_csv("fruit_data_with_colors.csv")
# notice: don't use fruit_name, as fruit_label is the encoded version
y = dataset["fruit_label"]
x = dataset.iloc[:, 2:]

# encoding the fruit_subtype column using LabelEncoder
encoder = enc()
x["fruit_subtype"] = encoder.fit_transform(x["fruit_subtype"])
print(x)

# splitting !
trainX, testX, trainY, testY = train_test_split(x, y, test_size = 0.2, random_state = 32)
svmClf = svm.SVC(kernel = "linear")
randomForest = RandomForestClassifier(n_estimators = 50)
# notice: n_estimators is the number of decision trees that the forest creats
decision = DecisionTreeClassifier()
knnClf = KNeighborsClassifier(n_neighbors = 5)
# notice: n_neighbors is the number of items closest to the object

# training !
svmClf.fit(trainX, trainY)
randomForest.fit(trainX, trainY)
decision.fit(trainX, trainY)
knnClf.fit(trainX, trainY)

# testing !
svmPred = svmClf.predict(testX)
randomForestPred = randomForest.predict(testX)
decisionPred = decision.predict(testX)
knnClfPred = knnClf.predict(testX)

# finding the mean absolute error:
print("SVM Error:", (metrics.mean_absolute_error(testY, svmPred)) * 100, "%")
print("Random Forest Error:", (metrics.mean_absolute_error(testY, randomForestPred)) * 100, "%")
print("Decision Tree Error:", (metrics.mean_absolute_error(testY, decisionPred)) * 100, "%")
print("K-Nearest Neighbor Error:", (metrics.mean_absolute_error(testY, knnClfPred)) * 100, "%")

# finding the accuracy score:
print("SVM Error:", (metrics.accuracy_score(testY, svmPred)) * 100, "%")
print("Random Forest Error:", (metrics.accuracy_score(testY, randomForestPred)) * 100, "%")
print("Decision Tree Error:", (metrics.accuracy_score(testY, decisionPred)) * 100, "%")
print("K-Nearest Neighbor Error:", (metrics.accuracy_score(testY, knnClfPred)) * 100, "%")