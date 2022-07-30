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
    
    input_data = input_parameters.json()
    
    input_dictionary = json.loads(input_data)
    
    ############ início do pipeline
    
    dataframe = pd.DataFrame([input_dictionary])
    
    dataframe = ceifar(dataframe,outliers_limites)
    
    dataframe.iloc[:,:] = pipeline.transform(dataframe.iloc[:,:])
    print('0')
    dataframe = dataframe.drop(['feature4'],axis=1)
    print('1')
    output_dict = dataframe.to_dict('records')[0]
    print('2')
    lista = [output_dict[key] for key in output_dict.keys()]
    print('3')
    lista = np.array(lista).reshape(1,-1)
    print('4')
    ########## fim do pipeline
    
    prediction = rf_model.predict(lista)
    print('5')
    
    output = {'predicao': prediction}
    print('6')
    return {'previsto': prediction}

