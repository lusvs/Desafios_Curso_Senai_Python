#Autor: Lucas SVS
#Data: 27/06/2024 
#Versão 2.0
#Descrição: Joga da velha
#=====================================================

#ARRAY
idosa = [  
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
]

#VARIAVEL
rodadas = 0 
jogador = 'X'

def motrar_vencedor(vencedor): #vencedor escopo local da função
    print('Temos um vencedor')
    return True

#ENTRADA
while rodadas < 9:                              #Determina que quando chegar na 9 rodada, o sistema para
    posicao = input(f'jogador {jogador} escolha uma posição: ')
    posicao_encontrada = False
    for linha in range(3):
        linhaC = ''
        for coluna in range(3):
            if posicao == idosa[linha][coluna]:
                idosa[linha][coluna] = jogador
                posicao_encontrada = True
            linhaC += ' | ' + idosa[linha][coluna] + ' | '
        print(f'{linhaC}')
    if posicao_encontrada == True:
        rodadas = rodadas + 1
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'
    else:
        print('posição não encontrada')

#SAIDA    
    print()
    if idosa[0][0] == idosa[0][1] == idosa[0][2]: #linha 1 
        houve_vencedor = motrar_vencedor(idosa[0][0]) #Precisamos colocar o 'idosa[0][0]' para determinar o vencedor, pois como o algoritmo mudo o jogador a cada lance,
        break                                         #assim que um jogador ganhar a notficação mostrara que o próximo que ganhou, então a colocando iremos falar que quem ganhou foi quem está na casa determinda.

    elif idosa[1][0] == idosa[1][1] == idosa[1][2]: #linha 2
        houve_vencedor = motrar_vencedor(idosa[1][0])
        break

    elif idosa[2][0] == idosa[2][1] == idosa[2][2]: #linha 3
        houve_vencedor = motrar_vencedor(idosa[2][0])
        break

    elif idosa[0][0] == idosa[1][0] == idosa[2][0]: #coluna 1
        houve_vencedor = motrar_vencedor(idosa[0][0])
        break

    elif idosa[0][1] == idosa[1][1] == idosa[2][1]: #coluna 2
        houve_vencedor = motrar_vencedor(idosa[0][1])
        break

    elif idosa[0][2] == idosa[1][2] == idosa[2][2]: #coluna 3
        houve_vencedor = motrar_vencedor(idosa[0][2])
        break

    elif idosa[0][0] == idosa[1][1] == idosa[2][2]: #diagonal 1
        houve_vencedor = motrar_vencedor(idosa[0][0])
        break
    
    elif idosa[0][2] == idosa[1][1] == idosa[2][0]: #diagonal 2
        houve_vencedor = motrar_vencedor(idosa[0][2])
        break

    else:
        houve_vencedor = False
    
    if (houve_vencedor == False):
        print('Deu idosa, acabou')