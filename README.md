# Awesome API

## Descrição

Este projeto consiste em um script Python projetado para capturar e armazenar cotações de criptomoedas. Oferece suporte para armazenamento local e em Azure Blob Storage, proporcionando flexibilidade para atender a diferentes necessidades.

## Pré-requisitos

* Python 3.x instalado.
* Pacote azure-storage-blob para uso do Azure Blob Storage. Este pode ser instalado via pip com o comando:

```shell script
pip install azure-storage-blob
```

## Configuração

Antes de utilizar a funcionalidade de armazenamento em Azure Blob Storage, é necessário configurar a string de conexão com suas credenciais do Azure no script.

## Uso

O projeto contém duas classes principais para armazenamento de dados: LocalDataWriter e BlobDataWriter.

Além das duas classes citadas, temos também a classe exchange_rate_api responsável pela requisição na API.

## Armazenamento Local com LocalDataWriter

* Inicialização

```python script
from script_name import LocalDataWriter

# Exemplo de dados

coin = "Bitcoin"
json_data = {"price": 50000}
directory = "./data"

writer = LocalDataWriter(coin, json_data, directory)
```

* Salvamento de dados

```python script
writer.save()
```

## Armazenamento em Azure Blob Storage com BlobDataWriter

* Inicialização

```python script
from script_name import BlobDataWriter

# Substitua com seus dados reais
coin = "Ethereum"
json_data = {"price": 4000}
container_name = "your-container-name"
connect_str = "your-azure-connection-string"

writer = BlobDataWriter(coin, json_data, container_name, connect_str)
```

* Upload de dados

```python script
writer.upload_blob()
```

## Documentação das Classes

### Classe `LocalDataWriter`

* `__init__(self, coin, json_data, directory="./data"):` Inicializa o objeto com a criptomoeda, dados JSON, e diretório para armazenamento.

* `_generate_filename(self):` Gera o nome do arquivo baseado em timestamp.

* `write_to_file(self):`Escreve os dados JSON em um arquivo no diretório especificado.

* `save(self):` Método público que executa o write_to_file e registra o sucesso da operação.

### Classe `BlobDataWriter``

* `__init__(self, coin, json_data, container_name, connect_str):` Inicializa o objeto com a criptomoeda, dados JSON, nome do container e string de conexão para o Azure Blob Storage.

* `upload_blob(self):` Faz o upload dos dados para o Azure Blob Storage.

* `_get_blob_service_client(self):`Obtém o cliente do serviço Blob do Azure.

* `_upload_to_blob(self, blob_service_client):` Realiza o upload dos dados para o blob especificado.

* `_generate_filename(self):` Gera o nome do arquivo para o blob baseado em timestamp.

## Dicionario de dados

| Key | Label |
| --- | ----- |
| bid | Compra |
| ask | Venda |
| varBid | Variação |
| pctChange | Porcentagem Variação |
| high | Máximo |
| low | Mínimo |

## Licença

Distribuído sob a licença MIT.

## Links úteis

* [Documentação API](https://docs.awesomeapi.com.br/api-de-moedas)

## Contato

Eduardo Veloso - [LinkedIn](https://www.linkedin.com/in/eduardoveloso/)

Projeto Link - [Github](https://github.com/eduardoveloso/api_cotacoes)

Blog Pessoal - [Blog](https://eduardoveloso.github.io)
