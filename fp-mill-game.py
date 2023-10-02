'''
Projeto 2 de FP 20/21 - Jogo Do Moinho

Joao Ponces de Carvalho   n-ist199091
'''

'''
TAD posicao
'''
def cria_posicao(col,lin):
    '''
    cria posicao segundo a representacao escolhida
    :param col: ccoluna
    :param lin: linha
    :return: representacao de posicao
    '''
    if type(col)!=str or type(lin)!= str or col not in ['a','b','c'] or lin not in ('1','2','3'):
        raise ValueError('cria_posicao: argumentos invalidos')
    return (col,lin)

def cria_copia_posicao(pos):
    '''
    copia qualquer posicao
    :param pos: posicao a copiar
    :return: posicao copiada
    '''
    return cria_posicao(obter_pos_c(pos),obter_pos_l(pos))

def obter_pos_c(pos):
    '''
    obtem a coluna de uma posicao
    :param pos: posicao
    :return: coluna
    '''
    return pos[0]

def obter_pos_l(pos):
    '''
    obtem a linha de uma posicao
    :param pos: posicao
    :return: linha
    '''
    return pos[1]

def eh_posicao(arg):
    '''
    reconhece a posicao
    :param arg: posicao
    :return: bool
    '''
    return type(arg)==tuple and len(arg)==2 and arg[0] in ['a','b','c'] and \
        arg[1] in ['1','2','3']

def posicoes_iguais(p1,p2):
    '''
    compara duas posicoes
    :param p1: primeira posicao
    :param p2: segunda posicao
    :return: bool
    '''
    return eh_posicao(p1) and eh_posicao(p2) and obter_pos_c(p1)==obter_pos_c(p2)\
        and obter_pos_l(p1)==obter_pos_l(p2)

def posicao_para_str(pos):
    '''
    tranforma uma posicao em string
    :param pos: posicao
    :return: string
    '''
    return obter_pos_c(pos)+obter_pos_l(pos)

def obter_posicoes_adjacentes(pos):
    '''
    indica as posicoes adjacentes a uma certa posicao
    :param pos: posicao
    :return: tuplo
    '''
    if obter_pos_c(pos)=='a':
        return obter_posicoes_adjacentes_c_a(pos)
    if obter_pos_c(pos)=='b':
        return obter_posicoes_adjacentes_c_b(pos)
    if obter_pos_c(pos)=='c':
        return obter_posicoes_adjacentes_c_c(pos)

def obter_posicoes_adjacentes_c_a (pos):
    '''
    auxilia a verificar as posicoes adjacentes das posicoes na coluna a
    :param pos: posicao
    :return: tuplo
    '''
    res,b2 = (),cria_posicao('b','2')
    if obter_pos_l(pos)=='1':
        res = (cria_posicao('b','1'),cria_posicao('a','2'),b2)
    if obter_pos_l(pos)=='2':
        res = (cria_posicao('a','1'),b2,cria_posicao('a','3'))
    if obter_pos_l(pos)=='3':
        res = (cria_posicao('a','2'),b2,cria_posicao('b','3'))
    return res

def obter_posicoes_adjacentes_c_b(pos):
    '''
    auxilia a verificar as posicoes adjacentes das posicoes na coluna b
    :param pos: posicao
    :return: tuplo
    '''
    res, b2= (), cria_posicao('b','2')
    if obter_pos_l(pos)=='1':
        res = (cria_posicao('a','1'),cria_posicao('c','1'),b2)
    if obter_pos_l(pos)=='2':
        res =(cria_posicao('a','1'),cria_posicao('b','1'),cria_posicao('c','1'),cria_posicao('a','2'),\
            cria_posicao('c','2'),cria_posicao('a','3'),cria_posicao('b','3'),cria_posicao('c','3'))
    if obter_pos_l(pos)=='3':
        res =(b2,cria_posicao('a','3'),cria_posicao('c','3'))
    return res

def obter_posicoes_adjacentes_c_c (pos):
    '''
    auxilia a verificar as posicoes adjacentes das posicoes na coluna a
    :param pos: posicao
    :return: tuplo
    '''
    res,b2= (),cria_posicao('b','2')
    if obter_pos_l(pos)=='1':
        res = (cria_posicao('b','1'),b2,cria_posicao('c','2'))
    if obter_pos_l(pos)=='2':
        res = (cria_posicao('c','1'),b2,cria_posicao('c','3'))
    if obter_pos_l(pos)=='3':
        res = (b2,cria_posicao('c','2'),cria_posicao('b','3'))
    return res

