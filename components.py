from base.component import Component


class Render2DComponent(Component):
    def __init__(self, sprite):
        self.sprite = sprite


class Position2DComponent(Component):
    def __init__(self, x, y):
        self.x = x
        self.y = y

