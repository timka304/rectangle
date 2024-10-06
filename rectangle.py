import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill("white")

class Rectangle():
    #properties

    #constructor
    def __init__(self, color, dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions = dimensions
    #functions
    def draw(self):
        self.Draw_rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

#creating instances/objects
red_rect = Rectangle("red", (50, 20, 100, 100))
blue_rect = Rectangle("blue", (500, 300, 150, 50))
green_rect = Rectangle("green", (350, 150, 50, 25))

#Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #accessing methods to draw rectangles 
    red_rect.draw()
    blue_rect.draw()
    green_rect.draw()
    #Display update to reflect the things on screeen


    pygame.display.update()

pygame.quit()