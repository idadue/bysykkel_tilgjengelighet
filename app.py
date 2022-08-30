import streamlit as st
import pandas as pd
from datetime import datetime
from city_bike_data import CityBikeData


def main():
    st.set_page_config(
        page_title="Bysykkel tilgjengelighet",
        page_icon="🚲",
        layout="wide",
    )

    city_bike = CityBikeData()
    df = city_bike.processed_data()
    if df is None:
        st.error("Tjenesten er ikke tilgjengelig akkurat nå 😭 Prøv igjen senere.")
    else:
        st.title("Bysykkel tilgjengelighet")
        st.markdown("Se hvor mange sykler og låser som er tilgjengelige i Oslo")

        station_name = st.selectbox("Bla eller søk etter stasjon",  df["name"])

        n_bikes = df.loc[df["name"] == station_name, "num_bikes_available"].item()
        n_locks = df.loc[df["name"] == station_name, "num_docks_available"].item()
        time = df.loc[df["name"] == station_name, "last_reported"].item()

        placeholder = st.empty()

        with placeholder.container():
            station, bikes, locks = st.columns(3)

            station.metric(
                    label="Stasjon 📍",
                    value=station_name,
                )

            bikes.metric(
                    label="Sykler 🚲",
                    value=n_bikes,
                )

            locks.metric(
                    label="Låser 🔒",
                    value=n_locks,
                )
            st.markdown(f"sist oppdatert: {datetime.fromtimestamp(time)}")


if __name__ == "__main__":
    main()
    