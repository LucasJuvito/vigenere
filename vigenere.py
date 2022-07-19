def make_matrix(alphabet):
    matrix = []
    alphabet = list(alphabet)
    for i in range(len(alphabet)):
        matrix.append("".join(alphabet))
        alphabet.append(alphabet.pop(0))

    return matrix

def validate_key(key):
    key = key.upper()
    for char in key:
        if ALPHABET.find(char) == -1:
            raise "Key must be a single word!"

def cypher(key, message):
    validate_key(key)    
    key = key.upper()
    message = message.upper()
    keystream = list(key)
    cyphertext = ""
    for char in message:
        i = ALPHABET.find(char)
        aux = keystream.pop(0)
        keystream.append(aux)
        j = ALPHABET.find(aux)
        if i == -1 or j == -1:
            cyphertext += char
            keystream.insert(0,keystream.pop())
        else:
            cyphertext += MATRIX[i][j]
        
        
    return cyphertext

def decypher(key, cyphertext):
    validate_key(key)  
    key = key.upper()
    cyphertext = cyphertext.upper()
    keystream = list(key)
    decyphertext = ""
    for char in cyphertext:
        aux = keystream.pop(0)
        keystream.append(aux)
        i = ALPHABET.find(aux)
        j = MATRIX[i].find(char)
        if i == -1 or j == -1:
            decyphertext += char
            keystream.insert(0,keystream.pop())
        else:
            decyphertext += MATRIX[0][j]

    return decyphertext

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MATRIX = make_matrix(ALPHABET)

PORTUGUESE_RELATIVE_FREQUENCIES = {
    'A'	: 14.63/100,
    'B'	: 1.04/100,
    'C'	: 3.88/100,
    'D'	: 4.99/100,
    'E'	: 12.57/100,
    'F'	: 1.02/100,
    'G'	: 1.30/100,
    'H'	: 1.28/100,
    'I'	: 6.18/100,
    'J'	: 0.40/100,
    'K'	: 0.02/100,
    'L'	: 2.78/100,
    'M'	: 4.74/100,
    'N'	: 5.05/100,
    'O'	: 10.73/100,
    'P'	: 2.52/100,
    'Q'	: 1.20/100,
    'R'	: 6.53/100,
    'S'	: 7.81/100,
    'T'	: 4.34/100,
    'U'	: 4.63/100,
    'V'	: 1.67/100,
    'W'	: 0.01/100,
    'X'	: 0.21/100,
    'Y'	: 0.01/100,
    'Z'	: 0.47/100,
}

ENGLISH_RELATIVE_FREQUENCIES = {
    'A':8.167/100,
    'B':1.492/100,
    'C':2.782/100,
    'D':4.253/100,
    'E':12.702/100,
    'F':2.228/100,
    'G':2.015/100,
    'H':6.094/100,
    'I':6.966/100,
    'J':0.153/100,
    'K':0.772/100,
    'L':4.025/100,
    'M':2.406/100,
    'N':6.749/100,
    'O':7.507/100,
    'P':1.929/100,
    'Q':0.095/100,
    'R':5.987/100,
    'S':6.327/100,
    'T':9.056/100,
    'U':2.758/100,
    'V':0.978/100,
    'W':2.360/100,
    'X':0.150/100,
    'Y':1.974/100,
    'Z':0.074/100
}