'''
TAD peca
'''
def cria_peca(x):
    '''
    cria peca segundo a representacao escolhida
    :param x: peca
    :return: representacao da peca
    '''
    if type(x)!= str or  x not in ['X','O',' ']:
        raise ValueError('cria_peca: argumento invalido')
    return str(x)

def cria_copia_peca(pec):
    '''
    cria uma copia da peca pretendida
    :param pec: peca
    :return: copia da peca
    '''
    return pec

def eh_peca(arg):
    '''
    reconhece peca
    :param arg: peca
    :return: bool
    '''
    return  type(arg)==str and len(arg)<=1 and arg in ['X','O',' ']

def pecas_iguais(pec1,pec2):
    '''
    compara dua pecas
    :param pec1: primeira peca
    :param pec2: segunda peca
    :return: bool
    '''
    return eh_peca(pec1) and eh_peca(pec2) and pec1==pec2

def peca_para_str(pec):
    '''
    reprenta a peca em string
    :param pec: peca
    :return: string
    '''
    return '['+pec+']'

def peca_para_inteiro(pec):
    '''
    muda a representacao da peca para inteiros
    :param pec: peca
    :return: 1 ou -1 ou 0
    '''
    return 1 if pec==cria_peca('X') else -1 if pec==cria_peca('O') else 0

'''
TAD tabuleiro
'''
def cria_tabuleiro():
    '''
    cria tabuleiro vazio na representacao escolhida
    :return: tabuleiro vazio
    '''
    tab = []
    for c in range(1,4):
        res = []
        for i in range(1,4):
           res += cria_peca(' ')
        tab += [res]
    return tab

def cria_copia_tabuleiro(t):
    '''
    cria copia do tabuleiro pretendido
    :param t: tabuleiro
    :return: copia do tabuleiro
    '''
    tab = []
    i = ('1','2','3')
    j = ('a','b','c')
    for c in range(0,3):
        res = []
        for l in range(0,3):
            res += cria_peca(obter_peca(t,cria_posicao(j[l],i[c])))
        tab += [res]
    return tab

def obter_vetor (t,s):
    '''
    obtem 1 dos 6 vetores do tabuleiro (linhas ou colunas)
    :param t: tabuleiro
    :param s: vetor pretendido ( 1,2,3,a,b ou c)
    :return: tuplo com as pecas do vetor
    '''
    return (t[0][0],t[1][0],t[2][0]) if s=='a' else (t[0][1],t[1][1],t[2][1]) if s=='b' else \
        (t[0][2],t[1][2],t[2][2]) if s == 'c' else (t[0][0],t[0][1],t[0][2]) if s =='1' else \
        (t[1][0], t[1][1], t[1][2]) if s =='2' else (t[2][0],t[2][1],t[2][2]) if s=='3' else ()

def obter_peca(t,p):
    '''
    obtem peca de qualquer posicao no tabuleiro
    :param t: tabuleiro
    :param p: posicao pretendida
    :return: peca
    '''
    if obter_pos_c(p)=='a':
        return t[0][0] if p==cria_posicao('a','1') else t[1][0] if p==cria_posicao('a','2') else t[2][0]
    if obter_pos_c(p)=='b':
        return t[0][1] if p==cria_posicao('b','1') else t[1][1] if p==cria_posicao('b','2') else t[2][1]
    if obter_pos_c(p)=='c':
        return t[0][2] if p==cria_posicao('c','1') else t[1][2] if p==cria_posicao('c','2') else t[2][2]

def coloca_peca(t,pec,pos):
    '''
    muda o tabuleiro colocando uma peca a escolha na posicao pretendida
    :param t: tabuleiro
    :param pec: peca a colocar
    :param pos: posicao ond se coloca a oeca
    :return: tabuleiro modificado
    '''
    t[ord(obter_pos_l(pos))-ord('1')][ord(obter_pos_c(pos))-ord('a')]=cria_peca(pec)
    return t

