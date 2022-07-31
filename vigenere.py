import re
from tabulate import tabulate
import pandas

# import matplotlib.pyplot as plt
# from numpy import average

"""
Parte I: cifrador/decifrador
"""
# Função que cifra um texto a partir de uma chave
def cypher(key: str, message: str) -> str:
    __validate_key(key)
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
            keystream.insert(0, keystream.pop())
        else:
            cyphertext += MATRIX[i][j]

    return cyphertext


# Função que decifra um texto a partir de uma chave
def decypher(key: str, cyphertext: str) -> str:
    __validate_key(key)
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
            keystream.insert(0, keystream.pop())
        else:
            decyphertext += MATRIX[0][j]

    return decyphertext


"""
Parte II: ataque de recuperação de senha por análise de frequência
"""
# Função que tenta decifrar um texto sem a chave
def decypher_withou_key(cyphertext: str, language: str = "english") -> None:
    key = password_recovery_attack(cyphertext, language)
    return decypher(key, cyphertext)


# Função que faz o ataque de recuperação de senha por análise de frequência
def password_recovery_attack(
    text: str, language: str = "english", max_try: int = 10, show_steps: bool = False
):
    text = text.upper()
    text = re.sub("[^A-Z]", "", text)

    if not language in LANGUAGES:
        raise "language not supported!"

    # Descobrir o tamanho da chave
    key_lenght = get_key_length(text, language, max_try, show_steps)

    # pegar a frequencia da lingua do texto
    language_frequencies = get_language_frequencies(language)

    # dividir o texto em grupos de cifras simples (cesar)
    text_sliced_by_key_lenght = __slicing_cyphertex(text, key_lenght)

    # calcular a frequencia de cada grupo e suas variantes
    frequencies = []
    for group in text_sliced_by_key_lenght:
        shifts = []
        for i in range(len(ALPHABET)):
            shift_text = __shift_left(group, i)
            shifts.append(__calculate_frequency(shift_text))
        frequencies.append(shifts)

    # tabela com todos os x² possíveis
    tableX = __table_of_cosets(frequencies, language_frequencies)

    # Cada coset é uma posição da chave
    # Quanto menor o X² para um coset mais chances de pertencer a chave
    for coset in tableX:
        tableX[coset] = {
            k: v for k, v in sorted(tableX[coset].items(), key=lambda item: item[1])
        }
    most_possible_key = __most_possible_key(tableX)

    if show_steps:
        print(f"COSETS OF X² METHOD FOR KEY LENGHT {key_lenght}")
        print(
            "The letter with the smallest X² value for each coset\nis probably the right letter for that position in key"
        )
        print()
        __show_cosets(tableX)

        print(f"automatic choice: {most_possible_key}")
        print()

    return {"most_possible_key": most_possible_key, "table": tableX}


# Função que retorna o tamanho mais provável da chave
def get_key_length(
    cyphertext: str,
    language: str = "english",
    max_try: int = 10,
    show_steps: bool = False,
) -> int:
    cyphertext = cyphertext.upper()
    cyphertext = re.sub("[^A-Z]", "", cyphertext)

    language_ic = get_language_ic(language)

    texts = []
    for i in range(max_try):
        texts.append(__slicing_cyphertex(cyphertext, i + 1))

    averages = {}
    for group in texts:
        average = 0
        for text in group:
            average += __ic(text)
        averages[len(group)] = average / len(group)

    largest_ic = {
        k: v
        for k, v in sorted(averages.items(), key=lambda item: item[1], reverse=True)
    }

    closest_ic = {
        k: v
        for k, v in sorted(
            averages.items(),
            key=lambda item: abs(item[1] - language_ic),
        )
    }
    # print(largest_ic)
    # print(closest_ic)
    if show_steps:
        print()
        print("INDICIES OF COINCIDENCE")
        print(
            "The length that yields the highest average IC and close to IC\nof language is likely to be the correct length of the keyword"
        )
        print()
        print(f"IC of {language}: {language_ic:.4f}")
        print()
        print("Closests ICs")
        __show_ic(closest_ic)
        print("Highests ICs")
        __show_ic(largest_ic)

    closest = list(closest_ic.keys())[0]
    largest = list(largest_ic.keys())[0]

    # gcd_closest_largest = gcd(largest, closest)

    # maiores até o mais próximo
    l = list(largest_ic.keys())[: (list(largest_ic.keys())).index(closest)]
    if closest_ic[closest] > language_ic:
        l.append(closest)

    # pegar o número que mais tem multipĺos na lista de maiores até o mais próximo
    multiples_list = []
    for i in range(len(l)):
        multiples_list.append([n for n in l if n % l[i] == 0])
    multiples_list.sort(reverse=True, key=len)

    dict_multiples = {f"{gcd_list(l)}": l for l in multiples_list}

    if show_steps:
        if len(dict_multiples) > 10:
            dict_multiples_limited = {
                k: v for k, v in list(dict_multiples.items())[:10]
            }
        else:
            dict_multiples_limited = dict_multiples

        print("Separating the largest to the closest by gcd")
        print(
            tabulate(
                dict_multiples_limited,
                headers=[f"GCD {k}" for k in dict_multiples_limited],
            )
        )
        print()

    # Retorna a o tamanho da chave mais provável
    return int(list(dict_multiples.keys())[0])

    # gcd_of_largest = gcd_list(multiples_list[0])
    # if gcd_of_largest > 1:
    #     return gcd_of_largest

    # gcd_of_largest = gcd_list(l)
    # if gcd_of_largest > 1:
    #     return gcd_of_largest

    # for length in largest_ic:

    # if closest_ic[closest] < language_ic:

    # if gcd_closest_largest > 1:
    #     return gcd_closest_largest

    # return closest


