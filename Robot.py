class Robot:
    def __init__(self, arg1, arg2):
        self.nome = arg1
        self.posicao = arg2

    def moverparacima(self):
        self.posicao = ( self.posicao[0] - 3, self.posicao[1] )


    def gritarnome(self):
        print "o meu nome e " + self.nome
        print "a minha posicao e " + str (self.posicao)


r1 = Robot( "fala",(2, 3) )
r1.gritarnome()
r1.moverparacima()
r1.gritarnome()

r2d2 = Robot("cala", (7, 8) )
r2d2.gritarnome()
