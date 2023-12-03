import time

from typing import List

from base.entity import Entity
from base.system import System


class GameEngine:
    entities: List[Entity] = []
    systems: List[System] = []

    def __init__(self) -> None:
        pass

    def run(self):
        self.start()
        start_time = end_time = time.time()

        while True:
            delta_time = end_time - start_time
            start_time = end_time
            self.update(delta_time)
            end_time = time.time()

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

    def update(self, delta_time):
        for system in self.systems:
            system.update(delta_time, self.entities)

