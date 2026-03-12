import json

import pytest


@pytest.fixture
def airplanes_1() -> dict:
    return {
        "time": 1772824667,
        "states": [
            [
                "39de4f",
                "TVF97HM ",
                "France",
                1772824667,
                1772824667,
                8.2904,
                42.5036,
                11590.02,
                False,
                240.07,
                329.48,
                0,
                None,
                11650.98,
                "1000",
                False,
                0,
            ],
            [
                "4b1819",
                "SWR27M  ",
                "Switzerland",
                1772824666,
                1772824666,
                3.4166,
                50.6344,
                11887.2,
                False,
                232.92,
                136.79,
                0,
                None,
                11925.3,
                "2077",
                False,
                0,
            ],
            [
                "a8a812",
                "N657PT  ",
                "United States",
                1772824660,
                1772824663,
                -122.9559,
                45.5429,
                None,
                True,
                0,
                357.19,
                None,
                None,
                None,
                None,
                False,
                0,
            ],
            [
                "a8a813",
                "R697PT  ",
                "Switzerland",
                1772824668,
                2772824663,
                -222.9559,
                55.5429,
                9448.8,
                True,
                3000,
                357.19,
                None,
                None,
                None,
                None,
                False,
                0,
            ],
            [
                "a2e5ec",
                "SKW4261 ",
                "United States",
                1772824666,
                1772824666,
                -100.0093,
                47.3865,
                9448.8,
                False,
                218.71,
                105.83,
                0.33,
                None,
                9265.92,
                None,
                False,
                0,
            ],
            [
                "a8a814",
                "R757PR  ",
                "Switzerland",
                1772824668,
                2772824663,
                -222.9559,
                55.5429,
                9200.8,
                True,
                2000,
                357.19,
                None,
                None,
                None,
                None,
                False,
                0,
            ],
            [
                "a8a813",
                None,
                None,
                1772824668,
                2772824663,
                -222.9559,
                55.5429,
                -9448.8,
                True,
                "3000",
                357.19,
                None,
                None,
                None,
                None,
                False,
                0,
            ],
        ],
    }


@pytest.fixture
def airplanes_result() -> str:
    return json.dumps(
        {
            "time": 1772824667,
            "states": [
                [
                    "39de4f",
                    "TVF97HM ",
                    "France",
                    1772824667,
                    1772824667,
                    8.2904,
                    42.5036,
                    11590.02,
                    False,
                    240.07,
                    329.48,
                    0,
                    None,
                    11650.98,
                    "1000",
                    False,
                    0,
                ],
                [
                    "4b1819",
                    "SWR27M  ",
                    "Switzerland",
                    1772824666,
                    1772824666,
                    3.4166,
                    50.6344,
                    11887.2,
                    False,
                    232.92,
                    136.79,
                    0,
                    None,
                    11925.3,
                    "2077",
                    False,
                    0,
                ],
                [
                    "a8a812",
                    "N657PT  ",
                    "United States",
                    1772824660,
                    1772824663,
                    -122.9559,
                    45.5429,
                    None,
                    True,
                    0,
                    357.19,
                    None,
                    None,
                    None,
                    None,
                    False,
                    0,
                ],
                [
                    "a8a813",
                    "R697PT  ",
                    "Switzerland",
                    1772824668,
                    2772824663,
                    -222.9559,
                    55.5429,
                    9448.8,
                    True,
                    3000,
                    357.19,
                    None,
                    None,
                    None,
                    None,
                    False,
                    0,
                ],
                [
                    "a2e5ec",
                    "SKW4261 ",
                    "United States",
                    1772824666,
                    1772824666,
                    -100.0093,
                    47.3865,
                    9448.8,
                    False,
                    218.71,
                    105.83,
                    0.33,
                    None,
                    9265.92,
                    None,
                    False,
                    0,
                ],
                [
                    "a8a814",
                    "R757PR  ",
                    "Switzerland",
                    1772824668,
                    2772824663,
                    -222.9559,
                    55.5429,
                    9200.8,
                    True,
                    2000,
                    357.19,
                    None,
                    None,
                    None,
                    None,
                    False,
                    0,
                ],
                [
                    "a8a813",
                    None,
                    None,
                    1772824668,
                    2772824663,
                    -222.9559,
                    55.5429,
                    -9448.8,
                    True,
                    "3000",
                    357.19,
                    None,
                    None,
                    None,
                    None,
                    False,
                    0,
                ],
            ],
        }
    )


@pytest.fixture
def airplanes_list() -> list[dict]:
    return [
        {"reg_country": "Canada", "callsign": "ACA411", "baro_altitude": 7924.8, "velocity": 192.45},
        {"reg_country": "Canada", "callsign": "A1112", "baro_altitude": 2200.3, "velocity": 500.4},
        {"reg_country": "France", "callsign": "TVF97HM", "baro_altitude": 11590.02, "velocity": 240.07},
    ]


@pytest.fixture
def airplanes_list_result() -> list[dict]:
    return [
        {"reg_country": "Canada", "callsign": "ACA411", "baro_altitude": 7924.8, "velocity": 192.45},
        {"reg_country": "Canada", "callsign": "A1112", "baro_altitude": 2200.3, "velocity": 500.4},
        {"reg_country": "France", "callsign": "TVF97HM", "baro_altitude": 11590.02, "velocity": 240.07},
        {"reg_country": "Russia", "callsign": "R2212", "baro_altitude": 5200.3, "velocity": 650.4},
    ]


@pytest.fixture
def airplanes_list_2() -> list[dict]:
    return [
        {"reg_country": "Canada", "callsign": "A1112", "baro_altitude": 2200, "velocity": 500},
        {"reg_country": "Canada", "callsign": "ACA411", "baro_altitude": 7924.8, "velocity": 192.45},
    ]


@pytest.fixture
def filtr_airplanes_valid_result_2() -> list[dict]:
    return [
        {"reg_country": "Canada", "callsign": "ACA411", "baro_altitude": 7924.8, "velocity": 192.45},
        {"reg_country": "Russia", "callsign": "R2212", "baro_altitude": 5200.3, "velocity": 650.4},
    ]


@pytest.fixture
def sort_airplanes_result() -> list[dict]:
    return [
        {"reg_country": "France", "callsign": "TVF97HM", "baro_altitude": 11590.02, "velocity": 240.07},
        {"reg_country": "Canada", "callsign": "ACA411", "baro_altitude": 7924.8, "velocity": 192.45},
    ]


@pytest.fixture
def filtr_country_airplanes_valid_result() -> list[dict]:
    return [
        {"reg_country": "Canada", "callsign": "ACA411", "baro_altitude": 7924.8, "velocity": 192.45},
        {"reg_country": "Canada", "callsign": "A1112", "baro_altitude": 2200.3, "velocity": 500.4},
        {"reg_country": "Russia", "callsign": "R2212", "baro_altitude": 5200.3, "velocity": 650.4},
    ]
