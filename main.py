import pygame
from piano import Piano
from note import notes
import winsound


size = width, height = 1200, 600

piano = Piano(position=(2,20), white_size=(30,250),black_size=(25,160), margin=2)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Piano')

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont('Arial', 13)

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(piano.get_note_by_pos(event.pos))
    
    screen.fill((0,0,0))

    piano.show(screen, font)

    pygame.display.update()
    clock.tick(60)