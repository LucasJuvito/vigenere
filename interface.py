import vigenere
import time
import os
import sys


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def start():
    for i in range(4):
        clear()
        print_especial("vigenere1")
        time.sleep(0.1)
        clear()
        print_especial("vigenere2")
        time.sleep(0.4) if i == 3 else time.sleep(0.1)
        clear()


def end():
    print("Encerrando...")
    sys.exit()


def menu():
    clear()
    print("Escolha uma das opções a seguir:")
    print()
    options = {
        "cypher": "cifrar",
        "decypher": "decifrar",
        "frenquencie_analise": "atacar uma cifra",
        "end": "sair",
    }

    for i, option in enumerate(options.values()):
        print(f"{i+1} - {option}")
    print()

    while True:
        cmd = input("opção: ")
        try:
            cmd = int(cmd)
            if cmd in range(len(options) + 1):
                break
            else:
                print("Digite um número válido")
        except:
            print("Digite um número válido")

    eval(list(options.keys())[cmd - 1] + "()")


def cypher():
    clear()

    print("   ___   ___   ___   ___     _     ___     ___    ___  ")
    print("  / __| |_ _| | __| | _ \   /_\   |   \   / _ \  | _ \ ")
    print(" | (__   | |  | _|  |   /  / _ \  | |) | | (_) | |   / ")
    print("  \___| |___| |_|   |_|_\ /_/ \_\ |___/   \___/  |_|_\ ")
    print("                                                       ")

    key = input("Digite a chave: ")
    text = input("Digite o texto a ser cifrado: ")

    cypher_text = vigenere.cypher(key, text)

    print(f"chave: {key}")
    print(f"texto original: {text}")
    print(f"texto cifrado : {cypher_text}")
    print()
    print("1 - realizar outra cifração")
    print("2 - voltar")
    print("3 - sair")
    print()

    while True:
        cmd = int(input("opção: "))
        if cmd == 1:
            cypher()
        elif cmd == 2:
            menu()
        elif cmd == 3:
            end()
        else:
            print("Digite um número válido")


def decypher():
    clear()

    print("  ___    ___    ___   ___   ___   ___     _     ___     ___    ___  ")
    print(" |   \  | __|  / __| |_ _| | __| | _ \   /_\   |   \   / _ \  | _ \ ")
    print(" | |) | | _|  | (__   | |  | _|  |   /  / _ \  | |) | | (_) | |   / ")
    print(" |___/  |___|  \___| |___| |_|   |_|_\ /_/ \_\ |___/   \___/  |_|_\ ")
    print("                                                                    ")

    key = input("Digite a chave: ")
    cypher_text = input("Digite o texto cifrado: ")

    text = vigenere.decypher(key, cypher_text)

    print(f"chave: {key}")
    print(f"texto cifrado : {cypher_text}")
    print(f"texto original: {text}")
    print()
    print("1 - realizar outra decifração")
    print("2 - voltar")
    print("3 - sair")
    print()

    while True:
        cmd = int(input("opção: "))
        if cmd == 1:
            decypher()
        elif cmd == 2:
            menu()
        elif cmd == 3:
            end()
        else:
            print("Digite um número válido")


