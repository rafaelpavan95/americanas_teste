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
    feature1:float
    feature2:float
    feature3:float
    feature4:float
    feature5:float
    feature6:float
    feature7:float
    feature8:float
    feature9:float
    feature10:float
    feature11:float
    feature12:float
    feature13:float
    feature14:float
    feature15:float 

        
        
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
    
    print(input_data)
    
    ############ início do pipeline
    
    dataframe = pd.DataFrame([input_data])
    
    print(dataframe)
    
    dataframe = ceifar(dataframe,outliers_limites)
    
    dataframe.iloc[:,:] = pipeline.transform(dataframe.iloc[:,:])

    dataframe = dataframe.drop(['feature4'],axis=1)

    output_dict = dataframe.to_dict('records')[0]
    
    print(output_dict)

    feature0 = output_dict['feature0'] 
    feature1 = output_dict['feature1']
    feature2 = output_dict['feature2']
    feature3 = output_dict['feature3']
    feature5 = output_dict['feature5']
    feature6  = output_dict['feature6']
    feature7 = output_dict['feature7']
    feature8 = output_dict['feature8']
    feature9 = output_dict['feature9']
    feature10 = output_dict['feature10']
    feature11 = output_dict['feature11']
    feature12 = output_dict['feature12']
    feature13 = output_dict['feature13']
    feature14 = output_dict['feature14']
    feature15 = output_dict['feature15']
    
    print(feature0,feature1,feature2,feature3,feature5,feature6,feature7,feature8,feature9,feature10,feature11,feature12,feature13,feature14,feature15)


    ########## fim do pipeline
    
    prediction = rf_model.predict(np.array([[feature0,feature1,feature2,feature3,feature5,feature6,feature7,feature8,feature9,feature10,feature11,feature12,feature13,feature14,feature15]]))
    
    print(prediction)
    
    return {'previsto': list(prediction)}