def remove_peca(t,pos):
    '''
    muda o tabuleiro removendo a peca da posicao pretendida
    :param t: tabuleiro
    :param pos: posicao a retirar a peca
    :return: tabuleiro modificado
    '''
    tuplo = ((0,0,0),(0,0,0),(0,0,0))
    t[ord(obter_pos_l(pos)) - ord('1')][ord(obter_pos_c(pos)) - ord('a')] = obter_peca(tuplo_para_tabuleiro(tuplo)\
        ,cria_posicao('a','1'))
    return t

def move_peca(t,pos1,pos2):
    '''
    move uma peca de uma posicao para outra
    :param t: tabuleiro
    :param pos1: posicao inicial da peca
    :param pos2: posicao final da peca
    :return: tabuleiro modificado
    '''
    pec_pos1 = obter_peca(t,pos1)
    t = remove_peca(t,pos1)
    return coloca_peca(t,pec_pos1,pos2)

def obter_posicoes_com_peca_de_jogs(t):
    '''
    funcao auxiliar que devolve todas as posicoes ocupadas por ambos os jogadores
    :param t: tabuleirp
    :return: tuplo
    '''
    lin , col, i , res  = ['1','2','3'] , ['a','b','c'], 0 , ()
    while i in range(0,3):
        j = 0
        while j in range(0,3):
            if obter_peca(t,cria_posicao(col[j],lin[i])) in (cria_peca('X'),cria_peca('O')):
                res += (cria_posicao(col[j],lin[i]),)
            j += 1
        i += 1
    return res

def eh_tabuleiro(arg):
    '''
    reconhece tabuleiro
    :param arg: tabuleiro
    :return: bool
    '''
    x, y = len(obter_posicoes_jogador(arg, cria_peca('X'))), len(obter_posicoes_jogador(arg, cria_peca('O')))
    if type(arg) != list or len(arg) != 3:
        return False
    for c in arg:
        if type(c) != list or len(c) != 3:
            return False
        for l in c:
            if l not in [cria_peca(' '), cria_peca('X'), cria_peca('O')]:
                return False
    if x + y > 6 or x > 3 or y > 3 or x - y >= 2 or y - x >= 2 or eh_tabuleiro_aux(arg) > 1:
        return False
    return True


def eh_tabuleiro_aux(t):
    '''
    funcao auxiliar ao eh_tabuleiro que verifica se existe mais de um jogador ganhador no tabuleiro
    :param t: tabuleiro
    :return: numero de jogadores ganhadores
    '''
    col, lin, res1, res2 = ['a', 'b', 'c'], ['1', '2', '3'], 0, 0
    for c in lin:
        if obter_vetor(t, c) == (cria_peca('X'), cria_peca('X'), cria_peca('X')) or obter_vetor(t, c) == (cria_peca\
        ('O'),cria_peca('O'), cria_peca('O')):
            res1 += 1
    for c in col:
        if obter_vetor(t, c) == (cria_peca('X'), cria_peca('X'), cria_peca('X')) or obter_vetor(t, c) == (cria_peca\
        ('O'),cria_peca('O'), cria_peca('O')):
            res2 += 1
    return res1 + res2

def eh_posicao_livre(t,pos):
    '''
    verifica se uma certa posicao e livre
    :param t: tabuleiro
    :param pos: posicao pretendida
    :return: bool
    '''
    tuplo = ((0,0,0),(0,0,0),(0,0,0))
    if obter_vetor(t,obter_pos_c(pos))[int(obter_pos_l(pos))-1] == \
            obter_peca(tuplo_para_tabuleiro(tuplo),cria_posicao('a','1')):
        return True
    return False

def tabuleiros_iguais(t1,t2):
    '''
    compara dois tabuleiros
    :param t1: primeiro tabuleiro
    :param t2: segundo tabuleiro
    :return: bool
    '''
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and obter_vetor(t1,'a')==obter_vetor(t2,'a') and \
           obter_vetor(t1, 'b') == obter_vetor(t2, 'b') and obter_vetor(t1,'c')==obter_vetor(t2,'c')

