import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

robot_x = 50  # Initial x-coordinate for the first robot

# Use a loop to display multiple robots in a row
for _ in range(10):
    window.blit(robot, (robot_x, 190))
    robot_x += 50  # Increase x-coordinate for the next robot

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
