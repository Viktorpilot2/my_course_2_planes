from abc import ABC, abstractmethod
from typing import Any

import requests


class AeroplanesAPI(ABC):
    """Абстрактный класс получения данных по самолетам через API"""

    @abstractmethod
    def __init__(self) -> None:
        """Абстрактная инициализация экземпляра класса получения данных по самолетам через API"""
        pass

    @abstractmethod
    def connect_api(self) -> bool:
        """Абстрактный метод проверки статуса ответа API"""
        pass

    @abstractmethod
    def get_info_planes(self, country: str) -> list[dict]:
        """Абстрактный метод получения данных по самолетам через API"""
        pass


class CoordsPlanes(AeroplanesAPI):
    """Класс получения данных по самолетам через API"""

    def __init__(self) -> None:
        """Инициализация экземпляра класса получения данных по самолетам через API"""
        self.__url_nomantim = "https://nominatim.openstreetmap.org/search"
        self.__url_opensky = "https://opensky-network.org/api/states/all?"
        self.headers_nominatim = {
            "User-Agent": "test-app/1.0",
        }
        self.airplanes = None

    def __connect_api(self) -> bool:
        """Метод, выполняющий проверку статуса ответа API"""
        response_nomantim = requests.get(self.__url_nomantim, headers=self.headers_nominatim)
        s_code_1 = response_nomantim.status_code
        response_opensky = requests.get(self.__url_opensky)
        s_code_2 = response_opensky.status_code

        flag = True
        if s_code_1 != 200:
            print(f"Ошибка при обращении к {self.__url_nomantim}: {s_code_1}")
            flag = False
        if s_code_2 != 200:
            print(f"Ошибка при обращении к {self.__url_opensky}: {s_code_2}")
            flag = False
        return flag

    @property
    def connect_api(self) -> bool:
        """Сеттер, возвращающий приватный атрибут проверки статуса ответа API"""
        return self.__connect_api()

    def get_info_planes(self, country: str, limit: int = 1) -> list[Any]:
        params_nominatim = {
            "country": country,
            "format": "json",
            "limit": limit,
        }
        if self.connect_api:
            response_1 = requests.get(self.__url_nomantim, headers=self.headers_nominatim, params=params_nominatim)
            s, n, w, e = [i.get("boundingbox") for i in response_1.json()][0]
            params_opensky = {"lamin": s, "lamax": n, "lomin": w, "lomax": e}

            response_2 = requests.get(self.__url_opensky, params=params_opensky)
            self.airplanes = response_2.json()
        else:
            self.airplanes = []
        return self.airplanes


if __name__ == "__main__":  # pragma: no cover
    aa = CoordsPlanes()
    airplanes = aa.get_info_planes("Russia")
    print(airplanes)

# ww = {'time': 1772824667, 'states': [
#     ['39de4f', 'TVF97HM ', 'France', 1772824667, 1772824667, 8.2904, 42.5036, 11590.02, False, 240.07, 329.48, 0, None,
#      11650.98, '1000', False, 0],
#     ['4b1819', 'SWR27M  ', 'Switzerland', 1772824666, 1772824666, 3.4166, 50.6344, 11887.2, False, 232.92, 136.79, 0,
#      None, 11925.3, '2077', False, 0],
#     ['a8a812', 'N657PT  ', 'United States', 1772824660, 1772824663, -122.9559, 45.5429, None, True, 0, 357.19, None,
#      None, None, None, False, 0],
#     ['a2e5ec', 'SKW4261 ', 'United States', 1772824666, 1772824666, -100.0093, 47.3865, 9448.8, False, 218.71, 105.83,
#      0.33, None, 9265.92, None, False, 0]]}
