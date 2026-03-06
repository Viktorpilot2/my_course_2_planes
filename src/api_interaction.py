from abc import ABC, abstractmethod
import requests


class AeroplanesAPI(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def connect_api(self):
        pass

    @abstractmethod
    def get_info_planes(self, country):
        pass


class CoordsPlanes(AeroplanesAPI):

    def __init__(self):
        self.__url_nomantim = 'https://nominatim.openstreetmap.org/search'
        self.__url_opensky = 'https://opensky-network.org/api/states/all?'
        self.headers_nominatim = {
            'User-Agent': 'test-app/1.0',
        }
        self.airplanes = None

    def __connect_api(self):
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
    def connect_api(self):
        return self.__connect_api()

    def get_info_planes(self, country, limit=1):
        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': limit,
        }
        if self.connect_api:
            response_1 = requests.get(self.__url_nomantim, headers=self.headers_nominatim, params=params_nominatim)
            s, n, w, e = [i.get('boundingbox') for i in response_1.json()][0]
            params_opensky = {"lamin": s,
                              "lamax": n,
                              "lomin": w,
                              "lomax": e}

            response_2 = requests.get(self.__url_opensky, params=params_opensky)
            self.airplanes = response_2.json()
            return self.airplanes


if __name__ == '__main__':
    aa = CoordsPlanes()
    airplanes = aa.get_info_planes("Russia")
    print(airplanes)

# ww = {"time": 1766142246, "states": [
#     ["4b1812",
#      "SWR438A ",
#      "Switzerland",
#      1766166618,
#      1766166618,
#      -0.0168,
#      51.0888,
#      4267.2,
#      "false",
#      189.7,
#      129.39,
#      14.63,
#      "null",
#      4282.44,
#      "2061",
#      "false",
#      0], ["4b1812",
#           "SWR438A ",
#           "Switzerland",
#           1766166618,
#           1766166618,
#           -0.0168,
#           51.0888,
#           4267.2,
#           "false",
#           189.7,
#           129.39,
#           14.63,
#           "null",
#           4282.44,
#           "2061",
#           "false",
#           0]]}
