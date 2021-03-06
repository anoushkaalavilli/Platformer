"""
platformer.py
Author: Anoushka Alavilli
Credit: Sarah Dunbar, Jasmine Lou, Dina Hertog-Raz, Mr. Dennison, http://brythonserver.github.io/ggame/#ggame.Sprite.collidingWithSprites
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

darkblue= Color(0x0000CD, 1.0)
black= Color(0x000000, 1.0)
turquoise= Color(0x58FAD0, 1.0)
red= Color(0xFF0000, 1.0)

thinline = LineStyle(3, turquoise)
noline= LineStyle(0, black)


SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

class Spring(Sprite):
    block = RectangleAsset(40, 25, thinline, darkblue)
    def __init__(self, xval, yval):
        super().__init__(Spring.block, (xval, yval))
        self.x = xval
        self.y = yval

class Block(Sprite):
    block= RectangleAsset(80, 65, thinline, darkblue)
    def __init__(self, xval, yval):
        super().__init__(Block.block, (xval, yval))
        self.x = xval
        self.y = yval

ocean= Color(0xA9BCF5, 0.75)
yval= 0
xval= 0
charactersprite = None
springsprite = None
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, ocean)
bg = Sprite(bg_asset, (0,0))



def classblock(event):
    global xval, yval
    x = xval - xval%80
    y = yval - yval%65
    Block(x-40, y-32.5)
    
def classspring(event):
    springgravity = 0
    global xval, yval
    global springsprite
    springsprite = Spring(xval, yval)

class Character(Sprite):
    character= RectangleAsset(40, 80, thinline, red)
    def __init__(self, xval, yval):
        super().__init__(Character.character, (xval, yval))
        self.x = xval
        self.y = yval

def classcharacter(event):
    gravity = 0
    global xval, yval
    global charactersprite
    x = xval
    y = yval
    if charactersprite:
        charactersprite.destroy()
    charactersprite = Character(x, y)



"""
def classcharacter(event):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__(Character.character, (xval, yval))
        xval = 0
        yval = 0
        self.listenKeyEvent('keydown', 'right arrow', self.MoveCharacterRight)
        self.listenKeyEvent('keydown', 'left arrow', self.MoveCharacterLeft)
        self.listenKeyEvent('keydown', 'up arrow', self.MoveCharacterUp)
"""

def MoveCharacterRight (event):
    if charactersprite:
        charactersprite.x += 5
        collision = charactersprite.collidingWithSprites(Block)
        if collision:
            charactersprite.x -= 5
    
def MoveCharacterLeft (event):
    if charactersprite:
        charactersprite.x -= 5
        collision = charactersprite.collidingWithSprites(Block)
        if collision:
            charactersprite.x += 5

def MoveCharacterUp (event):
    global gravity
    if charactersprite:
        gravity = -5
        
        '''
        charactersprite.y -= 5
        collision = charactersprite.collidingWithSprites(Block)
        if collision:
            charactersprite.y += 5
    
        '''
def mousemove(event):
    global xval, yval
    xval = event.x
    yval = event.y
    

gravity= 0
springgravity = 0

#Block(55, 250)
#Block(300, 250)


class Platformer(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        
    def step(self):
        global gravity
        if charactersprite:
            gravity += 0.15
            charactersprite.y += gravity
            collision = charactersprite.collidingWithSprites(Block)
            characterspringcollision = charactersprite.collidingWithSprites(Spring)
            if characterspringcollision:
                gravity = -10
            if collision:
                #gravity -= 0.15
                charactersprite.y -= gravity
                gravity= 0
            if not collision:
                gravity += 0.15
        global springgravity
        if springsprite:
            springcollision = springsprite.collidingWithSprites(Block)
            if not springcollision:
                springgravity += 0.15
                springsprite.y += springgravity


        
myapp= Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)

myapp.listenKeyEvent('keydown', 'w', classblock)
myapp.listenKeyEvent('keydown', 'p', classcharacter)
myapp.listenMouseEvent('mousemove', mousemove)
myapp.listenKeyEvent('keydown', 'right arrow', MoveCharacterRight)
myapp.listenKeyEvent('keydown', 'left arrow', MoveCharacterLeft)
myapp.listenKeyEvent('keydown', 'up arrow', MoveCharacterUp)
myapp.listenKeyEvent('keydown', 's', classspring)
myapp.listenMouseEvent
myapp.run()