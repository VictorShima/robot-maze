# definicoes de coisas
import sys
import random

def print_char(c):
    sys.stdout.write(c)
    sys.stdout.flush()

# zona nao configuravel

def mostrarecra():
    print "Pontuacao: ", pontos
    for l in range (1, linhas + 1):
        for c in range (1, colunas + 1):

            #print_char("  ("+str(l)+","+str(c)+")")

            if (l == linharobot and c == colunarobot ):
                print_char ("R")

            elif (l == linhafinal and c == colunafinal):
                print_char ("X")

            elif ((l,c) in conjuntodepedras):
                print_char ("#")

            elif ((l,c) in conjuntodepontos and conjuntodepontos[(l,c)] == 1) :
                print_char ("!")

            else :
                print_char (".")


        print_char("\n")


def inputteclado():
    direcao = (raw_input ( "Para onde quer andar: " ))
    return direcao

def moverrobot ( paraonde ):
    global linharobot
    global colunarobot
    global linhas
    global colunas
    global conjuntodepontos
    global pontos
    print "eu vou para " + paraonde

    if (paraonde == "w") and (linharobot != 1) and ((linharobot-1, colunarobot) not in conjuntodepedras):
        linharobot = linharobot - 1

    if (paraonde == "a") and (colunarobot != 1) and ((linharobot, colunarobot -1) not in conjuntodepedras):
        colunarobot = colunarobot - 1

    if (paraonde == "s") and (linharobot != linhas) and ((linharobot+1, colunarobot) not in conjuntodepedras):
        linharobot = linharobot + 1

    if (paraonde == "d") and colunarobot != colunas and ((linharobot, colunarobot+1) not in conjuntodepedras):
        colunarobot = colunarobot + 1

    if ( (linharobot,colunarobot) in conjuntodepontos and conjuntodepontos[(linharobot,colunarobot)] == 1) :
        conjuntodepontos[(linharobot,colunarobot)] = 0
        pontos = pontos+1


#zona configuravel

file = open("informacao_inicial.txt", "r")
content = file.read()
tokens = content.split()

#Extrat map size
linhas = int( tokens[0] )
colunas = int( tokens [1])

linharobot = int (tokens[2])
colunarobot = int(tokens[3])


linhafinal = int (tokens[4])
colunafinal = int (tokens[5])

npedras = int (tokens [6])
npontos = int (tokens [7])

conjuntodepedras = {}
for l in range (1, npedras + 1):
    linhapedra = random.randint(1, linhas)
    colunapedra = random.randint(1, colunas)
    conjuntodepedras[(linhapedra,colunapedra)] = 1

conjuntodepontos = {}
for l in range (1, npontos + 1):
    linhaponto = random.randint(1, linhas)
    colunaponto = random.randint(1, colunas)
    conjuntodepontos[(linhaponto,colunaponto)] = 1

pontos = 0

mostrarecra()

while True :

    opcao1 = inputteclado()

    moverrobot( opcao1 )

    mostrarecra()

    if (colunarobot == colunafinal and linharobot == linhafinal):

        break

print "Congratulations!!! Pontos = ",pontos
