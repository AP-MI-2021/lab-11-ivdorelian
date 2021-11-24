from dataclasses import dataclass

from Domain.city import City


@dataclass
class RouteWithCities:
    id_entity: str
    start_city: City
    stop_city: City
    price: float
    return_route: bool
