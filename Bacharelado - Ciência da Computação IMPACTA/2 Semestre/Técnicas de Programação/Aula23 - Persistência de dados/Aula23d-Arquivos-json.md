# Arquivos json
* JSON (JavaScript Object Notation): formato de dados leve e legível por humanos que é comumente usado para armazenar e trocar dados estruturados. 
* Baseados em um subconjunto da linguagem JavaScript, mas são independentes de linguagem de programação 
* Um arquivo JSON consiste em pares chave-valor, onde os valores podem ser strings, números, booleanos, arrays, objetos ou valores nulos 
* Estrutura útil para representar dados hierárquicos e complexos, como configurações de aplicativos, dados de API da web, entre outros. 

* Em Python: módulo json para manipulação deste tipo de arquivo:

| **Python**            | **JSON** |
|-----------------------|----------|
| dict                  | object   |
| list, tuple           | array    |
| str                   | string   |
| int, float e Enums    | number   |
| True                  | true     |
| False                 | false    |
| None                  | null     |

* **Em Python**: módulo json para manipulação deste tipo de arquivo 
* * Codificação (serialização) de um objeto em Python para JSON: json.dump (serializar o objeto e gravar em um arquivo JSON) e json.dumps (serializar um objeto e retorná-lo como str) 
* * Decodificação (desserialização) de um JSON para um objeto em Python:  
* * json.load (desserializar o arquivo JSON e retornar objeto Python) e  
* * json.loads(desserializar uma str correspondente ao JSON e retornar um objeto Python)