def tabuleiro_para_str(t):
    '''
    representacao do tabuleiro em string
    :param t: tabuleiro
    :return: string
    '''
    linha1,linha2,linha3  = obter_vetor(t,'1'),obter_vetor(t,'2'),obter_vetor(t,'3')
    inicio= '   a   b   c\n'
    linha1_tab ='1 '+peca_para_str(linha1[0])+'-'+peca_para_str(linha1[1])+'-'+peca_para_str(linha1[2])+'\n'
    linha_barras, linha_barras_2 ='   | \ | / |\n', '   | / | \ |\n'
    linha2_tab ='2 '+peca_para_str(linha2[0])+'-'+peca_para_str(linha2[1])+'-'+peca_para_str(linha2[2])+'\n'
    linha3_tab ='3 '+peca_para_str(linha3[0])+'-'+peca_para_str(linha3[1])+'-'+peca_para_str(linha3[2])
    return inicio+linha1_tab+linha_barras+linha2_tab+linha_barras_2+linha3_tab

def tuplo_para_tabuleiro(tup):
    '''
    representa um certo tuplo contendo 0,1 e -1 na representacao do tabuleiro escolhida
    :param tup: tuplo
    :return: tabuleiro
    '''
    tab = []
    for lin in tup :
        res = []
        for c in lin :
            if c == 1:
                res += ['X']
            elif c == -1:
                res += ['O']
            else :
                res += [' ']
        tab += [res]
    return tab

def obter_ganhador(t):
    '''
    devolve o jogador ganhador se este existir
    :param t: tabuleiro
    :return: jogador ganhador
    '''
    tuplo = ((0,0,0),(0,0,0),(0,0,0))
    if obter_vetor(t,'a')[0]==obter_vetor(t,'a')[1]==obter_vetor(t,'a')[2]!= cria_peca(' '):
        return obter_peca(t,cria_posicao('a','1'))
    elif obter_vetor(t,'b')[0]==obter_vetor(t,'b')[1]==obter_vetor(t,'b')[2]!= cria_peca(' '):
        return obter_peca(t,cria_posicao('b','1'))
    elif obter_vetor(t,'c')[0]==obter_vetor(t,'c')[1]==obter_vetor(t,'c')[2]!= cria_peca(' '):
        return obter_peca(t,cria_posicao('c','1'))
    elif obter_vetor(t,'1')[0]==obter_vetor(t,'1')[1]==obter_vetor(t,'1')[2]!= cria_peca(' '):
        return obter_peca(t,cria_posicao('a','1'))
    elif obter_vetor(t,'2')[0]==obter_vetor(t,'2')[1]==obter_vetor(t,'2')[2]!= cria_peca(' '):
        return obter_peca(t,cria_posicao('a','2'))
    elif obter_vetor(t,'3')[0]==obter_vetor(t,'3')[1]==obter_vetor(t,'3')[2]!= cria_peca(' '):
        return obter_peca(t,cria_posicao('a','3'))
    else :
        return obter_peca(tuplo_para_tabuleiro(tuplo),cria_posicao('a','1'))

def obter_posicoes_livres(t):
    '''
    obtem todas a posicoes livres no tabuleiro
    :param t: tabuleiro
    :return: tuplo
    '''
    lin , col, i , res  = ['1','2','3'], ['a','b','c'], 0 , ()
    while i in range(len(lin)):
        j = 0
        while j in range(len(col)):
            if eh_posicao_livre(t,cria_posicao(col[j],lin[i])):
                res += (cria_posicao(col[j],lin[i]),)
            j += 1
        i += 1
    return res

def obter_posicoes_jogador(tab,pec):
    '''
    obtem todas as posicoes ocupadas pelo jogador pretendido no tabuleiro
    :param tab: tabuleiro
    :param pec: jogador
    :return: tuplo
    '''
    lin, col, i, res = ['1', '2', '3'], ['a', 'b', 'c'], 0, ()
    while i in range(0, 3):
        j = 0
        while j in range(0, 3):
            if obter_peca(tab, cria_posicao(col[j], lin[i])) == cria_peca(pec):
                res += (cria_posicao(col[j],lin[i]),)
            j += 1
        i += 1
    return res
