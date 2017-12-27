##
# O Teclado é a entidade que vai receber os inputs do utilizador
# e depois passa-los ao jogo.
# Em cocos, o input tem que passar por eventos de uma Layer, por
# isso não pode ficar directamente no jogo (que é uma Scene).
#


import cocos




class Teclado ( cocos.layer.Layer ) :




    def __init__ ( self, jogo ) :
        super( Teclado, self ).__init__()
        self.jogo = jogo # Precisa de conseguir chamar coisas do jogo




    # Necessário para o cocos, para que este objecto receba os eventos
    # do teclado, tal como pressionar um botão.
    is_event_handler = True




    # This function is called when a key is pressed.
    # 'key' is a constant indicating which key was pressed.
    # 'modifiers' is a bitwise or of several constants indicating which
    # modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
    def on_key_press (self, key, modifiers):
        print( "Pressed key {0}".format(key) )

        if ( key == 65362 ) : # UP
            self.jogo.moverRobo( (0,+1) )

        elif ( key == 65361 ) : # LEFT
            self.jogo.moverRobo( (-1,0) )

        elif ( key == 65364 ) : # DOWN
            self.jogo.moverRobo( (0,-1) )

        elif ( key == 65363 ) : # RIGHT
            self.jogo.moverRobo( (+1,0) )
