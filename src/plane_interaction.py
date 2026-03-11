from __future__ import annotations

from src.api_interaction import CoordsPlanes


class PlanesInfo:
    """Класс формирования основных данных по самолетам"""

    __slots__ = ("reg_country", "callsign", "baro_altitude", "velocity")

    def __init__(
        self,
        reg_country: str | None = None,
        callsign: str | None = None,
        baro_altitude: int | float = 0,
        velocity: int | float = 0,
    ) -> None:
        """Инициализация экземпляра класса основных данных по самолетам"""
        self.reg_country = reg_country
        self.callsign = callsign.strip() if callsign else callsign
        self.baro_altitude = baro_altitude
        self.velocity = velocity
        self.__is_valid_data()

    @classmethod
    def create_obj(cls, country: str) -> list[PlanesInfo]:
        """Классметод создания списка объектов основных данных по самолетам"""
        data_airplanes = CoordsPlanes().get_info_planes(country)
        if data_airplanes:
            list_airplanes = [cls(data[2], data[1], data[7], data[9]) for data in data_airplanes.get("states", [])]
        else:
            list_airplanes = []
        return list_airplanes

    def __lt__(self, other: PlanesInfo) -> bool:
        """Магический метод для сравнения высот полета двух самолетов"""
        return self.baro_altitude < other.baro_altitude

    def __gt__(self, other: PlanesInfo) -> bool:
        """Магический метод для сравнения скоростей полета двух самолетов"""
        return self.velocity > other.velocity

    def __is_valid_data(self) -> None:
        """Проверка валидности значений при инициализации экземпляра класса основных данных по самолетам"""
        if not isinstance(self.reg_country, str) or self.reg_country is None or self.reg_country == "":
            self.reg_country = "Страна не указана"
        if not isinstance(self.callsign, str) or self.callsign is None or self.callsign == "":
            self.callsign = "Позывной не указан"
        if not isinstance(self.baro_altitude, int | float) or self.baro_altitude < 0 or self.baro_altitude is None:
            self.baro_altitude = 0
        if not isinstance(self.velocity, int | float) or self.velocity < 0 or self.velocity is None:
            self.velocity = 0


if __name__ == "__main__":  # pragma: no cover
    print(PlanesInfo.create_obj("Russia"))
    airplane = PlanesInfo("Canada", "ACA411", 2200, 500)
    airplane1 = PlanesInfo("Russia", "DAL464", 2500, 600)
    print(airplane < airplane1)
    print(airplane > airplane1)
