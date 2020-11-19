import Classes
from variables import *

p.init()

pendulum = Classes.Pendulum(40, 600, w, h)

running = True
while running:

    clock.tick(60)

    s.fill((0, 0, 0))
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
        if event.type == p.KEYDOWN:
            if event.key == p.K_ESCAPE:
                running = False

    pendulum.calculate_pos()
    p.display.update()
