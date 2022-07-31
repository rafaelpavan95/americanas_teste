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
 
 # [Análise Exploratória dos Dados]()
 
 
 # [Preparação dos Dados]()
 
 
 # [Modelagem]()
 
 
 # [Entrega do Modelo](https://github.com/rafaelpavan95/americanas_teste/blob/master/entrega_do_modelo.ipynb)
 
 - O modelo pode ser consumido tanto localmente, quanto remotamente (via Rest API).
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


