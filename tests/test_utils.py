from typing import Any
from unittest.mock import Mock, patch

from src.file_interaction import WriteFileJson
from src.utils import filtr_airplanes, filtr_country_airplanes, sort_airplanes


@patch("src.file_interaction.WriteFileJson.get_airplane")
def test_filtr_airplanes_valid(
    mock_get_airplane: Mock, airplanes_list_result: list[dict], filtr_airplanes_valid_result_2: list[dict]
) -> None:
    """Тестирование фильтрации самолетов по высоте полета, заданной пользователем при корректном вводе данных"""
    mock_get_airplane.return_value = airplanes_list_result
    airplanes = WriteFileJson()
    assert filtr_airplanes(airplanes, "5000 8000") == filtr_airplanes_valid_result_2


@patch("src.file_interaction.WriteFileJson.get_airplane")
@patch("builtins.input")
def test_filtr_airplanes_error(
    mock_input: Mock, mock_get_airplane: Mock, airplanes_list_result: list[dict], capsys: Any
) -> None:
    """Тестирование фильтрации самолетов по высоте полета, заданной пользователем
    при некорректном вводе данных"""
    mock_get_airplane.return_value = airplanes_list_result
    mock_input.return_value = "5000 8000"
    airplanes = WriteFileJson()
    filtr_airplanes(airplanes, "5000-8000")
    capture = capsys.readouterr()
    assert capture.out == "Неправильно введен диапазон высот\n"


def test_sort_airplanes_valid(airplanes_list_result: list[dict], sort_airplanes_result: list[dict]) -> None:
    """Тестирование сортировки и возврата топ количества самолетов по высоте полета,
    заданной пользователем при корректном вводе данных"""
    assert sort_airplanes("2", airplanes_list_result) == sort_airplanes_result


@patch("builtins.input")
def test_sort_airplanes_error(mock_input: Mock, airplanes_list_result: list[dict], capsys: Any) -> None:
    """Тестирование сортировки и возврата топ количества самолетов по высоте полета, заданной пользователем
    при некорректном вводе данных"""
    mock_input.return_value = "2"
    sort_airplanes("два", airplanes_list_result)
    capture = capsys.readouterr()
    assert capture.out == "Неправильно введено количество топ N самолетов\n"


@patch("src.file_interaction.WriteFileJson.get_airplane")
def test_filtr_country_airplanes_valid(
    mock_get_airplane: Mock, airplanes_list_result: list[dict], filtr_country_airplanes_valid_result: list[dict]
) -> None:
    """Тестирование фильтрации списка самолетов по стране регистрации при корректном вводе данных"""
    mock_get_airplane.return_value = airplanes_list_result
    airplanes = WriteFileJson()
    assert filtr_country_airplanes(airplanes, ["Canada", "Russia"]) == filtr_country_airplanes_valid_result
