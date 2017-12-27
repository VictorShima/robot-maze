##
# O 'main' é o ponto de entrada para o programa.
# É responsável por inicializar os mecanismos do cocos e de
# inicializar o jogo.
##


import cocos
from jogo import Jogo


cocos.director.director.init( resizable = True )
meuJogo = Jogo()
cocos.director.director.run( meuJogo )
