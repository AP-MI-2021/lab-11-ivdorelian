from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Route(Entity):
    id_start_city: str
    id_stop_city: str
    price: float
    return_route: bool
