# Importing the required packages
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from Model import svc, DecisionTree
from DataByFeature import X

# TODO - load trained model


# SVC Prediction
y_pred = svc.predict(X)
print("Predicted values:")
print(y_pred)

# Prediction Factors
print("Confusion Matrix: ", confusion_matrix(y_test, y_pred))
print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
print("Report : ", classification_report(y_test, y_pred))


# Decision Tree Prediction
y_pred = DecisionTree.predict(X)
print("Predicted values:")
print(y_pred)

# Prediction Factors
print("Confusion Matrix: ", confusion_matrix(y_test, y_pred))
print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
print("Report : ", classification_report(y_test, y_pred))
