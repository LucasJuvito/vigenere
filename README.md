# vigenere

Para usar as funções de cifração e decifração basta importar o arquivo vigenere.py

exemplo:

```python
>>> import vigenere
>>> vigenere.cypher("keyword", "some text to cypher")
'CSKA HVAD XM YMGKOV'
>>> vigenere.decypher("keyword", "CSKA HVAD XM YMGKOV")
'SOME TEXT TO CYPHER'
```

Para auxilio de uma interface gráfica simples execute o arquivo interface.py

> **Dependências da interface**
>
> Para garantir o funcionamento correto do código é preciso instalar as bibliotecas
>
> 1.  tabulate:
>
> ```python
> pip3 install tabulate
> ```
>
> 2.  pandas:
>
> ```python
> pip3 install pandas
> ```

### Principais funções

#### cypher

Recebe duas strings uma **_key_** , que é a chave para cifração, e uma **_message_** que é a mensagem que será cifrada.
Retorna uma string contendo o texto cifrado.

#### decypher

Recebe duas strings uma **_key_** e uma **_cyphertext_** que é a mensagem cifrada.
Retorna uma string contendo o texto decifrado a partir da chave.

#### decypher_withou_key

Recebe um texto cifrado, **_cyphertext_**, e uma lingua, **_language_**. Recupera a chave com base na lingua usando a função password_recovery_attack e decifra o texto cifrado com ela. Não é possível confiar 100% no resultado, pois o a função que recupera a chave retorna uma possível chave e nem sempre ela está correta pois a análise do texto para isso depende de muitos fatores.

#### password_recovery_attack

Recebe um texto cifrado, **_text_**, e uma lingua, **_language_**, e por meio de análise de frequência retorna a chave mais provável que foi usada para cifrar o texto. Pode receber alguns parametros opcionais como **_max_try_** que define até que tamanho de chave será feita a análise; e também **_show_steps_** que define se alguns dados realizados em certos passos cruciais da análise serão mostrados na tela.

Com o tamanho da chave retornado por **_get_key_length_** tenta descobrir qual letra melhor se encaixa para cada posição da chave usando o _X² method_ que se trata em dividir o texto em substrings do texto cifrado em que cada substring contém apenas caracteres cifrados pela mesma posição da chave, assim cada substring é uma cifra simples de César. Para cada substring é calculado qual deslocamento tem um menor X², ou melhor dizendo, tem a frequência das letras que mais se apróxima com a frequência das letras para uma determinada lingua.

#### get_key_length

Retorna o tamanho de chave mais provável para um texto cifrado, esse valor é descoberto por meio da análise dos indices de recorrência presente nas substrings do texto cifrado em comparação ao de uma lingua.
