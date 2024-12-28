import pygame
pygame.init()
s_width = 600
s_height = 600
screen= pygame.display.set_mode((s_width,s_height))
screen.fill("white")
pygame.display.update()

class Rectangle:
    def __init__(self, width, height, colour, x, y):
        self.width = width
        self.height = height
        self.colour = colour
        self.x = x
        self.y = y
        self.x = (s_width-width)//2
        self.y = (s_height-height)//2
        self.surface = screen

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, (self.x, self.y, self.width, self.height))

    def resize(self, dw, dh):
        self.x -= dw//2
        self.y -= dh//2
        self.width += dw
        self.height += dh

rectangle = Rectangle(100, 50, (255, 0, 0), 200, 200)

#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            rectangle.draw()
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            rectangle.resize(50, 50) 
            screen.fill((255, 255, 255))  
            rectangle.draw()
            pygame.display.update()

pygame.quit()

