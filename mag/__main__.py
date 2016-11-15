import cocos
import pyglet

from cocos.actions import *
from cocos.director import director
from cocos import audio

class Stage(cocos.layer.Layer):
    
    is_event_handler = True

    
    def __init__(self):
    
        super(Stage, self).__init__()
        self.obstacle = []
        self.obstacle.append((200, 300, -1))
        self.obstacle.append((400, 500, 1))
        self.obstacle.append((600, 700, -1))
        self.player = (500, 300, 1)
        self.F = (0, 0)
        self.globalK = 50000
        self.schedule(self.update)
        
        self.redImage = pyglet.image.load('mag/red.png')
        self.blueImage = pyglet.image.load('mag/blue.png')
        
        self.o1 = cocos.sprite.Sprite('blue.png')
        self.o1.x = 200
        self.o1.y = 300
        self.add(self.o1)
        
        self.o2 = cocos.sprite.Sprite('red.png')
        self.o2.x = 400
        self.o2.y = 500
        self.add(self.o2)
        
        self.o3 = cocos.sprite.Sprite('blue.png')
        self.o3.x = 600
        self.o3.y = 700
        self.add(self.o3)
        
        
        self.playersprite = cocos.sprite.Sprite('red.png')
        self.playersprite.x = 500
        self.playersprite.y = 300
        self.add(self.playersprite)
        
    def update(self, dt):
        playerx, playery, playerq = self.player
        Fx, Fy = self.F
        for obs in self.obstacle:
            obsx, obsy, obsq = obs
            dx = obsx-playerx
            dy = obsy-playery
            d = (dx**2+dy**2)**0.5
            Ftot = -obsq*playerq/(d**2)
            Fx += Ftot * dx / d * self.globalK * dt
            Fy += Ftot * dy / d * self.globalK * dt
        playerx += Fx
        playery += Fy
        #print(playerx)
        #print(playery)
        
        self.playersprite.x = playerx
        self.playersprite.y = playery
        self.player = (playerx, playery, playerq)
        self.F = (Fx, Fy)
    
    
    def on_key_press(self, key, modifiers):
        if key == 32:
            a, b, c = self.player
            self.player = a, b, -c
            if c == 1:
                self.playersprite.image = self.blueImage
            else:
                self.playersprite.image = self.redImage

def main():
    director.init(width = 1024, height = 768, resizable = False, caption = "Project MAG")

    
    StageFrame = Stage()
    
    scene = cocos.scene.Scene()
    scene.add(StageFrame)
    director.run(scene)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    