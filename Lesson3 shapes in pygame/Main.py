import pygame
pygame.init()

screen= pygame.display.set_mode((600,600))
screen.fill("white")
pygame.display.update()

class Circle():
    def __init__(self,radius,colour,y,x,width):
        self.radius = radius
        self.colour = colour
        self.x = x
        self.y = y 
        self.width = width
        self.circle_surface = screen

    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.colour,(self.x,self.y),self.radius,self.width)

    def grow(self,r):
        self.radius = self.radius + r
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.colour,(self.x,self.y),self.radius,self.width)

circle = Circle(50,"Red",250,250,0)        




#Main game loop
running= True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            circle.draw()
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            circle.grow(20)
            pygame.display.update()












pygame.quit()

