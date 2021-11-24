from Domain.city_validator import CityValidator
from Repository.json_repository import JsonRepository
from Service.city_service import CityService
from Service.routes_service import RoutesService
from Tests.test_routes_service import test_export_json
from UserInterface.console import Console


def main():
    city_repository = JsonRepository('cities.json')
    routes_repository = JsonRepository('routes.json')

    city_validator = CityValidator()

    city_service = CityService(city_repository, city_validator)
    routes_service = RoutesService(routes_repository, city_repository)

    console = Console(city_service, routes_service)
    console.run_console()


if __name__ == '__main__':
    test_export_json()
    main()
