import cocos
import pyglet




class CampoDeJogo (cocos.layer.Layer):


    def __init__ ( self ) :
        super( CampoDeJogo, self ).__init__()

        self.robot = cocos.sprite.Sprite("robot-pixelart.png")
        self.robot.position = 320,240
        self.add( self.robot, z=1 )



cocos.director.director.init( resizable=True)

campo1 = CampoDeJogo()
main_scene = cocos.scene.Scene ( campo1 )


cocos.director.director.run( main_scene )
