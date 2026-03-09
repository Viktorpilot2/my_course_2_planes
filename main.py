from src.api_interaction import CoordsPlanes
from src.file_interaction import WriteFileJson
from src.plane_interaction import PlanesInfo
from src.utils import sort_airplanes, filtr_airplanes, filtr_country_airplanes


def user_interaction():
    country = input("Введите название страны: ")

    # создание объекта класса "CoordsPlanes" при работе с API (список всех самолетов в заданном квадрате)
    airplanes_obj = CoordsPlanes()
    print(airplanes_obj.get_info_planes(country))

    # создание объекта класса "PlanesInfo" отдельно по каждому самолету
    airplane1 = PlanesInfo("Canada", "ACA411", 7924.8, 192.45)
    airplane2 = PlanesInfo("United States", "DAL464", 9745.98, 204.21)
    airplane3 = PlanesInfo("Canada", "A1112", 2200.3, 500.4)
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

    # фильтрация самолетов, полученных из json-файла, по заданной пользователем высоте полета
    altitude_range = input("Введите диапазон высот полета через пробел: ").strip()
    filtred_airplanes = filtr_airplanes(airplanes, altitude_range)
    print(filtred_airplanes)

    # получение списка топ самолетов по высоте полета после фильтрации
    top_n = input("Введите количество самолетов для вывода в топ N: ").strip()
    sorted_airplanes = sort_airplanes(top_n, filtred_airplanes)
    print(sorted_airplanes)

    # получение списка самолетов по стране регистрации
    reg_countryes_ = input("Введите названия стран для фильтрации по стране регистрации через пробел: ").strip().split()
    filtred_country_airplanes = filtr_country_airplanes(airplanes, reg_countryes_)
    print(filtred_country_airplanes)

if __name__ == '__main__':
    user_interaction()