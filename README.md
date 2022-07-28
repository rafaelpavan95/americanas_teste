# Teste para a vaga de Cientista de Dados Júnior - Americanas | BEE

Nome: Rafael Pavan

Vaga: Cientista de Dados Júnior

Empresa: Americanas

Docker Image: https://hub.docker.com/repository/docker/rafaelpavan95/ambiente_americanas

__________________

## Instruções para utilizar o ambiente Docker:

- Inicialmente, abra o terminal e digite:

```
sudo docker pull rafaelpavan95/ambiente_americanas:1.1
```

- Em seguida, digite:

```
sudo docker run --rm --name ambiente -p 8888:8888 rafaelpavan95/ambiente_americanas:1.1
```

- Após isso, um link para o jupyter-notebook deverá ser retornado no terminal. Então, apenas carregue os arquivos/diretórios/notebooks que deseje executar.

- Caso você tenha clonado este repositório em um diretório de seu computador, utilize:

```
sudo docker run --rm --name ambiente -p 8888:8888 -v "$<diretorio>:/home/notebooks" rafaelpavan95/ambiente_americanas:1.1

```

______________