"""
Funções auxiliares
"""
# Função que calcula o maior divisor comum
def gcd(*args) -> int:
    if len(args) > 1:
        args = list(args)
        args[1] = __gcd_of_2_numbers(args[0], args[1])
        args = tuple(args[1:])
        gcd(*args)

    return int(args[0])


def gcd_list(list):
    if len(list) <= 1:
        return int(list[0])

    list[1] = __gcd_of_2_numbers(list[0], list[1])
    return gcd_list(list[1:])


def __gcd_of_2_numbers(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


# Função que mostra uma tabela com as posíveis letras para cada posição da chave
def __show_cosets(tableX, max_rows: int = 10):
    if max_rows > len(tableX["coset1"]):
        max_rows = len(tableX["coset1"])

    for coset in tableX:
        tableX[coset] = [
            f"{__numbers_to_text([k])} - {v:6.3f}" for k, v in tableX[coset].items()
        ][: max_rows - 1]

    # print(tabulate(tableX, headers="keys"))
    print(pandas.DataFrame(tableX))
    print()


# Função que mostra uma tabela com os posíveis tamanhos de chave a partir do indice de conhecidência
def __show_ic(ic, max_rows: int = 10):
    if max_rows > len(ic):
        max_rows = len(ic)
    print(
        tabulate(
            [[k, v] for k, v in ic.items()][: max_rows - 1],
            headers=["key length", "average of ICs"],
            floatfmt=".4f",
        )
    )
    print()


# Função que faz a tabela de cosets
def __table_of_cosets(frequencies, language_frequencies):
    tableX = {}
    i = 0
    for group in frequencies:
        i += 1
        list_x_pow_2 = {}
        for shift_text in range(len(group)):
            list_x_pow_2[shift_text] = __calculate_x_pow_2(
                group[shift_text], language_frequencies
            )
        tableX[f"coset{i}"] = list_x_pow_2

    return tableX


# Função que pega a chave mais próvavel a partir de uma tabela de cosets
def __most_possible_key(tableX):
    most_possible_key = []
    for coset in tableX:
        most_possible_key.append(list(tableX[coset].keys())[0])
    most_possible_key = __numbers_to_text(most_possible_key)
    return most_possible_key


# Função que calcula o indice de conhecidência de um texto
def __ic(text):
    if len(text) <= 1:
        return 1
    text = text.upper()
    text = re.sub("[^A-Z]", "", text)
    frequencies = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0,
    }
    for letter in text:
        frequencies[letter] += 1

    ICgroup = []
    for letter in frequencies:
        ICgroup.append(
            (frequencies[letter] * (frequencies[letter] - 1))
            / (len(text) * (len(text) - 1))
        )

    return sum(ICgroup)


# Função que cria uma matriz do alfabeto
def __make_matrix(alphabet: str) -> list:
    matrix = []
    alphabet = list(alphabet)
    for _ in range(len(alphabet)):
        matrix.append("".join(alphabet))
        alphabet.append(alphabet.pop(0))

    return matrix


# Função que válida uma chave, chave para cifração deve conter apenas letras
def __validate_key(key: str) -> None:
    key = key.upper()
    for char in key:
        if ALPHABET.find(char) == -1:
            raise "Key must be a single word!"


# Função para calcular a frequência das letras em um texto
def __calculate_frequency(text: str) -> dict[str, float]:
    text = text.upper()
    text = re.sub("[^A-Z]", "", text)
    frequencies = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0,
    }
    for letter in text:
        frequencies[letter] += 1

    text_length = len(text)
    for key in frequencies:
        frequencies[key] = frequencies[key] / text_length

    return frequencies


