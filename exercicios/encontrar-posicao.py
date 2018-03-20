

#
# @BEATRIZ : O Exercício será preencher esta função. A função deverá funcionar automaticamente
#            para várias situações diferentes que são testadas.
#            O código abaixo deste função é usado para desenhar o mapa nos vários testes e vai
#            chamar esta função para saber se o resultado é correcto. Vai acontecer algo muito
#            semelhante depois no jogo.
#
# Esta função recebe o Estado do jogo e a posição para onde o robô se quer mover. Ela deve devolver
# um valor booleano que significa se o robô pode realmente mover-se para a posição que quer. Se
# retornar verdadeiro é porque o robô pode mover-se. Se retornar falso é porque o robô não se pode
# mover para lá por causa de ter uma pedra lá ou estar fora do campo.
#
# Neste exercício a função vai receber um estado mais pequeno, mas igual ao jogo. Ao conseguires
# preencher esta função podes copiar o código para o jogo principal e fica tudo a funcionar.
#
# Um exemplo de estado que poderás receber é por exemplo:
# estado = {
#     linhas : 3,
#     colunas : 3,
#     robo : Unidade { posicao: (2,2) },
#     pedras : [
#         Unidade { posicao: (2,3) },
#         Unidade { posicao: (1,1) },
#         Unidade { posicao: (1,2) },
#         Unidade { posicao: (3,1) }
#     ]
# }
#
# A posição desejada é um tuplo de 2 valores que representa o eixo X e exio Y.
# posicaoDesejada = ( x , y )
#
#
def seraQueRoboPodeMover ( estado, posicaoDesejada ) :
    robo = estado['robo'] # Vamos fazer um atalho que referenciar o robo mais facilmente.
    podeMover = True # No final, vamos devolver esta variavel para saber se pode mover.


    # Esta versao inicial só está a testar se o robô sai fora do campo em direccao a norte.
    # De resto, vai dizer sempre, erradamente, que o robô se pode mover.
    yDesejado = posicaoDesejada[1]
    if ( yDesejado > estado['colunas'] ) :
        podeMover = False


    return podeMover;










# @Rafael
#
# No código seguinte vou definir um código que cria várias situações e depois pergunta a
# função "seraQueRoboPodeMover" se o robô se pode mover em cada uma das situações.
# O objectivo, é conseguires escrever um código inteligente que se consegue adaptar a qualquer
# situação que lhe é posta a frente.
#
# Ao correr estes testes podes avaliar o teu código e melhora-lo incrementalmente.




class Unidade () :
    def __init__ ( self, tipo, posicao ) :
        self.tipo = tipo
        self.posicao = posicao




# Desenha um mapa no terminal.
# Exemplo:
#   +-------+
#   | · # · |
#   | # R · |
#   | # · # |
#   +-------+
def desenharMapa ( estado ) :
    mapa = {}

    robo = estado['robo']
    mapa[ robo.posicao ] = robo

    for pedra in estado['pedras'] :
        mapa[ pedra.posicao ] = pedra

    print( '  +' + '--' * estado['colunas'] + '-+' )
    for y in range( estado['linhas'], 0, -1 ) :
        line = '  |';
        for x in range( 1, estado['colunas'] + 1, +1 ) :
            char = '·'
            if (x,y) in mapa and mapa[(x,y)].tipo == 'robo' :
                char = 'R'
            if (x,y) in mapa and mapa[(x,y)].tipo == 'pedra' :
                char = '#'
            line += ' ' + char
        line += ' |'
        print( line )
    print( '  +' + '--' * estado['colunas'] + '-+' )




