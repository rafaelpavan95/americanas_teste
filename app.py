# !pip install requests

import json
import requests
import pandas as pd
import numpy as np
import pickle
import sklearn

def aplicacao_remota(amostra):
    

    '''
    
    input: 
        
        amostra -> uma amostra que deseja prever, contendo os dados em sua forma bruta na estrutura de dicionário. Exemplo:
        
        
            amostra = {
                        'feature0': 50.0, #float
                        'feature1': 1,    #int
                        'feature2': 159.9,
                        'feature3': 10.509999999999998, #float
                        'feature4': -86.83999999999999, #float
                        'feature5': 0.4120915032679737, #float
                        'feature6': 153, #int
                        'feature7': 0.0032371360866621, #float
                        'feature8': 2.536082474226805, #float
                        'feature9': 47264, #int
                        'feature10': 1193.6, #float
                        'feature11': 0.1339644772117962, #float
                        'feature12': 63.04999999999998, #float
                        'feature13': 0.0065359477124183, #float
                        'feature14': 159.9, #float
                        'feature15': 1 #int
                    }
            
            
            ****** Observação: enviar apenas uma amostra por vez.
            ****** Obedecer aos dtypes originais do conjunto de dados do problema (float e int).
            
    output:
    
            response -> Dicionário contendo o valor previsto (0 ou 1).
    '''

    
    url = 'https://rafaelpavan-americanas.herokuapp.com/predicao_americanas' # Link da API
    

    amostra_json = json.dumps(amostra)


    response = requests.post(url, data=amostra_json)


    return response.json()




def aplicacao_local(amostra):
    

    '''
    
    input: 
        
        amostra -> uma amostra que deseja prever, contendo os dados em sua forma bruta na estrutura de dicionário. Exemplo:
        
        
            amostra = {
                        'feature0': 50.0, #float
                        'feature1': 1,    #int
                        'feature2': 159.9,
                        'feature3': 10.509999999999998, #float
                        'feature4': -86.83999999999999, #float
                        'feature5': 0.4120915032679737, #float
                        'feature6': 153, #int
                        'feature7': 0.0032371360866621, #float
                        'feature8': 2.536082474226805, #float
                        'feature9': 47264, #int
                        'feature10': 1193.6, #float
                        'feature11': 0.1339644772117962, #float
                        'feature12': 63.04999999999998, #float
                        'feature13': 0.0065359477124183, #float
                        'feature14': 159.9, #float
                        'feature15': 1 #int
                    }
            
            
            ****** Observação: enviar apenas uma amostra por vez.
            ****** Obedecer aos dtypes originais do conjunto de dados do problema (float e int).
            
    output:
    
            response -> Dicionário contendo o valor previsto (0 ou 1).
    '''

    
    
    dados = pd.DataFrame([amostra])
    
    rf_model = pickle.load(open('modelos/rf.pkl','rb'))

    pipeline = pickle.load(open('pipeline/pipeline.pkl','rb'))

    limites = pd.read_csv('pipeline/outliers_limites.csv')

    for col_name in dados:
        
        
        dados.loc[dados[dados[col_name]<limites[col_name][0]].index, [col_name]] = [limites[col_name][0]]
        
        dados.loc[dados[dados[col_name]>limites[col_name][1]].index, [col_name]] = [limites[col_name][1]]
        

    
    dados.iloc[:,:] = pipeline.transform(dados.iloc[:,:])

    dados = dados.drop(['feature4'],axis=1)
    
    dados = dados.values
    
    prediction = rf_model.predict(dados)
    
    if prediction == 1:
        
        return {'predicted': 1}
    
    else: return {'predicted': 0}
