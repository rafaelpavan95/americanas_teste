# Teste para a vaga de Cientista de Dados Júnior - Americanas | BEE

Nome: Rafael Pavan

Vaga: Cientista de Dados Júnior

Empresa: Americanas

Docker Image: https://hub.docker.com/repository/docker/rafaelpavan95/ambiente_americanas

__________________

## Instruções para utilizar o ambiente Docker:

- Inicialmente, escolha uma pasta em seu computador para clonar este repositório. Então digite:


```
git clone https://github.com/rafaelpavan95/americanas_teste.git
```

- Após isso, colete a imagem do docker:

```
docker pull rafaelpavan95/ambiente_americanas:1.1
```

- Em seguida, digite o comando abaixo, substituindo "$< diretorio >$" pelo caminho ao qual você clonou este repositório em seu computador:

```
docker run --rm --name ambiente -p 8888:8888 -v "$<diretorio>:/home/notebooks" rafaelpavan95/ambiente_americanas:1.1

```

Você deverá receber uma mensagem no terminal, contendo o link para acessar o ambiente Jupyter Notebook com os pacotes necessários instalados. Basta abri-lo em seu navegador.


Exemplo:
  
 - Supondo que clonei o repositório no caminho 'home/rafaelpavan95/Desktop/americanas_teste', então:
 
 ```
 docker run --rm --name ambiente -p 8888:8888 -v "/home/rafaelpavan95/Desktop/americanas_teste:/home/notebooks" rafaelpavan95/ambiente_americanas:1.1
 ```

 ______________
 
 # Conteúdo
 
 Conforme solicitado no case, o projeto foi dividido em 4 etapas: Análise, Preparação, Modelagem e Entrega do Modelo.
 
 [Uma apresentação de slides resumindo as tarefas/análises realizadas pode ser acessada neste link.](https://docs.google.com/presentation/d/11GV9u_vggW3WUcopnulmxoTScxAk1-5PaAoxIy4aJ8M/edit?usp=sharing)
 
 
 # [Análise Exploratória dos Dados](https://github.com/rafaelpavan95/americanas_teste/blob/master/analise_exploratoria.ipynb)
 
 - Realizada análise estatística descritiva e visual dos dados. Tratamento de outliers e assimetria das distribuições das features. Análise da correlação. Visualização da informação através de boxplots, histogramas, gráficos de dispersão, etc. 
 
 # [Preparação dos Dados](https://github.com/rafaelpavan95/americanas_teste/blob/master/preparacao.ipynb)
 
 - Aqui foi criado o pipeline para o projeto, separando os dados em treino e teste e aplicando as transformações necessárias. Clamp de outliers / Yeo-Johnson / MinMaxScalers  

 # [Modelagem](https://github.com/rafaelpavan95/americanas_teste/blob/master/modelagem.ipynb)
 
 - Testado os modelos: Random Forest, KNN, Logistic Regression, Support Vector Machines, XGBoost. Métricas: acurácia, precisão macro, revocação macro, f1 macro e AUC.
 
| Modelos     | Acurácia      | Precisão Macro | Recall Macro | F1 Macro | AUC |   
| ------------- | ------------- | --------    | --------    | --------    | --------    |
| KNN	| 0.614286 |	0.615196 |	0.615479 |	0.614207 |	0.615479 |
| Logistic Regression |	0.628571 | 0.694784 |	0.643735	| 0.608096 |	0.643735 |
| Support Vector Machines |	0.585714	| 0.660714 |	0.603194 |	0.552765	| 0.603194 |
| `Random Forest` |	**0.657143** |	**0.757576** |	**0.674038**	| **0.632867**	| **0.674038** |
| XGBoost |	0.585714 | 0.620000	| 0.598280	| 0.570915	| 0.598280 |
| Dummy	| 0.457143	| 0.453267	| 0.453726	| 0.453125	| 0.453726 |

# [Entrega do Modelo](https://github.com/rafaelpavan95/americanas_teste/blob/master/entrega_do_modelo.ipynb)
 
 - O modelo pode ser consumido tanto localmente, quanto remotamente (via Rest API). A [API](https://github.com/rafaelpavan95/americanas_teste/blob/master/main.py) foi desenvolvida com fastAPI.
 - O deploy foi feito em: https://rafaelpavan-americanas.herokuapp.com/predicao_americanas
 - Exemplo de uso para uma amostra genérica:

```
import json

# caso não tenha instalado em seu computador
#!pip install requests 

import requests

amostra = {
            
             'feature0': 1300.0,
             'feature1': 26,
             'feature2': 2757.6500000000005,
             'feature3': 0.8800000000003338,
             'feature4': -1318.95,
             'feature5': 0.7848457350272233,
             'feature6': 1653,
             'feature7': 0.0067075150137964,
             'feature8': 2.1256021890777355,
             'feature9': 246440,
             'feature10': 42129.62000000001,
             'feature11': 0.0654563226537528,
             'feature12': 51.894000000000005,
             'feature13': 0.0151240169388989,
             'feature14': 110.30600000000004,
             'feature15': 25
            
            }
            
url = 'https://rafaelpavan-americanas.herokuapp.com/predicao_americanas' # Link da API
    
amostra_json = json.dumps(amostra) # amostra que deseja prever

response = requests.post(url, data=amostra_json) # request post

print(response.json()) 

```


