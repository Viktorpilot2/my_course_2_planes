from abc import ABC, abstractmethod

import requests


class AeroplanesAPI(ABC):
    """Абстрактный класс получения данных по самолетам через API"""

    @abstractmethod
    def __init__(self) -> None:
        """Абстрактная инициализация экземпляра класса получения данных по самолетам через API"""
        pass

    @property
    @abstractmethod
    def connect_api(self) -> bool:
        """Абстрактный метод проверки статуса ответа API"""
        pass

    @abstractmethod
    def get_info_planes(self, country: str) -> dict:
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
        self.airplanes: dict = {}

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

    def get_info_planes(self, country: str, limit: int = 1) -> dict:
        """Функция, возвращающая данные о самолетах в заданной стране"""
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
        return self.airplanes


if __name__ == "__main__":  # pragma: no cover
    aa = CoordsPlanes()
    airplanes = aa.get_info_planes("Russia")
    print(airplanes)
