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
