from Repository.json_repository import JsonRepository
from Service.routes_service import RoutesService
from Utils.clear_file import clear_file


def test_export_json():
    routes_filename = 'test_routes.json'
    cities_filename = 'test_cities.json'

    routes_repository = JsonRepository(routes_filename)
    city_repository = JsonRepository(cities_filename)

    routes_service = RoutesService(routes_repository, city_repository)

    routes_service.export_json('test_export.json')

    try:
        with open('test_export.json', 'r'):
            pass
        assert True
    except Exception:
        assert False
