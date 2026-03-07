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
    def __init__(self, path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/airplanes.json")):
        """Инициализация экземпляра класса записи в файл информации о самолетах"""
        self.__path = path
        self.list_planes = []
        self.dict_plane = {}

    def get_dict_airplanes(self, plane):
        """Преобразование экземпляра класса PlanesInfo в словарь с данными о самолете"""
        self.dict_plane = {"reg_country": plane.reg_country, "callsign": plane.callsign,
                       "baro_altitude": plane.baro_altitude, "velocity": plane.velocity}
        return self.dict_plane

    def create_path(self):
        """Создание файла json с пустым списком для дальнейшей записи информации о самолетах"""
        with open(self.__path, "w") as f:
            json.dump([], f)

    def get_airplane(self):
        """Чтение информации о самолетах из json файла"""
        if not os.path.exists(self.__path):
            self.create_path()
        else:
            try:
                with open(self.__path, "r", encoding="utf-8") as f:
                    self.list_planes = json.load(f)
            except JSONDecodeError:
                self.list_planes = []
            return self.list_planes

    def get_list_airplanes(self, plane):
        """Создание обновленного списка словарей с информацией о самолетах"""
        self.list_planes = self.get_airplane()
        self.dict_plane = self.get_dict_airplanes(plane)
        if not self.list_planes or self.dict_plane not in self.list_planes:
            self.list_planes.append(self.dict_plane)
        return self.list_planes

    def add_airplane(self, plane):
        """Запись в файл обновленного списка словарей с информацией о самолетах"""
        self.list_planes = self.get_list_airplanes(plane)
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(self.list_planes, f, indent=4, ensure_ascii=False)

    def del_airplane(self, plane):
        """Удаление из json файла информации о выбранном самолете"""
        self.list_planes = self.get_airplane()
        self.dict_plane = self.get_dict_airplanes(plane)
        if self.dict_plane in self.list_planes:
                self.list_planes.remove(self.dict_plane)
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(self.list_planes, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    ap = WriteFileJson()
    airplane3 = PlanesInfo("T", "A1112", 2200, 500)
    airplane4 = PlanesInfo("W", "B1113", 3200, 600)
    airplane5 = PlanesInfo("S", "C1114", 4200, 400)
    ap.add_airplane(airplane3)
    ap.add_airplane(airplane4)
    ap.add_airplane(airplane5)
    ap.del_airplane(airplane4)
