from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class City(Entity):
    name: str
    type: str
