from typing import List

from Domain.city import City
from Domain.city_validator import CityValidator
from Repository.repository import Repository


class CityService:
    def __init__(self,
                 city_repository: Repository,
                 city_validator: CityValidator):
        """
        Creeaza un service pentru localitati.
        :param city_repository: repository
               care retine localitati.
        :param city_validator: validatorul
               pentru localitati
        """
        self.city_repository = city_repository
        self.city_validator = city_validator

    def add_city(self, id_city: str, name: str, type: str):
        """
        Adauga o localitate.
        :param id_city: id-ul localitatii.
        :param name: numele localitatii, string nenul.
        :param type: tipul localitatii, sat, oras sau municipiu.
        :return:
        """
        city = City(id_city, name, type)
        self.city_validator.validate(city)
        self.city_repository.create(city)

    def get_all(self) -> List[City]:
        """
        :return: o lista cu toate localitatile
        """
        return self.city_repository.read()
