# Bysykkel tilgjengelighet 🚲
[Del 1](#del-1): En enkel [streamlit applikasjon](https://github.com/streamlit/streamlit)  som henter sanntidsdata fra [Oslo bysykkel](https://oslobysykkel.no/apne-data/sanntid) og viser antall ledige sykler og låser for valgt stasjon. 

[Del 2](#del-2): REST-basert endepunkt.

## Setup

Python virtuelt miljø og installer nødvendige biblioteker (anbefaler python 3.9):

Windows:

```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Unix/MacOS:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Run
### Del 1
```
streamlit run app.py
```

Streamlit serveren skal da starte standardnettleseren din og ta deg rett til appen.

### Del 2
For å starte applikasjonen:
```
python -m api.app
```
#### Endepunkter:
Versjon
```
GET /version
```
Respons
```
version	"1.0.0"
service	"Bysykkel tilgjengelighet"
server_time	"2022-09-20T19:16:56.731994"
status	"OK"
```

Tilgjengelighet
```
GET /availability
```
Respons
```
{
    "last_reported": "2022-09-20T18:58:17+00:00",
    "data": [
        {
            "station_id": 2351,
            "name": "Sogn Studentby",
            "num_bikes_available": 1,
            "num_docks_available": 17
        },
        {
            "station_id": 2350,
            "name": "Blindern T-Bane",
            "num_bikes_available": 0,
            "num_docks_available": 25
        }, 
        ...
        {
            "station_id": 485,
            "name": "Sommerfrydhagen",
            "num_bikes_available": 4,
            "num_docks_available": 17
        }
    ]
}
```
## Hvordan bruke streamlit applikasjonen
![](demo.gif)

