def make_matrix(alphabet):
    matrix = []
    alphabet = list(alphabet)
    for i in range(len(alphabet)):
        matrix.append("".join(alphabet))
        alphabet.append(alphabet.pop(0))

    return matrix

def validate_key(key):
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
            cyphertext += matrix[i][j]
        
        
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
        j = matrix[i].find(char)
        if i == -1 or j == -1:
            decyphertext += char
            keystream.insert(0,keystream.pop())
        else:
            decyphertext += matrix[0][j]

    return decyphertext

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
matrix = make_matrix(ALPHABET)
