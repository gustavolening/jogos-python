import random

def imrpime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
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

def jogar():
    imrpime_mensagem_abertura()
    
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_da_palavra(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print("Fruta com {} letras!".format(str(letras_acertadas.count('_'))), "\n", letras_acertadas)

    #Enquanto não enforcou E não acertou
    while(not enforcou and not acertou):

        chute = input("Qual a letra?").strip().upper() ##Strip serve para tirar os espaços antes e depois da palavra.

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1


        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
