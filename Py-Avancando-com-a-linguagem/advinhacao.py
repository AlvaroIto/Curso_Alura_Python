from random import randint

def jogar():

    print('===============================')
    print('Bem vindo ao jogo de Advinhação')
    print('===============================')

    numero_secreto = randint(1, 101)
    total_de_tentativas = 0
    rodada = 1

    print(numero_secreto)

    print('Escolha o nível de dificuldade:\n'
          '(1) Fácil (2) Médio (3) Difícil')

    dif = int(input('Digite o nível: '))

    if dif == 1:
        total_de_tentativas = 20
    elif dif == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while rodada <= total_de_tentativas:
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        num = int(input('Digite um número: '))
        print(f'Você digitou: {num}')

        if numero_secreto == num:
            print('Você acertou')
            break
        else:
            if num > numero_secreto:
                print('Você errou! o seu chute foi maior do que o número secreto')
            else:
                print('Você errou! o seu chute foi menor do que o número secreto')

        rodada += 1
    print('Fim do jogo')


if __name__ == '__main__':
    jogar()