from base.system import System


class Render2DSystem(System):
    def update(self, entities):
        for entity in entities:
            if "Render2DComponent" in entity.components:
                render = entity.components["Render2DComponent"]
                print(f"Rendering {entity.name} with sprite: {render.sprite}")


class Movement2DSystem:
    def update(self, entities):
        for entity in entities:
            if "Position2DComponent" in entity.components:
                position = entity.components["Position2DComponent"]
                print(f"Moving {entity.name} to ({position.x}, {position.y})")

