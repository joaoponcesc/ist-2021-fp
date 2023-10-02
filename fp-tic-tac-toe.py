########################################################
# 1 Projeto de Fundamentos de Programacao              #
# Joao Ponces de Carvalho   ist199091                  #
# Novembro de 2020                                     #
########################################################

def eh_tabuleiro(x):
    '''

    :param x: equivale ao tabuleiro
    :return:  verifica se o tabulerio e valido
    '''
    if type(x) != tuple:
        return False
    if len(x) != 3:
        return False
    for c in x:
        if type(c) != tuple:
            return False
        if len(c) != 3:
            return False
        for p in c:
            if (p != 1 and p != 0 and p != -1) or type(p) != int:
                return False
    return True


def eh_posicao(x):
    '''

    :param x: equivale ao tabuleiro
    :return:  verifica se uma posicao e valida
    '''
    if type(x) != int or x <= 0 or x > 9:
        return False
    return True


def obter_coluna(x, y):
    '''

    :param x: equivale ao tabuleiro
    :param y: coluna a obter
    :return: coluna pedida (1 ou 2 ou 3) em tuplo
    '''
    if eh_tabuleiro(x) == False:
        raise ValueError("obter_coluna: algum dos argumentos e invalido")
    if (y != 1 and y != 2 and y != 3) or type(y) != int:
        raise ValueError("obter_coluna: algum dos argumentos e invalido")
    col = ()
    for c in x:
        i = 0
        while i < len(c):
            if (i + 1) == y:
                col += (c[i],)
            i = i + 1
    return col


def obter_linha(x, y):
    '''

    :param x: equivale ao tabuleiro
    :param y: linha a obter
    :return: linha pedida (1 ou 2 ou 3) em tuplo
    '''
    if eh_tabuleiro(x) == False:
        raise ValueError("obter_linha: algum dos argumentos e invalido")
    if (y != 1 and y != 2 and y != 3) or type(y) != int:
        raise ValueError("obter_linha: algum dos argumentos e invalido")
    for c in range(len(x)):
        if c + 1 == y:
            return x[c]


def obter_diagonal(x, y):
    '''

    :param x: equivale ao tabuleiro
    :param y: diagonal a obter
    :return: diagonal pedida (1 ou 2) em tuplo
    '''
    if eh_tabuleiro(x) == False:
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")
    if (y != 1 and y != 2) or type(y) != int:
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")
    i = 0
    j = 2
    diag = ()
    if y == 1:
        while i < len(x):
            diag += (x[i][i],)
            i += 1
    if y == 2:
        while j >= 0 and i < len(x):
            diag += (x[j][i],)
            j -= 1
            i += 1
    return diag


def tabuleiro_str(x):
    '''

    :param x: equivale ao tabuleiro
    :return:  tabuleiro em string
    '''
    if eh_tabuleiro(x) == False:
        raise ValueError("tabuleiro_str: o argumento e invalido")
    barra = ' | '
    skip = '\n' + '-----------' + '\n'
    tabuleiro = tab = final = ''
    for c in x:
        for d in c:
            if d == 1:
                d = 'X'
            if d == -1:
                d = 'O'
            if d == 0:
                d = ' '
            tabuleiro += d + barra
            tab = ' ' + tabuleiro[:9] + ' '
        final += tab + skip
        tab = ''
        tabuleiro = ''
    return final[:59]


def eh_posicao_livre(x, y):
    '''

    :param x: equivale ao tabuleiro
    :param y: posicao a verificar se esta livre
    :return:  True (se a posicao esta livre) e False (se nao esta livre)
    '''
    if eh_posicao(y) == False or eh_tabuleiro(x) == False:
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")
    if y == 1 or y == 2 or y == 3:
        i = j = 0
        while i < len(x[j]):
            if x[j][i] == 0 and i + 1 == y:
                return True
            i += 1
    if y == 4 or y == 5 or y == 6:
        j, i = 1, 0
        while i < len(x[j]):
            if x[j][i] == 0 and i + 4 == y:
                return True
            i += 1
    if y == 7 or y == 8 or y == 9:
        j, i = 2, 0
        while i < len(x[j]):
            if x[j][i] == 0 and i + 7 == y:
                return True
            i += 1
    return False


def obter_posicoes_livres(x):
    '''
    :param x: equivale ao tabuleiro
    :return:  tuplo com todas as posicoes livres
    '''
    if eh_tabuleiro(x) == False:
        raise ValueError("obter_posicoes_livres: o argumento e invalido")
    livres = ()
    i = 0
    som = 1
    while i < len(x):
        l = 0
        while l < len(x[i]):
            if x[i][l] == 0:
                livres += (l + som,)
            l += 1
        som += 3
        i += 1
    return livres


def jogador_ganhador(x):
    '''
    :param x: equivale ao tabuleiro
    :return:  1 (se o jogador vencedor e o X) e -1 (se o jogador vencedor e o O)
    '''
    if eh_tabuleiro(x) == False:
        raise ValueError("jogador_ganhador: o argumento e invalido")
    ganhador = 0
    for c in range(len(x)):
        if obter_linha(x, c + 1) == (1, 1, 1) or obter_coluna(x, c + 1) == (1, 1, 1):
            ganhador = 1
        elif obter_linha(x, c + 1) == (-1, -1, -1) or obter_coluna(x, c + 1) == (-1, -1, -1):
            ganhador = -1
        elif obter_diagonal(x, 2) == (1, 1, 1) or obter_diagonal(x, 1) == (1, 1, 1):
            ganhador = 1
        elif obter_diagonal(x, 2) == (-1, -1, -1) or obter_diagonal(x, 1) == (-1, -1, -1):
            ganhador = -1
    return ganhador


def marcar_posicao(x, y, z):
    '''

    :param x: equivale ao tabuleiro
    :param y: numero que vai ficar na posicao desejada(1 ou -1)
    :param z: posicao do tabuleiro que queremos substituir
    :return:
    '''
    if (eh_tabuleiro(x) == False) or (y != 1 and y != -1) or \
            z not in obter_posicoes_livres(x) or type(y) != int:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if z in range(1, 4):
        if x[0][z - 1] == 0:
            linha1 = list(x[0])
            linha1[z - 1] = y
            return (tuple(linha1),) + (x[1],) + (x[2],)
    if z in range(4, 7):
        if x[1][z - 4] == 0:
            linha1 = list(x[1])
            linha1[z - 4] = y
            return (x[0],) + (tuple(linha1),) + (x[2],)
    if z in range(7, 10):
        if x[2][z - 7] == 0:
            linha1 = list(x[2])
            linha1[z - 7] = y
            return (x[0],) + (x[1],) + (tuple(linha1),)


def escolher_posicao_manual(x):
    '''

    :param x: equivale ao tabuleiro
    :return: a posicao que o utilizador inseriu se esta for livre (senao gera erro)
    '''
    if eh_tabuleiro(x) == False:
        raise ValueError("escolher_posicao_manual: o argumento e invalido")
    posicao = int(input("Turno do jogador. Escolha uma posicao livre: "))  # input que recebe a posicao do jogador
    if posicao in obter_posicoes_livres(x) and eh_posicao(posicao):
        return posicao
    else:
        raise ValueError("escolher_posicao_manual: a posicao introduzida e invalida")


def escolher_posicao_auto(x, y, z):
    '''

    :param x: equivale ao tabuleiro
    :param y: peca do jogador 1 (X) ou -1 (O)
    :param z: dificuldade escolhida (basico ou normal ou perfeito) do computador
    :return:  a posicao em que o computador escolhe jogar de acordo com a estrategia escolhida e o tabuleiro recebido
    '''
    if (eh_tabuleiro(x) == False) or (y != 1 and y != -1) and type(y) != int or \
            (z != 'basico' and z != 'normal' and z != 'perfeito'):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    if z == 'basico':
        return basico(x)
    if z == 'normal':
        return normal(x, y)
    if z == 'perfeito':
        return perfeito(x, y)


def jogo_do_galo(x, y):
    '''

    :param x: peca que o jogador pretende ser (O ou X) durante o jogo
    :param y: dificuldade escolhida pelo jogador para atribuir ao computador
    :return:  jogo final (mostra sempre o tabuleiro atualizado depois de uma jogada ate alguem ganhar ou empatar)
    '''
    if (x != 'O' and x != 'X') or (y != 'basico' and y != 'normal' and y != 'perfeito'):
        raise ValueError('jogo do galo: algum dos argumentos e invalido')
    print('Bem-vindo ao JOGO DO GALO.\nO jogador joga com', "'" + x + "'.")
    new_tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    if x == 'O':
        return jogador_2(new_tab, y)
    if x == 'X':
        return jogador_1(new_tab, y)


######################################
#        NIVEIS DE DIFICULDADE       #
######################################

def basico(x):
    '''
    dificuldade do computador nivel normal

    :param x: equivale ao tabuleiro
    :return: jogada adequada de acordo com o tabuleiro
    '''
    if est_5(x) in range(5, 6):
        return 5
    else:
        return est_7_8(x)


def normal(x, y):
    '''
    dificuldade do computador nivel normal

    :param x: equivale ao tabuleiro
    :param y: 1 ou -1 (depndendo se o computador e X ou O, respetivamente)
    :return: jogada adequada de acordo com o tabuleiro e estrategia
    '''
    jogada = 0
    jog = -(y)
    if est_1(x, y) in range(1, 10):
        jogada = est_1(x, y)
    elif est_2(x, jog) in range(1, 10):
        jogada = est_2(x, jog)
    elif est_5(x) == 5:
        jogada = 5
    elif est_6(x) in range(1, 10):
        jogada = est_6(x)
    elif est_7_8(x) in range(1, 10):
        jogada = est_7_8(x)
    return jogada


def perfeito(x, y):  # ( faltam as estrategias 3 e 4 )
    '''
    dificuldade do computador nivel perfeito

    :param x: equivale ao tabuleiro
    :param y: 1 ou -1 (depndendo se o computador e X ou O, respetivamente)
    :return: jogada adequada de acordo com o tabuleiro e a estrategia
    '''
    jogada = 0
    jog = -(y)
    if est_1(x, y) in range(1, 10):
        jogada = est_1(x, y)
    elif est_2(x, jog) in range(1, 10):
        jogada = est_2(x, jog)
    elif est_5(x) == 5:
        jogada = 5
    elif est_6(x) in range(1, 10):
        jogada = est_6(x)
    elif est_7_8(x) in range(1, 10):
        jogada = est_7_8(x)
    return jogada


############################
#        ESTRATEGIAS       #
############################

def est_1(x, y):
    '''
    verifica se duas pecas estao em linha e decide a posicao para fazer tres em linha e ganhar

    :param x: equivale ao tabuleiro
    :param y: 1 ou -1 (depndendo se o computador e X ou O, respetivamente)
    :return:  posicao que leva a vitoria
    '''
    if est_1_linha(x, y) > 0:
        return est_1_linha(x, y)
    elif est_1_coluna(x, y) > 0:
        return est_1_coluna(x, y)
    elif est_1_diagonal(x, y) > 0:
        return est_1_diagonal(x, y)


def est_2(x, y):
    '''
    verifica se duas pecas estao em linha e decide a posicao para impedir o tres em linha do adversario

    :param x: equivale ao tabuleiro
    :param y: 1 ou -1 (depndendo se o computador e X ou O, respetivamente)
    :return:  posicao que leva a impedir a vitoria do adversario
    '''
    if est_1_linha(x, y) > 0:
        return est_1_linha(x, y)
    elif est_1_coluna(x, y) > 0:
        return est_1_coluna(x, y)
    elif est_1_diagonal(x, y) > 0:
        return est_1_diagonal(x, y)


def est_5(x):
    '''
    verifica se o centro esta livre ( se estiver decide colocar ai a peca )

    :param x: equivale ao tabuleiro
    :return: posicao 5 (centro)  se esta estiver livre
    '''
    if 5 in obter_posicoes_livres(x):
        return 5


def est_6(x):
    '''
    verifica se o adversario possui uma peca num canto e decide jogar no canto oposto

    :param x: equivale ao tabuleiro
    :return:  9 ou 1 ou 3 ou 7 se estiverem livres
    '''
    if 1 not in obter_posicoes_livres(x) and 9 in obter_posicoes_livres(x):
        return 9
    elif 1 in obter_posicoes_livres(x) and 9 not in obter_posicoes_livres(x):
        return 1
    if 3 in obter_posicoes_livres(x) and 7 not in obter_posicoes_livres(x):
        return 3
    elif 3 not in obter_posicoes_livres(x) and 7 in obter_posicoes_livres(x):
        return 7


def est_7_8(x):
    '''
    verifica se os cantos ou as laterais estao livres por esta ordem e decide jogar numa das posicoes

    :param x: equivale ao tabuleiro
    :return: 1 ou 3 ou 7 ou 9 ou 2 ou 4 ou 6 ou 8 se for a jogada adequada
    '''
    if 1 in obter_posicoes_livres(x):
        return 1
    elif 3 in obter_posicoes_livres(x):
        return 3
    elif 7 in obter_posicoes_livres(x):
        return 7
    elif 9 in obter_posicoes_livres(x):
        return 9
    elif 2 in obter_posicoes_livres(x):
        return 2
    elif 4 in obter_posicoes_livres(x):
        return 4
    elif 6 in obter_posicoes_livres(x):
        return 6
    elif 8 in obter_posicoes_livres(x):
        return 8


#####################################
#        DEFENICOES AUXILIARES      #
#####################################

def est_1_linha(x, y):
    '''
    funcao auxiliar as estrategias 1 e 2
    verifica se o tabuleiro possui algum dois em linha numa das tres linhas

    :param x: equivale ao tabuleiro
    :param y: 1 ou -1 (que equivalem as pecas X e O respetivamente)
    :return: posicao que levaria a um tres em linha
    '''
    a, b, c = 1, 2, 3
    pos = 0
    i = 1
    while i < 4:
        if obter_linha(x, i) == (y, y, 0):
            pos = c
        elif obter_linha(x, i) == (0, y, y):
            pos = a
        elif obter_linha(x, i) == (y, 0, y):
            pos = b
        a += 3
        b += 3
        c += 3
        i += 1
    return pos


def est_1_coluna(x, y):
    '''
    funcao auxiliar as estrategias 1 e 2
    verifica se o tabuleiro possui algum dois em linha numa das tres colunas

    :param x: equivale ao tabuleiro
    :param y: 1 ou -1 (que equivalem as pecas X e O respetivamente)
    :return: posicao que levaria a um tres em linha
    '''
    a, b, c = 1, 4, 7
    pos2 = 0
    for e in range(1, 4):
        if obter_coluna(x, e) == (y, y, 0):
            pos2 = c
        elif obter_coluna(x, e) == (0, y, y):
            pos2 = a
        elif obter_coluna(x, e) == (y, 0, y):
            pos2 = b
        a += 1
        b += 1
        c += 1
    return pos2


def est_1_diagonal(x, y):
    '''
    funcao auxiliar as estrategias 1 e 2
    verifica se o tabuleiro possui algum dois em linha numa das duas diagonais

    :param x: equivale ao tabuleiro
    :param y: 1 ou -1 (que equivalem as pecas X e O respetivamente)
    :return: posicao que levaria a um tres em linha
    '''
    a, b, c = 5, 1, 9
    pos3 = 0
    j = 1
    while j < 3:
        if obter_diagonal(x, j) == (y, y, 0):
            pos3 = c
        elif obter_diagonal(x, j) == (0, y, y):
            pos3 = b
        elif obter_diagonal(x, j) == (y, 0, y):
            pos3 = a
        c -= 6
        b += 6
        j += 1
    return pos3


def jogador_1(x, y):
    '''
    funcao auxiliar a funcao jogo_do_galo
    quando o jogador e o primeiro a jogar (escolheu X)
    cria um ciclo de tabuleiros que sao atualizados dependendo das jogadas feitas

    :param x: equivale ao tabuleiro
    :param y: dificuldade escolhida pelo jogador (basico ou normal ou perfeito)
    :return: X ou O ou EMPATE (depndendo se ha algum vencedor ou se empatam o jogo respetivamete)
    '''
    while obter_posicoes_livres(x) != ():
        jog, comp = 1, -1
        j = escolher_posicao_manual(x)
        x = marcar_posicao(x, jog, j)
        print(tabuleiro_str(x))
        if jogador_ganhador(x) == 1:
            return 'X'
        if obter_posicoes_livres(x) == ():
            return 'EMPATE'
        print('Turno do computador ' + "(" + y + "):")
        x = marcar_posicao(x, comp, escolher_posicao_auto(x, comp, y))
        print(tabuleiro_str(x))
        if jogador_ganhador(x) == -1:
            return 'O'


def jogador_2(x, y):
    '''
    funcao auxiliar a funcao jogo_do_galo
    quando o jogador e o segundo a jogar (escolheu O)
    cria um ciclo de tabuleiros que sao atualizados dependendo das jogadas feitas

    :param x: equivale ao tabuleiro
    :param y: dificuldade escolhida pelo jogador (basico ou normal ou perfeito)
    :return: X ou O ou EMPATE (depndendo se ha algum vencedor ou se empatam o jogo respetivamete)
    '''
    while obter_posicoes_livres(x) != ():
        jog, comp = -1, 1
        print('Turno do computador ' + "(" + y + "):")
        x = marcar_posicao(x, comp, escolher_posicao_auto(x, comp, y))
        print(tabuleiro_str(x))
        if jogador_ganhador(x) == 1:
            return 'X'
        if obter_posicoes_livres(x) == ():
            return 'EMPATE'
        j = escolher_posicao_manual(x)
        x = marcar_posicao(x, jog, j)
        print(tabuleiro_str(x))
        if jogador_ganhador(x) == -1:
            return 'O'