############################################################################
def obter_movimento_manual(t,pec):
    '''
    funcao que verifica a validade da jogada do jogador
    :param t: tabuleiro
    :param pec: peca do jogador
    :return: tuplo com posicoes , se estas forem validas
    '''
    pos_liv_str, res = tuple(posicao_para_str(p) for p in obter_posicoes_livres(t)), 0
    pos_jog_str = tuple(posicao_para_str(p) for p in obter_posicoes_com_peca_de_jogs(t))
    pos_com_pec = tuple(p for p in obter_posicoes_com_peca_de_jogs(t) if obter_peca(t, p) == pec)
    if len(obter_posicoes_com_peca_de_jogs(t)) < 6:
        esc = input('Turno do jogador. Escolha uma posicao: ')
        if len(esc) != 2 or esc not in pos_liv_str:
            raise ValueError('obter_movimento_manual: escolha invalida')
        return (cria_posicao(esc[0], esc[1]),)
    if len(obter_posicoes_com_peca_de_jogs(t)) == 6:
        esc = input('Turno do jogador. Escolha um movimento: ')
        pos_i, pos_f = esc[0] + esc[1], esc[2] + esc[3]
        if pos_i == pos_f:
            if len(esc) != 4 or (pos_i in pos_liv_str) or pos_i not in pos_jog_str or '[' + pec + ']' != peca_para_str\
                        (obter_peca(t, cria_posicao(esc[0], esc[1]))):
                raise ValueError('obter_movimento_manual: escolha invalida')
            for p in pos_com_pec:
                for c in obter_posicoes_adjacentes(p):
                    if c in obter_posicoes_livres(t):
                        res += 1
            if res >= 1:
                raise ValueError('obter_movimento_manual: escolha invalida')
            return (cria_posicao(esc[0], esc[1]), cria_posicao(esc[2], esc[3]))
        if len(esc) != 4 or pos_i not in pos_jog_str or '[' + pec + ']' != peca_para_str(obter_peca(t, cria_posicao \
                    (esc[0], esc[1]))) or pos_f not in pos_liv_str or cria_posicao(esc[2], esc[3]) not in \
                obter_posicoes_adjacentes(cria_posicao(esc[0], esc[1])):
            raise ValueError('obter_movimento_manual: escolha invalida')
        return (cria_posicao(esc[0], esc[1]), cria_posicao(esc[2], esc[3]))


def estrategia_1(tab,pec):
    '''
    estrategia que verifica se existe jogada possivel para a vitoria
    :param tab: tabuleiro
    :param pec: peca do jogador
    :return: tuplo com posicoes possiveis
    '''
    res= ()
    for p in obter_posicoes_livres(tab) :
        if obter_ganhador(coloca_peca(cria_copia_tabuleiro(tab),pec,p))== pec :
            res += (p,)
    return res

def estrategia_2(tab,pec):
    '''
    estrategia que verifica se existe jogada possivel para evitar a vitoria do adversario
    :param tab: tabuleiro
    :param pec: peca do jogador
    :return: tuplo com posicoes possiveis
    '''
    if pec == cria_peca('O'):
        jog = cria_peca('X')
    else :
        jog = cria_peca('O')
    res = ()
    for p in obter_posicoes_livres(tab):
        if obter_ganhador(coloca_peca(cria_copia_tabuleiro(tab),jog, p)) == jog:
            res += (p,)
    return res

def estrategia_3 (tab):
    '''
    verifica se a posicao do meio do tabuleiro esta livre
    :param tab: tabuleiro
    :return: tuplo com a posicao do meio se livre
    '''
    if eh_posicao_livre(tab,cria_posicao('b','2')):
        return (cria_posicao('b','2'),)
    else :
        return ()

def estrategia_4 (tab):
    '''
    verifica se os cantos estao livres pela ordem de leitura do tabuleiro
    :param tab: tabuleiro
    :return: tuplo com posicoes possiveis
    '''
    cantos,i = (cria_posicao('a','1'),cria_posicao('c','1'),cria_posicao('a','3'),cria_posicao('c','3')),0
    while i != 4 :
       if eh_posicao_livre(tab,cantos[i]):
            return (cantos[i],)
       i += 1
    return ()

def estrategia_5 (tab):
    '''
    verifica se as laterais estao livres pela ordem de leitura do tabuleiro
    :param tab: tabuleiro
    :return: tuplo com posicoes possiveis
    '''
    laterais,i = (cria_posicao('b','1'),cria_posicao('a','2'),cria_posicao('c','2'),cria_posicao('b','3')),0
    while i != 4 :
       if eh_posicao_livre(tab,laterais[i]):
            return (laterais[i],)
       i += 1
    return ()

def obter_movimento_auto (tab,pec,dific):
    '''
    determina a melhor jogada do computador de acordo com a dificulade escolhida
    :param tab: tabuleiro
    :param pec: peca do computador
    :param dific: dificuldade do computador
    :return: tuplo
    '''
    if dific == 'facil':
        return dific_facil(tab,pec)
    if dific == 'normal':
        return dific_normal(tab,pec)
    if dific == 'dificil':
        return dific_dificil(tab,pec)

