import pygame
## player 

class Player:
    def __init__(self,x,y,size,speed):
        self.x=x
        self.y=y
        self.size=size
        self.speed=speed

    def move(self,keys):
        if keys[pygame.K_LEFT]:
            self.x -=self.speed
        if keys[pygame.K_RIGHT]:
            self.x +=self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y +=self.speed

    def stay_in_bounds(self,width,height):
        if self.x <0:
            self.x=0
        if self.x > width - self.size:
            self.x=width- self.size
        if self.y <0:
            self.y=0
        if self.y > height - self.size:
            self.y= height - self.size

    def draw(self,screen):
        pygame.draw.rect(screen,(0,0,255),(self.x,self.y, self.size,self.size))
        