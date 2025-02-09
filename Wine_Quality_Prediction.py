#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay


Data = pd.read_csv("C:/Users/Asus/Downloads/WINE/WineQT.csv")

print("Dataset Head:")
print(Data.head())

print("\nSummary Statistics:")
print(Data[['density', 'fixed acidity']].describe())

sns.pairplot(Data, x_vars=['density', 'fixed acidity'], y_vars=['quality'], kind='scatter')
plt.title('Density and Fixed Acidity vs. Quality')
plt.show()

Correlation_Matrix = Data.corr()
print("\nCorrelation Matrix with Quality:")
print(Correlation_Matrix['quality'].sort_values(ascending=False))

X = Data.drop('quality', axis=1)
y = Data['quality']

print("\nClass Distribution:")
print(y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
sgd_model = SGDClassifier(random_state=42)
svc_model = SVC(random_state=42)

rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
print(f"\nRandom Forest Accuracy: {rf_accuracy:.2f}")
print("Random Forest Classification Report:")
print(classification_report(y_test, rf_predictions, zero_division=1))

sgd_model.fit(X_train, y_train)
sgd_predictions = sgd_model.predict(X_test)
sgd_accuracy = accuracy_score(y_test, sgd_predictions)
print(f"\nSGD Accuracy: {sgd_accuracy:.2f}")
print("SGD Classification Report:")
print(classification_report(y_test, sgd_predictions, zero_division=1))

svc_model.fit(X_train, y_train)
svc_predictions = svc_model.predict(X_test)
svc_accuracy = accuracy_score(y_test, svc_predictions)
print(f"\nSVC Accuracy: {svc_accuracy:.2f}")
print("SVC Classification Report:")
print(classification_report(y_test, svc_predictions, zero_division=1))

ConfusionMatrixDisplay.from_estimator(rf_model, X_test, y_test)
plt.title("Random Forest Confusion Matrix")
plt.show()

ConfusionMatrixDisplay.from_estimator(sgd_model, X_test, y_test)
plt.title("SGD Confusion Matrix")
plt.show()

ConfusionMatrixDisplay.from_estimator(svc_model, X_test, y_test)
plt.title("SVC Confusion Matrix")
plt.show()

feature_importances = rf_model.feature_importances_
features = X.columns
importance_Data = pd.DataFrame({'Feature': features, 'Importance': feature_importances})
importance_Data = importance_Data.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_Data)
plt.title('Feature Importance - Random Forest')
plt.show()


# In[ ]:




