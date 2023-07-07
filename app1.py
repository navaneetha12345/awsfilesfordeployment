from flask import Flask,render_template,request
import json
import boto3
import numpy as np

endpoint_name = "v1-xgboost-diabetes1"
region_name = 'ap-northeast-3'

session = boto3.Session(region_name=region_name,aws_access_key_id='AKIAUSVENS7WOWGHQB3D',
                            aws_secret_access_key='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')
runtime_client = session.client('sagemaker-runtime')

gender = input("Enter gender (male/female): ")
age = float(input("Enter age: "))
hypertension = float(input("Enter hypertension (0 or 1): "))
heart_disease = int(input("Enter heart disease (0 or 1): "))
smoking_history = int(input("Enter smoking history (0-5): "))
bmi = float(input("Enter BMI: "))
HbA1c_level = float(input("Enter HbA1c level: "))
blood_glucose_level = int(input("Enter blood glucose level: "))

input_data = f'{gender}, {age}, {hypertension}, {heart_disease}, {smoking_history}, {bmi}, {HbA1c_level}, {blood_glucose_level}\n'


response = runtime_client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType='text/csv',
    Body=input_data.encode('utf-8')
)

result = response['Body'].read().decode('utf-8')
predictions = json.loads(result)
print(predictions)
predictions1=np.round(float(result))

print('Prediction:', predictions1)