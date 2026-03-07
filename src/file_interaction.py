import json
import os.path
from abc import ABC, abstractmethod
from json import JSONDecodeError

from src.plane_interaction import PlanesInfo


class WriteFile(ABC):

    @abstractmethod
    def add_airplane(self, plane):
        pass

    @abstractmethod
    def get_airplane(self):
        pass

    @abstractmethod
    def del_airplane(self, plane):
        pass


class WriteFileJson(WriteFile):
    def __init__(self, path="../data/airplanes.json"):
        self.__path = path
        self.list_planes = []
        self.dict_plane = {}

    def add_airplane(self, plane):
        self.list_planes = self.get_list_airplanes(plane)
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(self.list_planes, f, indent=4, ensure_ascii=False)

    def get_airplane(self):
        if not os.path.exists(self.__path):
            self.create_path()
        else:
            try:
                with open(self.__path, "r", encoding="utf-8") as f:
                    self.list_planes = json.load(f)
            except JSONDecodeError:
                self.list_planes = []
            return self.list_planes

    def create_path(self):
        with open(self.__path, "w") as f:
            json.dump([], f)

    def del_airplane(self, plane):
        self.list_planes = self.get_airplane()
        self.dict_plane = self.get_dict_airplanes(plane)
        if self.dict_plane in self.list_planes:
                self.list_planes.remove(self.dict_plane)
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(self.list_planes, f, indent=4, ensure_ascii=False)

    def get_dict_airplanes(self, plane):
        self.dict_plane = {"reg_country": plane.reg_country, "callsign": plane.callsign,
                       "baro_altitude": plane.baro_altitude, "velocity": plane.velocity}
        return self.dict_plane

    def get_list_airplanes(self, plane):
        self.list_planes = self.get_airplane()
        self.dict_plane = self.get_dict_airplanes(plane)
        if not self.list_planes:
            self.list_planes.append(self.dict_plane)
        elif self.dict_plane not in self.list_planes:
            self.list_planes.append(self.dict_plane)
        return self.list_planes


if __name__ == '__main__':
    ap = WriteFileJson()
    airplane3 = PlanesInfo("T", 1111, 2200, 500)
    airplane4 = PlanesInfo("W", 1111, 2200, 500)
    airplane5 = PlanesInfo("S", 1111, 2200, 500)
    ap.add_airplane(airplane3)
    ap.add_airplane(airplane4)
    ap.add_airplane(airplane5)
    ap.del_airplane(airplane4)