def frenquencie_analise():
    clear()
    print_especial("decifrador")
    print()
    print("selecione uma língua")
    print()
    for idx, option in enumerate(vigenere.LANGUAGES):
        print(f"{idx + 1} - {option.capitalize()}")

    print()
    while True:
        language = input("opção: ")
        if language.upper() in [l.upper() for l in vigenere.LANGUAGES]:
            break
        try:
            language = vigenere.LANGUAGES[int(language) - 1]
            break
        except:
            print("Digite uma lingua válida")

    clear()
    print_especial("decifrador")
    print()
    cypher_text = input("Digite o texto cifrado: ")

    clear()
    print_especial("decifrador")
    print()
    print("Deseja visualizar tabelas de possiblididade?")
    print("S - sim")
    print("N - não")
    print()
    show = False
    while True:
        cmd = input("opção: ")
        if cmd.upper() in ["S", "SIM"]:
            show = True
            break
        elif cmd.upper() in ["N", "NÃO", "NAO"]:
            break
        else:
            print("Digite uma opção válida")

    clear()
    print_especial("decifrador")
    print()
    print("É sabido o tamnaho da chave?")
    print("S - sim")
    print("N - não")
    print()
    key_length = None
    max_try = 10
    while True:
        cmd = input("opção: ")
        if cmd.upper() in ["S", "SIM"]:

            clear()
            print_especial("decifrador")
            print()
            print("Qual o tamanho da chave?")
            print("")

            while True:
                cmd = input("tamanho: ")
                try:
                    key_length = int(cmd)
                    break
                except:
                    print("Digite um número inteiro")

            break
        elif cmd.upper() in ["N", "NÃO", "NAO"]:
            clear()
            print_especial("decifrador")
            print()
            print("Quantos tamanhos de chaves devem ser testados?")
            print("")

            while True:
                cmd = input("tamanho: ")
                try:
                    max_try = int(cmd)
                    break
                except:
                    print("Digite um número inteiro")
            break
        else:
            print("Digite uma opção válida")

    clear()
    print_especial("decifrador")
    print()

    print(f"Texto cifrado: {cypher_text}")
    print(f"Língua: {language}")

    result = vigenere.password_recovery_attack(
        cypher_text, language, max_try, show, key_length
    )

    key = list(result.values())[0]

    print(f"\nA chave mais provável é: {key}")

    print()
    print("1 - realizar outro ataque")
    print("2 - voltar")
    print("3 - sair")
    print()

    while True:
        cmd = int(input("opção: "))
        if cmd == 1:
            frenquencie_analise()
        elif cmd == 2:
            menu()
        elif cmd == 3:
            end()
        else:
            print("Digite um número válido")


def print_especial(text):
    if text == "vigenere1":
        print("")
        print("██    ██ ██  ██████  ███████ ███    ██ ███████ ██████  ███████ ")
        print("██    ██ ██ ██       ██      ████   ██ ██      ██   ██ ██      ")
        print("██    ██ ██ ██   ███ █████   ██ ██  ██ █████   ██████  █████   ")
        print(" ██  ██  ██ ██    ██ ██      ██  ██ ██ ██      ██   ██ ██      ")
        print("  ████   ██  ██████  ███████ ██   ████ ███████ ██   ██ ███████ ")
        print("                                                               ")

    if text == "vigenere2":
        print("")
        print("██╗   ██╗██╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗ ███████╗")
        print("██║   ██║██║██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔════╝")
        print("██║   ██║██║██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝█████╗  ")
        print("╚██╗ ██╔╝██║██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══╝  ")
        print(" ╚████╔╝ ██║╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║███████╗")
        print("  ╚═══╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝")
        print("                                                               ")

    if text == "decifrador":
        print(
            " (                     (      (      (                (          )    (     "
        )
        print(
            " )\ )            (     )\ )   )\ )   )\ )     (       )\ )    ( /(    )\ )  "
        )
        print(
            "(()/(    (       )\   (()/(  (()/(  (()/(     )\     (()/(    )\())  (()/(  "
        )
        print(
            " /(_))   )\    (((_)   /(_))  /(_))  /(_)) ((((_)(    /(_))  ((_)\    /(_)) "
        )
        print(
            "(_))_   ((_)   )\___  (_))   (_))_| (_))    )\ _ )\  (_))_     ((_)  (_))   "
        )
        print(
            " |   \  | __| ((/ __| |_ _|  | |_   | _ \   (_)_\(_)  |   \   / _ \  | _ \  "
        )
        print(
            " | |) | | _|   | (__   | |   | __|  |   /    / _ \    | |) | | (_) | |   /  "
        )
        print(
            " |___/  |___|   \___| |___|  |_|    |_|_\   /_/ \_\   |___/   \___/  |_|_\  "
        )


start()
menu()
