# Importing the required packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import FeatureExtraction

X, y = FeatureExtraction.main()

# TODO - load "featuresMatrix.csv" and "labels.csv"

# separate to training and learning sets: X is the data by feature, y is the class vector(target, distractor, baseline)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=100)

# SVC (sklearn Support Vector Classification)
model = LinearSVC(max_iter=1000)
model.fit(X_train, y_train)
print("SVC model")

# Prediction
y_pred = model.predict(X_test)
print("Predicted values:")
print(y_pred)

# Prediction Factors
print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
print("Report:", classification_report(y_test, y_pred))

# importance = model.coef_[0]
# # summarize feature importance
# for i, v in enumerate(importance):
#     print('Feature: %0d, Score: %.5f' % (i, v))
# # plot feature importance
# plt.bar([x for x in range(len(importance))], importance)
# plt.show()

# Decision Tree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print("Decision Tree model")

# Prediction
y_pred = model.predict(X_test)
print("Predicted values:")
print(y_pred)

# Prediction Factors
print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
print("Report:", classification_report(y_test, y_pred))

# Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
print("Logistic Regression model")

# Prediction
y_pred = model.predict(X_test)
print("Predicted values:")
print(y_pred)

# Prediction Factors
print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
print("Report:", classification_report(y_test, y_pred))

# importance = model.coef_[0]
# # summarize feature importance
# for i, v in enumerate(importance):
#     print('Feature: %0d, Score: %.5f' % (i, v))
# # plot feature importance
# plt.bar([x for x in range(len(importance))], importance)
# plt.show()

# K-nearest neighbors
model = KNeighborsClassifier()
model.fit(X_train, y_train)
print("K-nearest neighbors model")

# Prediction
y_pred = model.predict(X_test)
print("Predicted values:")
print(y_pred)

# Prediction Factors
print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
print("Report:", classification_report(y_test, y_pred))

# Random Forest
model = RandomForestClassifier()
model.fit(X_train, y_train)
print("Random Forest model")

# Prediction
y_pred = model.predict(X_test)
print("Predicted values:")
print(y_pred)

# Prediction Factors
print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
print("Report:", classification_report(y_test, y_pred))

# TODO - save trained models