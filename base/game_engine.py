from base.entity import Entity
from base.system import System

class GameEngine:
    entities = []
    systems = []

    def __init__(self) -> None:
        pass

    def run(self):
        self.start()
        while True:
            self.update()

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def remove_entity(self, entity: Entity):
        self.entities.remove(entity)

    def add_system(self, system: System):
        self.systems.append(system)

    def remove_system(self, system: System):
        self.systems.remove(system)

    def start(self):
        pass

    def update(self):
        for system in self.systems:
            system.update(self.entities)

