import pygame
import random
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

robot_x = 50  # Initial x-coordinate for the first robot

# Use a loop to display multiple robots in a row
for _ in range(1000):
    Y = random.randint(0, 390)
    X = random.randint(0, 590)
    window.blit(robot, (X, Y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
