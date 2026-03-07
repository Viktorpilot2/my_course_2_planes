from src.api_interaction import CoordsPlanes


class PlanesInfo:

    __slots__ = ("reg_country", "callsign", "baro_altitude", "velocity")
    def __init__(self, reg_country=None, callsign=None, baro_altitude=0, velocity=0):
        self.reg_country = reg_country
        self.callsign = callsign
        self.baro_altitude = baro_altitude
        self.velocity = velocity
        self.__is_valid_data()

    @classmethod
    def create_obj(cls, country):
        data_airplanes = CoordsPlanes().get_info_planes(country)
        list_airplanes = [cls(data[2], data[1], data[7], data[9]) for data in data_airplanes.get("states")]
        return list_airplanes

    def __lt__(self, other):
        return self.baro_altitude < other.baro_altitude

    def __gt__(self, other):
        return self.velocity > other.velocity


    def __is_valid_data(self):
        if not isinstance(self.reg_country, str) or self.reg_country is None:
            self.reg_country = "Страна не указана"
        if not isinstance(self.callsign, str | int) or self.callsign is None:
            self.callsign = "Позывной не указан"
        if not isinstance(self.baro_altitude, int | float) or self.baro_altitude < 0:
            self.baro_altitude = 0
        if not isinstance(self.velocity, int | float) or self.velocity < 0:
            self.velocity = 0


if __name__ == '__main__':
    print(PlanesInfo.create_obj("Russia"))
    airplane = PlanesInfo("T", 111, 2200, 500)
    airplane1 = PlanesInfo("555", 11, 2500, 600)
    print(airplane < airplane1)
    print(airplane > airplane1)
