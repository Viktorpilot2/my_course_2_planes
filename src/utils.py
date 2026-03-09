from src.file_interaction import WriteFileJson

def filtr_airplanes(airplanes, altitude):
    """Фильтрация самолетов по высоте полета, заданной пользователем"""
    while True:
        try:
            list_altitude = [*map(int, altitude.split())]
            return [x for x in WriteFileJson.get_airplane(airplanes) if list_altitude[0] <= x.get("baro_altitude") <= list_altitude[1]]
        except (ValueError, IndexError):
            print("Неправильно введен диапазон высот")
            altitude = input("Введите диапазон высот полета через пробел: ").strip()
            continue

def sort_airplanes(n, filtred_airplane, reverse=True):
    """Сортировка и возврат топ списка самолетов по высоте полета"""
    while True:
        try:
            sorted_airplanes_ = sorted(filtred_airplane, key=lambda x: x.get("baro_altitude"), reverse=reverse)
            top_n_airplans = sorted_airplanes_[:int(n)]
            return top_n_airplans
        except (ValueError, TypeError):
            print("Неправильно введено количество топ N самолетов")
            n = int(input("Введите количество самолетов для вывода в топ N: ").strip())
            continue

def filtr_country_airplanes(airplanes, reg_countryes):
        reg_countryes = [*map(lambda x: x.lower(), reg_countryes)]
        return [x for x in WriteFileJson.get_airplane(airplanes) if x.get("reg_country").lower() in reg_countryes]



if __name__ == '__main__':
    airplanes_country = WriteFileJson()
    altitude_range = input("Введите диапазон высот полета через пробел: ").strip()
    filtred_airplanes = filtr_airplanes(airplanes_country, altitude_range)
    print(filtred_airplanes)

    top_n = input("Введите количество самолетов для вывода в топ N: ").strip()
    sorted_airplanes = sort_airplanes(top_n, filtred_airplanes)
    print(sorted_airplanes)

    reg_countryes_ = input("Введите названия стран для фильтрации по стране регистрации через пробел: ").strip().split()
    filtred_country_airplanes = filtr_country_airplanes(airplanes_country, reg_countryes_)
    print(filtred_country_airplanes)
