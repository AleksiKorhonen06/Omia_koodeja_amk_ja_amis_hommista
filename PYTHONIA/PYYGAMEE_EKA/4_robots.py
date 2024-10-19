import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
window.blit(robot, (0, 0))
window.blit(robot, (590, 0))
window.blit(robot, (590, 390))
window.blit(robot, (0, 390))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()