import pytest
import json
import pandas as pd
from pandas.testing import assert_frame_equal
from city_bike_data import CityBikeData


@pytest.fixture
def city_bike():
    return CityBikeData()


@pytest.fixture
def station_status():
    with open("tests/data/station_status.json") as f:
        return json.load(f)


@pytest.fixture
def station_information():
    with open("tests/data/station_information.json") as f:
        return json.load(f)


@pytest.fixture
def example_processed_data():
    data = [
        {
            "station_id": "623",
            "name": "7 Juni Plassen",
            "address": "7 Juni Plassen",
            "lat": 59.9150596,
            "lon": 10.7312715,
            "capacity": 15,
            "is_installed": 1,
            "is_renting": 1,
            "num_bikes_available": 4,
            "num_docks_available": 8,
            "last_reported": 1663754697,
            "is_returning": 1
        }
    ]
    return pd.DataFrame(data)


def test_get_data(city_bike):
    station_status_response = city_bike.get_data(city_bike.AVAILABILITY)
    station_information_response = city_bike.get_data(city_bike.STATIONS)
    assert station_status_response.ok is True
    assert station_information_response.ok is True


def test_process_data(city_bike, station_status, station_information, example_processed_data):
    station_status_df = pd.json_normalize(station_status["data"]["stations"])
    station_information_df = pd.json_normalize(station_information["data"]["stations"])

    assert_frame_equal(city_bike.processes_data(station_information_df, station_status_df),example_processed_data)
