from Service.city_service import CityService
from Service.routes_service import RoutesService


class Console:
    def __init__(self,
                 city_service: CityService,
                 routes_service: RoutesService):
        self.city_service = city_service
        self.routes_service = routes_service

    def show_menu(self):
        print('1. Adauga localitate')
        print('2. Adauga ruta autocar')
        print('sl. Afiseaza localitatile')
        print('sr. Afiseaza rutele')
        print('3. Afisare localitati ordonate dupa '
              'nr. de rute dus-intors care '
              'pornesc din ele')
        print('4. Afisarea rutelor care se opresc '
              'intr-o localitate municipiu')
        print('5. Export JSON')
        print('x. Exit')

    def run_console(self):

        while True:
            self.show_menu()
            opt = input('Optiunea: ')

            if opt == '1':
                self.handle_add_city()
            elif opt == 'sl':
                self.handle_show_all(self.city_service.get_all())
            elif opt == '2':
                self.handle_add_route()
            elif opt == 'sr':
                self.handle_show_all(self.routes_service.get_all())
            elif opt == '3':
                self.handle_show_all(
                    self.routes_service.get_cities_ordered_by_return_routes())
            elif opt == '4':
                self.handle_show_all(
                    self.routes_service.get_routes_stoping_in_a_municipiu())
            elif opt == '5':
                self.handle_export()
            elif opt == 'x':
                break
            else:
                print('Optiune invalida.')

    def handle_add_city(self):
        try:
            id_city = input('Id-ul localitatii: ')
            name = input('Numele localitatii: ')
            type = input('Tipul localitatii (sat, oras, municipiu): ')

            self.city_service.add_city(id_city, name, type)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_show_all(self, entities):
        for entity in entities:
            print(entity)

    def handle_add_route(self):
        try:
            id_route = input('Id-ul rutei: ')
            id_start_city = input('Id-ul orasului de pornire: ')
            id_stop_city = input('Id-ul orasului de sosire: ')
            price = float(input('Pretul: '))
            return_route = input('Dus intors? da / nu')

            if return_route == 'da':
                return_route = True
            else:
                return_route = False

            self.routes_service.add_route(id_route,
                                          id_start_city,
                                          id_stop_city,
                                          price,
                                          return_route)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_export(self):
        try:
            filename = input('Numele fisierului pentru export: ')
            self.routes_service.export_json(filename)
        except Exception as ex:
            print('Eroare:', ex)
