import streamlit as st
import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('./Data/WA_Fn-UseC_-HR-Employee-Attrition.csv')

processedData = df.copy()
le = preprocessing.LabelEncoder()
processedData['Attrition'] = le.fit_transform(processedData['Attrition'])
processedData['BusinessTravel'] = le.fit_transform(processedData['BusinessTravel'])
processedData['Department'] = le.fit_transform(processedData['Department'])
processedData['EducationField'] = le.fit_transform(processedData['EducationField'])
processedData['Gender'] = le.fit_transform(processedData['Gender'])
processedData['OverTime'] = le.fit_transform(processedData['OverTime'])
processedData['MaritalStatus'] = le.fit_transform(processedData['MaritalStatus'])
processedData = processedData.drop([
        'EmployeeCount',
        'JobRole',
        'Over18',
        'StandardHours'
        ], axis=1)

st.title("Unsupervised Training")
st.sidebar.header("Unsupervised Training", divider='rainbow')

st.write("In this section ")