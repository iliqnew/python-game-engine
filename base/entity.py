

class Entity:
    def __init__(self, name):
        self.name = name
        self.components = {}

    def add_component(self, component):
        component_type = type(component).__name__
        self.components[component_type] = component

