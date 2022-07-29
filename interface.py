from unittest import result
import vigenere
import time
import os
import sys


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def start():
    clear()
    print("         _________ _______  _______  _        _______  _______  _______   ")
    print("|\     /|\__   __/(  ____ \(  ____ \( (    /|(  ____ \(  ____ )(  ____ \  ")
    print("| )   ( |   ) (   | (    \/| (    \/|  \  ( || (    \/| (    )|| (    \/  ")
    print("| |   | |   | |   | |      | (__    |   \ | || (__    | (____)|| (__      ")
    print("( (   ) )   | |   | | ____ |  __)   | (\ \) ||  __)   |     __)|  __)     ")
    print(" \ \_/ /    | |   | | \_  )| (      | | \   || (      | (\ (   | (        ")
    print("  \   /  ___) (___| (___) || (____/\| )  \  || (____/\| ) \ \__| (____/\  ")
    print("   \_/   \_______/(_______)(_______/|/    )_)(_______/|/   \__/(_______/  ")
    print("                                                                          ")
    print("           _______           _______           _______  _______           ")
    print("          (  ____ \|\     /|(  ____ )|\     /|(  ____ \(  ____ )          ")
    print("          | (    \/( \   / )| (    )|| )   ( || (    \/| (    )|          ")
    print("          | |       \ (_) / | (____)|| (___) || (__    | (____)|          ")
    print("          | |        \   /  |  _____)|  ___  ||  __)   |     __)          ")
    print("          | |         ) (   | (      | (   ) || (      | (\ (             ")
    print("          | (____/\   | |   | )      | )   ( || (____/\| ) \ \__          ")
    print("          (_______/   \_/   |/       |/     \|(_______/|/   \__/          ")
    print("                                                                          ")

    time.sleep(1)
    clear()


def end():
    print("Encerrando...")
    sys.exit()


def menu():
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
        cmd = int(input("opção: "))

        if cmd in range(len(options) + 1):
            eval(list(options.keys())[cmd - 1] + "()")
        else:
            print("Digite um número válido")


def cypher():
    clear()
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
    print("selecione uma língua")
    print()
    for l in vigenere.LANGUAGES:
        print(l)

    print()
    while True:
        language = input("opção: ")
        if language.upper() in [l.upper() for l in vigenere.LANGUAGES]:
            break
        else:
            print("Digite uma lingua válida")

    cypher_text = input("Digite o texto cifrado: ")

    result = vigenere.password_recovery_attack(cypher_text, language)

    key = list(result.values())[0]

    print(f"A chave mais provável é: {key}")

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


start()
menu()
