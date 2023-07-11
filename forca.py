import random

def imrpime_mensagem_abertura():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
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
    print("Você ganhou :) !!!")

def imprime_mensagem_perdedor():
    print("Você perdeu :( !!!")


def jogar():

    imrpime_mensagem_abertura()
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

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor()


if(__name__ == "__main__"):
    jogar()