# Função que pega a frenquência relativa para uma determinada lingua
def get_language_ic(language: str = "english") -> float:
    if language == "portuguese":
        return PORTUGUESE_INDEX_OF_COINCIDENCE

    return ENGLISH_INDEX_OF_COINCIDENCE


# Função que pega a frenquência relativa para uma determinada lingua
def get_language_frequencies(language: str = "english") -> dict[str, float]:
    if language == "portuguese":
        return PORTUGUESE_RELATIVE_FREQUENCIES

    return ENGLISH_RELATIVE_FREQUENCIES


# Função que quebra o texto cifrado em cifras simples a partir do tamnaho da chave
def __slicing_cyphertex(cyphertext: str, key_lenght: int) -> list[str]:
    return [cyphertext[i::key_lenght] for i in range(key_lenght)]


# Função que transforma um texto em uma lista de números, ex: "ABC" -> [0,1,2]
def __text_to_numbers(text: str) -> list[int]:
    return [ord(x) - 65 for x in text]


# Função que trasforma uma lista de números em um texto, ex: [0,1,2] -> "ABC"
def __numbers_to_text(numbers: list[int]) -> str:
    return "".join([chr(x + 65) for x in numbers])


# Função que desloca um texto a partir de uma posição
def __shift_left(text: str, shift: int) -> str:
    text = __text_to_numbers(text)
    return __numbers_to_text([(x - shift) % 26 for x in text])


# Função que calcula o quão parecida a frêquencia do texto está com a frêquencia relativa da língua, quanto menor o número mais pŕoximo
def __calculate_x_pow_2(frequencies: dict, language_frequencies: dict) -> float:
    x_pow_2 = 0
    for i in ALPHABET:
        x_pow_2 += (
            (frequencies[i] - language_frequencies[i])
            * (frequencies[i] - language_frequencies[i])
        ) / language_frequencies[i]
    return x_pow_2


# Constantes
LANGUAGES = ["english", "portuguese"]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MATRIX = __make_matrix(ALPHABET)
PORTUGUESE_INDEX_OF_COINCIDENCE = 1.94 / len(ALPHABET)
PORTUGUESE_RELATIVE_FREQUENCIES = {
    "A": 0.1463,
    "B": 0.0104,
    "C": 0.0388,
    "D": 0.0499,
    "E": 0.1257,
    "F": 0.0102,
    "G": 0.0130,
    "H": 0.0128,
    "I": 0.0618,
    "J": 0.0040,
    "K": 0.0002,
    "L": 0.0278,
    "M": 0.0474,
    "N": 0.0505,
    "O": 0.1073,
    "P": 0.0252,
    "Q": 0.0120,
    "R": 0.0653,
    "S": 0.0781,
    "T": 0.0434,
    "U": 0.0463,
    "V": 0.0167,
    "W": 0.0001,
    "X": 0.0021,
    "Y": 0.0001,
    "Z": 0.0047,
}
ENGLISH_INDEX_OF_COINCIDENCE = 1.73 / len(ALPHABET)
ENGLISH_RELATIVE_FREQUENCIES = {
    "A": 0.08167,
    "B": 0.01492,
    "C": 0.02782,
    "D": 0.04253,
    "E": 0.12702,
    "F": 0.02228,
    "G": 0.02015,
    "H": 0.06094,
    "I": 0.06966,
    "J": 0.00153,
    "K": 0.00772,
    "L": 0.04025,
    "M": 0.02406,
    "N": 0.06749,
    "O": 0.07507,
    "P": 0.01929,
    "Q": 0.00095,
    "R": 0.05987,
    "S": 0.06327,
    "T": 0.09056,
    "U": 0.02758,
    "V": 0.00978,
    "W": 0.02360,
    "X": 0.00150,
    "Y": 0.01974,
    "Z": 0.00074,
}


""" 
    # mostrar os gráficos
    plt.style.use("seaborn-whitegrid")
    # criar subplots
    fig, axes = plt.subplots(nrows=key_lenght // 2, ncols=2)
    # permitir iteração nos subplots
    axes = axes.flatten()
    # definir cada subplot
    for i in range(key_lenght):
        # linhas correspondente a lingua
        axes[i].plot(
            frequencies[i].keys(),
            language_frequencies.values(),
            label=f"_{language}",
            color="#004643",
        )
        # linha correspondente ao texto
        axes[i].plot(
            frequencies[i].keys(),
            frequencies[i].values(),
            label="_text",
            color="#f9bc60",
        )
        # definindo título do gráfico
        axes[i].set_title(f"group: {i}", color="#f9bc60")
        # axes[i].legend()

    # definindo título geral
    plt.suptitle(f"frequency analisys in {language}", color="#004643")
    # Auto adjust
    plt.tight_layout()
    # Display
    plt.show()

    # Calcular fator para cada shift um dos 26 shifts possíveis para cada grupo """
