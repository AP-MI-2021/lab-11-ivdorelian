import json
from typing import List

from Domain.route import Route
from Repository.repository import Repository
from ViewModels.route_with_cities import RouteWithCities


class RoutesService:
    def __init__(self,
                 routes_repository: Repository,
                 city_repository: Repository):
        """
        Creeaza un service pentru rute.
        :param routes_repository: repository
               care retine rute.
        :param city_repository: repository
               pentru localitati
        """
        self.routes_repository = routes_repository
        self.city_repository = city_repository

    def add_route(self,
                  id_route: str,
                  id_start_city: str,
                  id_stop_city: str,
                  price: float,
                  return_route: bool):
        """
        Adauga o ruta.
        :param id_route: id-ul rutei
        :param id_start_city: id-ul orasului de pornire,
        diferit de id_start_city
        :param id_stop_city: id-ul orasului de sosire,
        diferit de id_stop_city
        :param price: pretul
        :param return_route: daca e dus-intors
        :return:
        """
        route = Route(id_route,
                      id_start_city,
                      id_stop_city,
                      price,
                      return_route)
        errors = []
        if self.city_repository.read(id_start_city) is None:
            errors.append(f'Nu exista oras cu id-ul {id_start_city}')
        if self.city_repository.read(id_stop_city) is None:
            errors.append(f'Nu exista oras cu id-ul {id_stop_city}')
        if id_stop_city == id_start_city:
            errors.append('id-urile oraselor de pornire si sosire '
                          'nu pot fi egale!')
        if errors:
            raise ValueError(errors)
        self.routes_repository.create(route)

    def get_all(self) -> List[Route]:
        """
        :return: o lista cu toate rutele
        """
        return self.routes_repository.read()

    def get_cities_ordered_by_return_routes(self):
        """
        :return: un tuple format dintr-o lista
        cu localitatile ordonate dupa
        numarul de rute dus-intors care pornesc din ele
        si numarul acestor rute
        """
        result = []
        routes = self.routes_repository.read()
        for city in self.city_repository.read():
            routes_from_city = [route for route in routes
                                if route.id_start_city == city.id_entity and
                                route.return_route]
            result.append((city, len(routes_from_city)))

        return sorted(result, key=lambda x: x[1])

    def get_routes_stoping_in_a_municipiu(self) -> List[RouteWithCities]:
        """
        :return: o lista cu rutele care se opresc intr-o localitate municipiu.
        """
        result = []
        for route in self.routes_repository.read():
            route_with_cities = RouteWithCities(
                route.id_entity,
                self.city_repository.read(route.id_start_city),
                self.city_repository.read(route.id_stop_city),
                route.price,
                route.return_route
            )
            if route_with_cities.stop_city.type == 'municipiu':
                result.append(route_with_cities)

        return result

    def export_json(self, export_filename):
        """
        Exporta  un fișier JSON cu un obiect în care cheile sunt
        numele localităților, iar valoarea unei chei X este o listă
        cu numele localităților în care ajung direct autocare care
        pornesc din X.
        :param export_filename: numele fisierului in case se exporta.
        """
        result = {}
        routes = self.routes_repository.read()
        for city in self.city_repository.read():
            ids_from_city = [route.id_stop_city for route in routes
                             if route.id_start_city == city.id_entity]
            result[city.name] = [self.city_repository.read(id_stop_city).name
                                 for id_stop_city in ids_from_city]

        with open(export_filename, 'w') as f:
            json.dump(result, f, indent=2)
