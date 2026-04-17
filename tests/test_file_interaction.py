import json
import os
from unittest.mock import Mock, mock_open, patch

from src.file_interaction import WriteFileJson
from src.plane_interaction import PlanesInfo


def test_init_valid() -> None:
    """Тестирование инициализации экземпляра класса 'WriteFileJson' и сеттера пути к файлу"""
    airplane = WriteFileJson()
    assert airplane.path == os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/airplanes.json")
    assert airplane.list_planes == []
    assert airplane.dict_plane == {}


@patch("os.path.exists")
@patch("src.file_interaction.WriteFileJson.create_path")
def test_get_airplane_not_path(mock_create_path: Mock, mock_path: Mock) -> None:
    """Тестирование функции для чтения информации о самолетах из json файла при отсутствии файла по заданному адресу"""
    airplane = WriteFileJson()
    mock_path.return_value = False
    mock_create_path.return_value = "путь создан"
    assert airplane.get_airplane() == []


@patch("os.path.exists")
@patch("builtins.open", mock_open(read_data="[]"))
@patch("json.load")
def test_get_airplane_valid(mock_json: Mock, mock_path: Mock, airplanes_1: dict, airplanes_result: str) -> None:
    """Тестирование функции для чтения информации о самолетах из json файла при валидных значениях"""
    airplane = WriteFileJson()
    mock_path.return_value = True
    mock_json.return_value = airplanes_1
    assert airplane.get_airplane() == json.loads(airplanes_result)


@patch("src.file_interaction.WriteFileJson.get_airplane")
@patch("src.file_interaction.WriteFileJson.get_dict_airplanes")
def test_get_list_airplanes(
    mock_get_dict: Mock, mock_get: Mock, airplanes_list: list, airplanes_list_result: list
) -> None:
    """Тестирование функции создающей обновленный список словарей с информацией о самолетах"""
    write_file = WriteFileJson()
    airplane = PlanesInfo("Canada", "A1112", 2200, 500)
    mock_get.return_value = airplanes_list
    mock_get_dict.return_value = {
        "reg_country": "Russia",
        "callsign": "R2212",
        "baro_altitude": 5200.3,
        "velocity": 650.4,
    }
    assert write_file.get_list_airplanes(airplane) == airplanes_list_result


@patch("src.file_interaction.WriteFileJson.get_list_airplanes")
def test_add_airplane(mock_get_list: Mock) -> None:
    """Тестирование записи в файл обновленной информации о самолетах"""
    airplane_1 = [{"reg_country": "Canada", "callsign": "ACA411", "baro_altitude": 7924.8, "velocity": 192.45}]
    mock_get_list.return_value = airplane_1
    airplane_instance = WriteFileJson()
    mock_plane = PlanesInfo("Canada", "ACA411", 7924.8, 192.45)
    mocked_open = mock_open()
    with patch("builtins.open", mocked_open):
        airplane_instance.add_airplane(mock_plane)
    mocked_open.assert_called_once_with(airplane_instance.path, "w", encoding="utf-8")
