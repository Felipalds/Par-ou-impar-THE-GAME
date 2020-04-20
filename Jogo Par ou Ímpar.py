#Bibliotecas
from random import randint
from time import sleep
from playsound import playsound
#Variaveis
user = str('')

#Jogo
def jogo(user=''):
    playsound('musica.mp3', False)
    # Variáveis
    choice = str(".")
    vitorias = int()
    cabecalho = str("Par ou Ímpar")
    cabecalho2 = str("THE GAME")
    lista = [0,1,2,3,4,5,6,7,8,9,10]


    # Página Inicial
    print(10 * "=-")
    print(f"{cabecalho:^20}")
    print(f"{cabecalho2:^20}")
    print(10 * "=-")

    #Escolhas
    while choice not in 'ABCD' or choice =="ABCD":
        print('''
    (A) Jogar
    (B) Pontuações
    (C) Créditos
    (D) Sair''')
        choice = str(input("")).upper().strip()

        #Escolhas caso resposta errada
        if choice not in ("ABCD") or choice == "ABCD":
            print("Desculpe, não entendi...")
    #Jogo
    if choice == "A":
        user = str(input("Nickname: "))
        while True:
            parouimpar = str(input("PAR(P) OU ÍMPAR(I)? ")).upper().strip()
            if parouimpar not in 'PI':
                print("Não entendi, digite novamente")
            else:
                numero = int(input("Qual o seu número? (0 - 10)"))
                if numero not in lista:
                    print(f"Número inválido, você não possui {numero} dedos!")
                else:
                    numerocomputador = randint(0,10)
                    soma = numero + numerocomputador

                    #PAR
                    if parouimpar == "P":
                        if soma % 2 == 0:
                            print('')
                            print('-----------------------')
                            print(f'Jogador jogou: {numero}')
                            print(f'Computador jogou: {numerocomputador}')
                            print(f'Soma: {soma}')
                            print("\033[32mVocê Venceu!\033[m")
                            print('-----------------------')
                            vitorias = vitorias + 1
                            sleep(3)
                            print(50 * "\n")
                        elif soma % 2 != 0:
                            sleep(0.5)
                            print('.', end='')
                            sleep(0.5)
                            print('.', end='')
                            sleep(0.5)
                            print('.', end='')
                            sleep(0.5)
                            print('.', end='')
                            print('')
                            print('-----------------------')
                            print(f'Jogador jogou: {numero}')
                            print(f'Computador jogou: {numerocomputador}')
                            print(f'Soma: {soma}')
                            print("\033[31mVocê Perdeu!\033[m")
                            print('-----------------------')
                            sleep(3.5)

                            break

                #ÌMPAR
                    elif parouimpar == "I":
                        if soma % 2 != 0:
                            print('')
                            print('-------------------')
                            print(f'Jogador jogou: {numero}')
                            print(f'Computador jogou: {numerocomputador}')
                            print(f'Soma: {soma}')
                            print("\033[32mVocê Venceu!\033[m")
                            print('--------------------')
                            sleep(3.5)
                            print(50 * "\n")
                            vitorias = vitorias + 1

                        elif soma % 2 == 0:
                            sleep(0.5)
                            print('.', end = '')
                            sleep(0.5)
                            print('.', end='')
                            sleep(0.5)
                            print('.', end='')
                            sleep(0.5)
                            print('.', end='')
                            print('')
                            print('------------------')
                            print(f'Jogador jogou: {numero}')
                            print(f'Computador jogou: {numerocomputador}')
                            print(f'Soma: {soma}')
                            print('------------------')
                            print("\033[31mVocê Perdeu!\033[m")
                            sleep(3)
                            break
        #Ao acabar o jogo
        print("FIM DE JOGO!")
        print(user)
        print(f"Número de vitórias: {vitorias}")
        sleep(3)
        print(50 * "\n")
        jogo()
    elif choice == "B":
        print("AINDA EM FASE DE CONSTRUÇÃO. AGUARDE NOVAS ATUALIZAÇÕES")
        if user == str(''):
            user = str(input('Nickname: '))
        print(user, vitorias, ' PONTOS')
    elif choice == 'C':
        print("Jogo desenvolvido por: Felipalds")
        sleep(0.8)
        print("Programação: Felipalds")
        sleep(0.8)
        print("Lógica: Felipalds")
        sleep(0.8)
        print('Som: Felipalds')
        sleep(0.8)
        print('Arte e Desing: Felipalds')
        sleep(0.8)
        print("Agradecimentos especiais à:")
        sleep(0.8)
        print("Luiz Guilherme F. Rosa")
        print("Gabriel Albuquerque da Silva")
        print("Ellen Gemelli")
        sleep(0.8)
        print("Felipalds, 2020, A EMPRESA DO FUTURO!")
        sleep(1.4)
        print(50 * "\n")
        jogo()
    elif choice == 'D':
        print("Até Logo!")
        sleep(1)
jogo()










#Outros