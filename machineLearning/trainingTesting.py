import pandas as pd
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

dataset = pd.read_csv(r"C:\Users\ASU\Documents\temporary file (0163)\machineLearning\weather_forecast_preprocessed.csv")
print(dataset)
y = dataset["Play"]
x = dataset.iloc[:, 0:4]

# classifier 1: applyig k-fold cross validation
# step 1: create an object classifier of SVM
clf = svm.SVC(kernel = "linear")

# step 2: training the data using cross_val_score
score = cross_val_score(clf, x, y, cv = 5)
# notice: cross_val_score takes four parameters; the model, the input data, the output data, and the number of folds (k)
print(score)
# notice: this results in five values, each one represents the accuracy of each run

# step 3: find the average accuracy
print(score.mean())

# classifier 2: applying random forest classifier
randomForest = RandomForestClassifier(n_estimators = 50)
randomForestScore = cross_val_score(randomForest, x, y, cv = 5)

# classifier 3: applying k-nearest neighbour classifier
knn = KNeighborsClassifier(n_neighbors = 3)
knnScore = cross_val_score(knn, x, y, cv = 5)

# classifier 4: applying decision tree classifier
decisionTree = DecisionTreeClassifier()
decisionTreeScore = cross_val_score(decisionTree, x, y, cv = 5)

print(f"SVM accuracy: {score.mean()}\nRandom Forest accuracy: {randomForestScore.mean()}")
print(f"K-Nearest Neighbour accuracy: {knnScore.mean()}\nDecision Tree accuracy: {decisionTreeScore.mean()}\n")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 32)
# notice: only specify the test_size or the train_size, no need to specify both unless using only part of the data
# notice: random_state is used to determine how randomly/chaotically it selects the records
# notice: train_test_split returns four arrays; x_train (records used to train the model), x_test (records used to test the model), y_train (output of training data), y_test (output of testing data)

print(x_train)
print(x_test)
print(y_train)
print(y_test)

# step 1: training, using fit method
clf.fit(x_train, y_train)

# step 2: predicting based on testing data
y_pred = clf.predict(x_test)
print("Actual Output:")
print(y_test)
print("Predicted Output:", y_pred)

# step 3: finding the error and accuracy
print("Error:", metrics.mean_absolute_error(y_test, y_pred))
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
