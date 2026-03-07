from src.api_interaction import CoordsPlanes
from src.file_interaction import WriteFileJson
from src.plane_interaction import PlanesInfo

def user_interaction():
    country = input("Введите название страны: ")
    # top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    # filter_words = input("Введите названия стран для фильтрации по стране регистрации: ").split()
    # altitude_range = input("Введите диапазон высот полета: ")

    # создание объекта класса "CoordsPlanes" при работе с API (список всех самолетов в заданном квадрате)
    airplanes_obj = CoordsPlanes()
    print(airplanes_obj.get_info_planes(country))

    # создание объекта класса "PlanesInfo" отдельно по каждому самолету
    airplane1 = PlanesInfo("Canada", "ACA411", 7924.8, 192.45)
    airplane2 = PlanesInfo("United States", "DAL464", 9745.98, 204.21)
    airplane3 = PlanesInfo("T", "A1112", 2200.3, 500.4)
    # сравнение созданные объекты по высоте и скорости с помощью магических методов
    print(airplane1 < airplane2)
    print(airplane1 > airplane2)
    # создание объекта класса "PlanesInfo" из полученного класса "CoordsPlanes"
    # (выбранные данные по всем самолетам полученным по API)
    print(PlanesInfo.create_obj(country))

    # создание объекта класса "WriteFileJson" (запись данных по самолетам в json-файл)
    airplanes = WriteFileJson()
    # добавление объекта (информации по одному самолету) в список для записи в json-файл
    airplanes.add_airplane(airplane1)
    airplanes.add_airplane(airplane2)
    airplanes.add_airplane(airplane3)
    # удаление объекта (информации по одному самолету) из списка json-файла
    airplanes.del_airplane(airplane2)
    # добавление объектов (информации по всем самолетам, полученным с API) в список для записи в json-файл
    for i in PlanesInfo.create_obj(country):
        airplanes.add_airplane(i)


if __name__ == '__main__':
    user_interaction()