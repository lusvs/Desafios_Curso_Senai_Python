#Autor: Lucas SVS
#Data: 25/06/2024 
#Versão 1.0
#Descrição: Joga da velha
#=====================================================

idosa = [  
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
rodadas = 0 
jogador = 'X'
while rodadas < 9:                                                        #Determina que quando chegar a 9 rodadas o sistema para
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

    #soma = soma + 1 -> soma += 1
    #linha_completa = linha_completa + idosa[linha][coluna] + ' | '