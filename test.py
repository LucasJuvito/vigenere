import vigenere

message = "Professor universitário. Juntamente com José Saramago (Prémio Nobel de Literatura, 1998), Luiz Francisco Rebello, Manuel da Fonseca e Urbano Tavares Rodrigues foi, em 1992, um dos fundadores da Frente Nacional para a Defesa da Cultura (FNDC).[1] Natália Correia definiu-o como 'o escritor da possessão do sentimento'. Foi eleito Presidente da Associação de Jovens Escritores de Portugal (AJEP) de 1990 a 1994. Costuma definir-se como um escritor de emoções. E escrever é a sua segunda respiração. A convite de universidades americanas, europeias, asiáticas e australianas tem difundido a língua e cultura portuguesas. A viagem que mais o marcou (e fascinou) foi, em 1992, quando visitou a Austrália e durante a qual foi recebido, para além dos responsáveis governamentais australianos, pelas comunidades portuguesa e timorense. Propôs, em 1992, junto de Mário Soares e Cavaco Silva, respectivamente Presidente da República e Primeiro-Ministro de Portugal, a criação do Departamento de Língua e Cultura Portuguesas na Northern Territory University,em Darwin (Austrália). Os seus livros ou excertos estão traduzidos em inglês, alemão, espanhol, francês e grego. Está referenciado nos mais importantes sitios e publicações sobre a língua e a literatura portuguesas (e.g., Revista Colóquio Letras, da Fundação Calouste Gulbenkian). Foi colaborador de diversos jornais e revistas, entre os quais, Jornal de Letras, Artes e Ideias, Convergência Lusíada (Real Gabinete Português de Leitura), North Perspective (North Territory University, Darwin, Austrália).[2] Letras & Letras e O Escritor."
key = "KEYWORD"

cypher_text = vigenere.cypher(key, message)
print(cypher_text)
print()
decypher_text = vigenere.decypher(key, cypher_text)
print(decypher_text)
