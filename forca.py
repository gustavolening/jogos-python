def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ['_','_','_','_','_','_']

    enforcou = False
    acertou = False

    print("Fruta com {} letras!".format(str(letras_acertadas.count('_'))), "\n", letras_acertadas)

    #Enquanto não enforcou E não acertou
    while(not enforcou and not acertou):

        chute = input("Qual a letra?").strip() ##Strip serve para tirar os espaços antes e depois da palavra.


        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print("Jogando.........")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
