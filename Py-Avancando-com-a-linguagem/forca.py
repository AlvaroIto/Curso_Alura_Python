from random import choice

def mensagem_abertura():
    print('==========================')
    print('Bem vindo ao jogo da Forca')
    print('==========================')


def gerar_palavra():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    print(palavras)

    palavra_secreta = choice(palavras)
    return palavra_secreta



def jogar():

    mensagem_abertura()

    palavra_secreta = gerar_palavra()

    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append('_')

    perdeu = False
    ganhou = False
    erros = 0

    print(letras_acertadas)

    while not perdeu and not ganhou:
        chute = input('Informe uma letra: ').lower().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        perdeu = erros == 6
        ganhou = '_' not in letras_acertadas
        print(letras_acertadas)

    if ganhou:
        print('Você ganhou!!')
    else:
        print('Você perdeu!!')
    print('Fim do jogo')

if __name__ == '__main__':
    jogar()