# Definição dos estados para cada teste.
testes = [

    {
        'linhas' : 5,
        'colunas' : 5,
        'robo' : Unidade( 'robo', (4,3) ),
        'pedras' : [
            Unidade( 'pedra', (4,2) ),
            Unidade( 'pedra', (1,2) ),
            Unidade( 'pedra', (5,1) ),
            Unidade( 'pedra', (2,5) ),
            Unidade( 'pedra', (4,5) ),
            Unidade( 'pedra', (2,3) ),
            Unidade( 'pedra', (1,1) )
        ],
        'solucaoExercicio' : {
            'norte': True,
            'este': True,
            'sul': False,
            'oeste': True
        }
    },

    {
        'linhas' : 3,
        'colunas' : 3,
        'robo' : Unidade( 'robo', (2,2) ),
        'pedras' : [
            Unidade( 'pedra', (2,3) ),
            Unidade( 'pedra', (1,1) ),
            Unidade( 'pedra', (1,2) ),
            Unidade( 'pedra', (3,1) )
        ],
        'solucaoExercicio' : {
            'norte': False,
            'este': True,
            'sul': True,
            'oeste': False
        }
    },

    {
        'linhas' : 2,
        'colunas' : 2,
        'robo' : Unidade( 'robo', (1,1) ),
        'pedras' : [
            Unidade( 'pedra', (1,2) )
        ],
        'solucaoExercicio' : {
            'norte': False,
            'este': True,
            'sul': False,
            'oeste': False
        }
    },

    {
        'linhas' : 3,
        'colunas' : 3,
        'robo' : Unidade( 'robo', (3,3) ),
        'pedras' : [
            Unidade( 'pedra', (2,2) ),
            Unidade( 'pedra', (3,2) ),
            Unidade( 'pedra', (2,3) )
        ],
        'solucaoExercicio' : {
            'norte': False,
            'este': False,
            'sul': False,
            'oeste': False
        }
    },

    {
        'linhas' : 6,
        'colunas' : 6,
        'robo' : Unidade( 'robo', (3,1) ),
        'pedras' : [
            Unidade( 'pedra', (2,5) )
        ],
        'solucaoExercicio' : {
            'norte': True,
            'este': True,
            'sul': False,
            'oeste': True
        }
    }

]




def sumtups ( t1, t2 ) :
    output = tuple( x + y for x, y in zip(t1, t2) )
    # print("t1 = " + str(t1))
    # print("t2 = " + str(t2))
    # print("zip(t1+t2) = " + str(list(zip(t1, t2))))
    # print("output = " + str(output))
    return output



direccoes = [
    { 'nome': 'norte', 'mod' : (0,1)  },
    { 'nome': 'este',  'mod' : (1,0)  },
    { 'nome': 'sul',   'mod' : (0,-1) },
    { 'nome': 'oeste', 'mod' : (-1,0) }
]


# Correr cada teste um-a-um.
# Em cada teste o robô vai estar no estado definido pelo teste e vai tentar depois ir para as
# diversas direcções: norte, este, sul, oeste.
numTeste = 0
totalCertos = 0
for teste in testes :
    numTeste += 1
    robo = teste['robo']
    certos = 0


    print()
    print()
    print( "Iniciar teste " + str(numTeste) + " com seguinte mapa:" )
    desenharMapa( teste )
    print( "  O Robo começa sempre na posição ( %d , %d )." % robo.posicao )


    # Vai testar cada uma das quatro direcções.
    for direccao in direccoes :
        posicaoDesejada = sumtups( robo.posicao, direccao['mod'] )
        print(
            "    Vai tentar ir para '%s', para ( %d , %d )."
            % ( (direccao['nome'],) + sumtups( robo.posicao, direccao['mod'] ) )
        )
        podeMover = seraQueRoboPodeMover( teste, posicaoDesejada )
        if podeMover :
            print("      A função disse que o robo se pode mover.")
        if not podeMover :
            print("      A função não permitiu ao robo de se mover.")


        # Avaliar o resultado pretendido para esta direção.
        if podeMover == teste['solucaoExercicio'][ direccao['nome'] ] :
            certos += 1
            print("      CERTO")
        else :
            print("      INCORRECTO")


    # Mostrar uma pontuação deste teste.
    totalCertos += certos
    print("  Resultado do Teste: [" + "##" * certos + "  " * (4-certos) + "] " + str(certos) + " em 4")


# Mostrar um total para todos os testes:
print()
print()
print(
    "RESULTADO FINAL: ["
    + "##" * totalCertos
    + "  " * ( numTeste * 4 - totalCertos )
    + "] " + str( totalCertos / ( numTeste * 4 ) * 100 ) + "%"
)
print()
print()
print()
print()
print()
