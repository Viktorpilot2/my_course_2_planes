from unittest.mock import Mock, patch

from src.plane_interaction import PlanesInfo


def test_planes_info_init() -> None:
    """Тестирование инициализации экземпляра класса 'PlanesInfo'"""
    airplane = PlanesInfo("T", "ACA411", 2200, 500)
    assert airplane.reg_country == "T"
    assert airplane.callsign == "ACA411"
    assert airplane.baro_altitude == 2200
    assert airplane.velocity == 500


@patch("src.api_interaction.CoordsPlanes.get_info_planes")
def test_create_obj_valid(mock_coords_planes: Mock, airplanes_1: dict) -> None:
    """Тестирование классметода создания списка объектов основных данных по самолетам,
    полученных по API при валидных значениях"""
    mock_coords_planes.return_value = airplanes_1
    assert PlanesInfo.create_obj("France")[1].reg_country == "Switzerland"
    assert PlanesInfo.create_obj("France")[0].callsign == "TVF97HM"
    assert PlanesInfo.create_obj("France")[3].baro_altitude == 9448.8
    assert PlanesInfo.create_obj("France")[4].velocity == 218.71


@patch("src.api_interaction.CoordsPlanes.get_info_planes")
def test_create_obj_response_none(mock_coords_planes: Mock) -> None:
    """Тестирование классметода создания списка объектов основных данных по самолетам,
    полученных по API при ошибках API"""
    mock_coords_planes.return_value = None
    assert PlanesInfo.create_obj("France") == []


def test_is_valid_data() -> None:
    """Тестирование создания экземпляров класса 'PlanesInfo' на валидность значений"""
    PlanesInfo.create_obj("Russia")
    airplane_1 = PlanesInfo(None, "ACA411", 2200, 500)
    airplane_2 = PlanesInfo("France", None, 2200, 500)
    airplane_3 = PlanesInfo("France", "ACA411", -2200, 500)
    airplane_4 = PlanesInfo("France", "ACA411", 2200, "500")  # type: ignore
    assert airplane_1.reg_country == "Страна не указана"
    assert airplane_2.callsign == "Позывной не указан"
    assert airplane_3.baro_altitude == 0
    assert airplane_4.velocity == 0


def test_lt() -> None:
    """Тестирование метода сравнения самолетов по высоте полета"""
    PlanesInfo.create_obj("Russia")
    airplane_1 = PlanesInfo("Italy", "ACA411", 2200, 500)
    airplane_2 = PlanesInfo("France", "RFD411", 4200, 300)
    result = airplane_1 < airplane_2
    assert result is True
    result = airplane_2 < airplane_1
    assert result is False


def test_gt() -> None:
    """Тестирование метода сравнения самолетов по скорости полета"""
    PlanesInfo.create_obj("Russia")
    airplane_1 = PlanesInfo("Italy", "ACA411", 2200, 500)
    airplane_2 = PlanesInfo("France", "RFD411", 4200, 300)
    result = airplane_1 > airplane_2
    assert result is True
    result = airplane_2 > airplane_1
    assert result is False
