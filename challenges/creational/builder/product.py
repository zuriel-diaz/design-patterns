class Product:
    def __init__(self, id: int, type: str, name: str, description: str, price: float, countries: list, alias: str):
        self._id = id
        self._type = type
        self._name = name
        self._description = description
        self._price = price
        self._countries = countries
        self._alias = alias