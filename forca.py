def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "mamao".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

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