def estrategias_colocacao(tab,pec):
    '''
    funcao auxiliar para a fase de colocacao das pecas ( 3 cada jogador)
    :param tab: tabuleiro
    :param pec: peca do compuardor
    :return: tuplo com posicao mais vantajosa
    '''
    if estrategia_1(tab,pec) != ():
         return estrategia_1(tab,pec)
    elif estrategia_2(tab,pec) != ():
         return estrategia_2(tab,pec)
    elif estrategia_3(tab)!= ():
        return estrategia_3(tab)
    elif estrategia_4(tab)!= ():
        return estrategia_4(tab)
    elif estrategia_5(tab)!= ():
        return estrategia_5(tab)

def escolha_mov_adj(tab,pec):
    '''
    funcao auxiliar para a fase de movimento das pecas (ate haver ganhador)
    :param tab: tabuleiro
    :param pec: peca do compuardor
    :return: tuplo com posicao mais vantajosa
    '''
    pos_jog,i= (),0
    pos_ocupadas = obter_posicoes_com_peca_de_jogs(tab)
    for c in pos_ocupadas :
        if obter_peca(tab,c) == pec :
            pos_jog+= (c,)
    while i != len(pos_jog):
        j = 0
        pos_adj_vaz = ()
        while j != len(obter_posicoes_adjacentes(pos_jog[i])):
            if obter_posicoes_adjacentes(pos_jog[i])[j] in obter_posicoes_livres(tab):
                pos_adj_vaz += (obter_posicoes_adjacentes(pos_jog[i])[j],)
            j += 1
        if pos_adj_vaz!= ():
            return (pos_jog[i],pos_adj_vaz[0])
        i +=1
    return (pos_jog[0],pos_jog[0])


def minimax(tab,pec,prof,seq_mov):
    '''
    algoritmo minimax
    :param tab: tabuleiro
    :param pec: peca do computador
    :param prof: profundidade de recursao
    :param seq_mov: sequancia de movimentos (inicialmente vazia)
    :return: tuplo com o jogador propenso a ganhar (1,-1 ou 0) e com todos os movimentos para que tal aconteca
    '''
    valor_tab = 1 if obter_ganhador(tab)== cria_peca('X') else -1 if obter_ganhador(tab)== cria_peca('O') else 0
    melhor_res,m_seq_mov = -1*valor_tab,()
    jog_op= cria_peca('X') if cria_peca(pec)== cria_peca('O') else cria_peca('O')
    if obter_ganhador(tab)!= cria_peca(' ') or prof==0:
        return valor_tab, seq_mov
    for p in tuple(pos for pos in obter_posicoes_com_peca_de_jogs(tab) if obter_peca(tab,pos)==pec):
        for a in obter_posicoes_adjacentes(p) :
            if a in obter_posicoes_livres(tab):
                tab_c = cria_copia_tabuleiro(tab)
                tab_c = move_peca(tab_c,p,a)
                novo_res , nova_seq_mov = minimax(tab_c,jog_op,prof-1,seq_mov+(p,a))
                if m_seq_mov == () or (cria_peca(pec)==cria_peca('X') and novo_res>melhor_res) or (cria_peca(pec)\
                    ==cria_peca('O') and novo_res<melhor_res):
                    melhor_res , m_seq_mov = novo_res , nova_seq_mov
    return melhor_res, m_seq_mov

def dific_facil(tab,pec):
    '''
    nivel de dificuldade facil
    :param tab: tabuleiro
    :param pec: peca do computador
    :return: tuplo coma melhor jogada
    '''
    if len(obter_posicoes_com_peca_de_jogs(tab))<6 :
        return estrategias_colocacao(tab,pec)
    if len(obter_posicoes_com_peca_de_jogs(tab))==6 :
        return escolha_mov_adj(tab,pec)

def dific_normal(tab,pec):
    '''
    nivel de dificuldade normal
    :param tab: tabuleiro
    :param pec: peca do computador
    :return: tuplo coma melhor jogada
    '''
    if len(obter_posicoes_com_peca_de_jogs(tab)) < 6:
        return estrategias_colocacao(tab, pec)
    if len(obter_posicoes_com_peca_de_jogs(tab)) == 6:
        mov = minimax(tab, pec, 1, ())
        return (mov[1][0], mov[1][1])

