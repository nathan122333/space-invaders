import pygame
class Effect:
    def __init__(self ,x ,y):
        self.current=0
        self.time=0
        self.x=x
        self.y=y
        self.image=pygame.image.load(r"C:\Users\Nathan Kimani\Desktop\game\Nathan-main\Nathan-main\Free Smoke Fx  Pixel 04.png")
        self.allimage=[]
        self.heigh=64
        self.width=64
        self.total_image=7
        for i in range(7):
            small_image=self.image.subsurface(i*self.width,7*64,64,64)
            self.allimage.append(small_image)


    def show(self,screan):
        if self.time>1:
            self.current=self.current+1
            self.time=0
        self.time=self.time + 0.15
        if self.current > 6:
            return
        screan.blit(self.allimage[self.current],(self.x,self.y))




















































































