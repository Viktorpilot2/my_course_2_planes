import json
from unittest.mock import Mock, patch

from src.api_interaction import CoordsPlanes


@patch("requests.get")
def test_connect_api_sc_true(mock_requests: Mock) -> None:
    """Тестирование функции при возвращении от API статус кода 200"""
    airplanes_obj = CoordsPlanes()
    mock_requests.return_value.status_code = 200
    assert airplanes_obj.connect_api is True


@patch("requests.get")
def test_connect_api_sc_false(mock_requests: Mock) -> None:
    """Тестирование функции при возвращении от API статус кода с ошибкой"""
    airplanes_obj = CoordsPlanes()
    mock_requests.return_value.status_code = 404
    assert airplanes_obj.connect_api is False


@patch("src.api_interaction.CoordsPlanes.connect_api")
@patch("requests.get")
def test_get_info_planes(mock_requests: Mock, mock_api: Mock, airplanes_1: dict, airplanes_result: dict) -> None:
    """Тестирование функции, возвращающей json-ответ с данными по самолетам при успешном обращении к API"""
    airplanes_obj = CoordsPlanes()
    mock_api.return_value = True
    mock_requests.return_value.json.side_effect = [
        [{"boundingbox": ["41.6765597", "83.3362128", "-141.0027500", "-52.3237664"]}],
        airplanes_1,
    ]
    assert json.dumps(airplanes_obj.get_info_planes("France")) == airplanes_result
