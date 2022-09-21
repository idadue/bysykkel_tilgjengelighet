from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from city_bike_data import CityBikeData


class VersionInfo(BaseModel):
    version: str
    service: str
    server_time: datetime = Field(default_factory=datetime.now)
    status: str = "OK"

    def now(self):
        self.server_time = datetime.utcnow()
        return self


class StationData(BaseModel):
    station_id: int
    name: str
    num_bikes_available: int
    num_docks_available: int


class CityBikeAvailability(BaseModel):
    last_reported: datetime
    data: List[StationData]


VERSION_INFO = VersionInfo(version="1.0.0", service="Bysykkel tilgjengelighet")

app = FastAPI(version=VERSION_INFO.version)


@app.get("/version")
async def version():
    return VERSION_INFO.now()


@app.get("/availability")
async def get_availability():
    city_bike = CityBikeData()
    station_status_df = city_bike.get_data_df(city_bike.AVAILABILITY)
    station_information_df = city_bike.get_data_df(city_bike.STATIONS)
    availability_df = city_bike.processes_data(station_status_df, station_information_df)

    availability_dict = (availability_df.groupby(['last_reported'])
                         .apply(lambda x: x[['station_id', 'name', 'num_bikes_available', 'num_docks_available']].to_dict('records'))
                         .reset_index()
                         .rename(columns={0: 'data'})
                         .to_dict(orient='records'))

    availability = CityBikeAvailability(last_reported=availability_dict[0]["last_reported"], data=availability_dict[0]["data"])
    return availability


if __name__ == "__main__":
    import uvicorn
    port = 8000
    uvicorn.run(app, port=port, host="127.0.0.1")
