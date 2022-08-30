# Bysykkel tilgjengelighet 🚲
En enkel [streamlit applikasjon](https://github.com/streamlit/streamlit)  som henter sanntidsdata fra [Oslo bysykkel](https://oslobysykkel.no/apne-data/sanntid) og viser antall ledige sykler og låser for valgt stasjon. 

## Setup

Python virtuelt miljø og installer nødvendige biblioteker  (anbefaler python 3.9):

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

```
streamlit run app.py
```

Streamlit serveren skal da starte standardnettleseren din og ta deg rett til appen.

## Bruk
![](demo.gif)

