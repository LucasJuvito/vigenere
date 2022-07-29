# vigenere

Para usar as funções de cifração e decifração basta importar o arquivo vigenere.py

exemplo:

```
>>> import vigenere
>>> vigenere.cypher("keyword", "some text to cypher")
'CSKA HVAD XM YMGKOV'
>>> vigenere.decypher("keyword", "CSKA HVAD XM YMGKOV")
'SOME TEXT TO CYPHER'
```

Para auxilio de uma interface gráfica simples execute o arquivo interface.py

### Dependências

Para garantir o funcionamento correto do código é preciso instalar as bibliotecas

1. tabulate: ```pip3 install tabulate```
