from urllib import response
import requests
import logging
import pandas as pd
from pandas import json_normalize


class CityBikeData():
    def __init__(self):
        self.IDENTIFIER = "osloorigo-kodeoppgave"
        self.CITY_BIKE_API = "https://gbfs.urbansharing.com/oslobysykkel.no/"
        self.STATIONS = "station_information.json"
        self.AVAILABILITY = "station_status.json"
        self.headers = {"Client-Identifier": self.IDENTIFIER}

    def get_data(self, endpoint: str) -> response:
        try:
            response = requests.get(url=self.CITY_BIKE_API + endpoint, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as errh:
            logging.exception(errh)
        except requests.exceptions.ConnectionError as errc:
            logging.exception(errc)
        except requests.exceptions.Timeout as errt:
            logging.exception(errt)
        except requests.exceptions.RequestException as err:
            logging.exception(err)

    def get_data_df(self, endpoint: str) -> pd.DataFrame:
        try:
            response = self.get_data(endpoint)
            df = pd.json_normalize(response.json()["data"]["stations"])
            return df
        except Exception as ex:
            logging.exception(ex)
            return None

    def processed_data(self) -> pd.DataFrame:
        try:
            station_info_df = self.get_data_df(self.STATIONS)
            station_status_df = self.get_data_df(self.AVAILABILITY)
            df = pd.merge(station_info_df, station_status_df, on="station_id")
            return df
        except Exception as ex:
            logging.exception(ex)
            return None
