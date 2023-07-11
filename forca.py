import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_da_palavra(palavra_secreta)

    print("Fruta com {} letras!".format(str(letras_acertadas.count('_'))), "\n", letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    #Enquanto não enforcou E não acertou
    while(not enforcou and not acertou):

        chute = chute_do_jogador()


        if(chute in palavra_secreta):
            validacao_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")


def carrega_palavra_secreta(frutas="palavras.txt"):
    arquivo = open(frutas, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_da_palavra(palavra):

    lista = ["_" for letra in palavra]

    return lista


def chute_do_jogador():
    letra_do_chute = input("Qual a letra?").strip().upper() ##Strip serve para tirar os espaços antes e depois da palavra.
    return letra_do_chute


def validacao_chute_correto(palavra, chute, letras):
    index = 0
    for letra in palavra:
        if (chute == letra):
            letras[index] = letra
        index += 1



def imprime_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
