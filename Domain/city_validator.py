from Domain.city import City


class CityValidator:

    def validate(self, city: City):

        errors = []
        if city.name == '':
            errors.append('Numele localitatii nu poate fi gol!')
        if city.type not in ['sat', 'oras', 'municipiu']:
            errors.append('Tipul localitatii este invalid.')

        if errors:
            raise ValueError(errors)