def dific_dificil(tab,pec):
    '''
    nivel de dificuldade dificil
    :param tab: tabuleiro
    :param pec: peca do computador
    :return: tuplo coma melhor jogada
    '''
    if len(obter_posicoes_com_peca_de_jogs(tab)) < 6:
        return estrategias_colocacao(tab, pec)
    if len(obter_posicoes_com_peca_de_jogs(tab)) == 6:
        mov = minimax(tab, pec, 5, ())
        return (mov[1][0], mov[1][1])

def moinho(pec,dific):
    '''
    funcao final que permite jogar o jogo final
    :param pec: peca que o jogador quer ([X] ou [O]
    :param dific: dificuldade do computador (facil, normal ou dificil)
    :return: jogo final
    '''
    if pec not in ('[X]','[O]') or dific not in ('facil','normal','dificil'):
        raise ValueError('moinho: argumentos invalidos')
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade '+dific+'.')
    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))
    if pec == '[X]':
        return jogador_primeiro(t,cria_peca('X'),dific)
    if pec == '[O]':
        return jogador_segundo(t,cria_peca('O'),dific)

def jogador_primeiro(t,pec,dific):
    '''
    funcao auxiliar para quando o jogdor escolhe a peca [X] e joga primeiro
    :param t: tabuleiro
    :param pec: peca do jogador
    :param dific: dificuldade do computador
    :return: jogo final
    '''
    comput = cria_peca('O')
    while len(obter_posicoes_com_peca_de_jogs(t))< 6 :
        turno_j = obter_movimento_manual(t,pec)
        t = coloca_peca(t,pec,turno_j[0])
        print(tabuleiro_para_str(t))
        if obter_ganhador(t)== pec :
            return peca_para_str(obter_ganhador(t))
        print("Turno do computador ("+dific+"):")
        print(tabuleiro_para_str(coloca_peca(t,comput,obter_movimento_auto(t,comput,dific)[0])))
        if obter_ganhador(t)== comput :
            return peca_para_str(obter_ganhador(t))
    while len(obter_posicoes_com_peca_de_jogs(t))== 6 :
        turno_j = obter_movimento_manual(t,pec)
        t = move_peca(t,turno_j[0],turno_j[1])
        print(tabuleiro_para_str(t))
        if obter_ganhador(t)== pec :
            return peca_para_str(obter_ganhador(t))
        print("Turno do computador ("+dific+"):")
        print(tabuleiro_para_str(move_peca(t,obter_movimento_auto(t,comput,dific)[0],obter_movimento_auto\
            (t,comput,dific)[1])))
        if obter_ganhador(t)== comput :
            return peca_para_str(obter_ganhador(t))

def jogador_segundo(t,pec,dific):
    '''
    funcao auxiliar para quando o jogdor escolhe a peca [O] e joga em segundo lugar
    :param t: tabuleiro
    :param pec: peca do jogador
    :param dific: dificuldade do computador
    :return: jogo final
    '''
    comput = cria_peca('X')
    while len(obter_posicoes_com_peca_de_jogs(t))< 6 :
        print("Turno do computador ("+dific+"):")
        print(tabuleiro_para_str(coloca_peca(t,comput,obter_movimento_auto(t,comput,dific)[0])))
        if obter_ganhador(t)== comput :
            return peca_para_str(obter_ganhador(t))
        turno_j = obter_movimento_manual(t, pec)
        t = coloca_peca(t, pec, turno_j[0])
        print(tabuleiro_para_str(t))
        if obter_ganhador(t) == pec:
            return peca_para_str(obter_ganhador(t))
    while len(obter_posicoes_com_peca_de_jogs(t))== 6 :
        print("Turno do computador ("+dific+"):")
        print(tabuleiro_para_str(move_peca(t,obter_movimento_auto(t,comput,dific)[0],obter_movimento_auto\
            (t,comput,dific)[1])))
        if obter_ganhador(t)== comput :
            return peca_para_str(obter_ganhador(t))
        turno_j = obter_movimento_manual(t, pec)
        t = move_peca(t, turno_j[0], turno_j[1])
        print(tabuleiro_para_str(t))
        if obter_ganhador(t) == pec:
            return peca_para_str(obter_ganhador(t))

moinho('[X]', 'facil')
