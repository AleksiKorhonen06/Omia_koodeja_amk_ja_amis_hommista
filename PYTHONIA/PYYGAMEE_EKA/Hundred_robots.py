import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
a_x = 50
a_y = 100
robot_x = 50  
robot_y = 100


for _ in range(10):
    robot_x = a_x
    for _ in range(10):
        window.blit(robot, (robot_x, robot_y))
        robot_x += 40  
        a_x += 1
    a_y += 25
    robot_y = a_y
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
