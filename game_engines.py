from base.game_engine import GameEngine

from entities import (
    Entity,
)
from components import (
    Position2DComponent,
    Render2DComponent,
)
from systems import (
    Movement2DSystem,
    Render2DSystem,
)


class ExampleGameEngine(GameEngine):
    def __init__(self) -> None:
        # Example usage

        entity1 = Entity("Player")
        entity1.add_component(Render2DComponent("player_sprite.png"))
        entity1.add_component(Position2DComponent(10, 20))
        self.add_entity(entity1)

        entity2 = Entity("Enemy")
        entity2.add_component(Render2DComponent("enemy_sprite.png"))
        entity2.add_component(Position2DComponent(30, 40))
        self.add_entity(entity2)

        self.add_system(Render2DSystem())
        self.add_system(Movement2DSystem())

        super().__init__()