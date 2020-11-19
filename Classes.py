from variables import *


class Pendulum:
    def __init__(self, max_angle, length):
        self.max_angle = max_angle
        self.length = length
        self.point = v(w / 2, h / 20)
        self.radius = 20
        self.T = 2 * math.pi * math.sqrt(self.length / 10)

    def X(self, t):
        return self.max_angle * math.sin(2 * math.pi * t / self.T)

    def calculate_pos(self):
        # calculate angle and convert it to radians
        x = self.X(p.time.get_ticks() / 60) * 0.0174532925  # 60 is the fps
        pos = v(self.point.x + math.sin(x) * self.length,
                self.point.y + math.cos(x) * self.length)

        self.draw(pos, self.point)

    def draw(self, pos, point):
        p.draw.line(s, (255, 255, 255), point, pos)
        p.draw.circle(s, (255, 0, 255), point, 5)
        p.draw.circle(s, (255, 255, 255), pos, self.radius)
