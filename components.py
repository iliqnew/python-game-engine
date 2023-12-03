from base.component import Component
import numpy as np

class Render2DComponent(Component):
    def __init__(self, sprite):
        self.sprite = sprite


class Position2DComponent(Component):
    def __init__(self, x, y):
        self.pos = np.array([x, y])
        self.__velocity = np.zeros(2)

    def set_x(self, x: float):
        self.pos[0] = x - self.pos[0]

    def set_y(self, y: float):
        self.pos[1] = y - self.pos[1]
    
    def set_pos(self, pos: np.ndarray):
        self.pos = pos

    def set_velocity(self, velocity: np.ndarray):
        self.__velocity = velocity

    def update(self):
        self.pos += self.__velocity
        self.__velocity = np.zeros(2)

