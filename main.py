#!/usr/bin/env python
# coding: utf-8


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json
import pandas as pd
import numpy as np


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
                )

# averiguação do tipo dos dados

class model_input(BaseModel):

    feature0:float
    feature1:int
    feature2:float
    feature3:float
    feature4:float
    feature5:float
    feature6:int
    feature7:float
    feature8:float
    feature9:int
    feature10:float
    feature11:float
    feature12:float
    feature13:float
    feature14:float
    feature15:int 

        
def ceifar(dados, limites):
    
    dados_out = dados.copy()
    
    for col_name in dados:
        
        
        dados_out.loc[dados_out[dados_out[col_name]<limites[col_name][0]].index, [col_name]] = [limites[col_name][0]]
        dados_out.loc[dados_out[dados_out[col_name]>limites[col_name][1]].index, [col_name]] = [limites[col_name][1]]
        

    return dados_out


# carrega o modelo

rf_model = pickle.load(open('modelos/rf.pkl','rb'))

pipeline = pickle.load(open('pipeline/pipeline.pkl','rb'))

outliers_limites = pd.read_csv('pipeline/outliers_limites.csv')

    
@app.post('/predicao_americanas')
def predicao_americanas(input_parameters : model_input):
   
    # recebe dados, verifica, aplica o pipeline e faz previsão
    
    input_data = input_parameters.dict()
    
    feature0 = input_data['feature0'] 
    feature1 = input_data['feature1']
    feature2 = input_data['feature2']
    feature3 = input_data['feature3']
    feature4 = input_data['feature4']
    feature5 = input_data['feature5']
    feature6  = input_data['feature6']
    feature7 = input_data['feature7']
    feature8 = input_data['feature8']
    feature9 = input_data['feature9']
    feature10 = input_data['feature10']
    feature11 = input_data['feature11']
    feature12 = input_data['feature12']
    feature13 = input_data['feature13']
    feature14 = input_data['feature14']
    feature15 = input_data['feature15']
    
    ############ início do pipeline
    
    dataframe = pd.DataFrame([input_data])
    
    
    dataframe = ceifar(dataframe,outliers_limites)
    
    dataframe.iloc[:,:] = pipeline.transform(dataframe.iloc[:,:])

    dataframe = dataframe.drop(['feature4'],axis=1)
    
    dados = dataframe.values

    ########## fim do pipeline
    
    prediction = rf_model.predict(dados)
    
    if prediction == 1:
        
        return {'predicted': 1}
    
    else: return {'predicted': 0}
    
