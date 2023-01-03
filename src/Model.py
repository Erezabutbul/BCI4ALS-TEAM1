# Importing the required packages
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from FeatureExtraction.main import X, y

# TODO - load "featuresMatrix.csv" and "labels.csv"

# separate to training and learning sets: X is the data by feature, y is the class vector(target, distractor, baseline)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

# SVC (sklearn Support Vector Classification)
svc = LinearSVC()
svc.fit(X_train, y_train)

# Prediction
y_pred = svc.predict(X_test)
print("Predicted values:")
print(y_pred)

# Prediction Factors
print("Confusion Matrix: ", confusion_matrix(y_test, y_pred))
print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
print("Report : ", classification_report(y_test, y_pred))


# Decision Tree
DecisionTree = DecisionTreeClassifier()
DecisionTree.fit(X_train, y_train)

# Prediction
y_pred = DecisionTree.predict(X_test)
print("Predicted values:")
print(y_pred)

# Prediction Factors
print("Confusion Matrix: ", confusion_matrix(y_test, y_pred))
print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
print("Report : ", classification_report(y_test, y_pred))

# TODO - save trained models