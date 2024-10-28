# HR Data API Project 🚀

Dies ist ein einfaches Projekt, das zeigt, wie man eine API in Python erstellt, um HR-Daten (Personaldaten) zu bereinigen und zu transformieren und sie dann über einen API-Aufruf in einem Jupyter Notebook analysieren kann. Die API wird mit **FastAPI** erstellt, und **Pandas** wird für die Datenverarbeitung verwendet.

## Übersicht 📚

Die API übernimmt eine CSV-Datei (`personal.csv`) mit HR-Daten und berechnet eine neue Spalte „Total Salary“, die das Gehalt auf Basis des Stundenlohns und der geleisteten Arbeitsstunden berechnet. Die transformierten Daten werden dann in `clean_data.csv` gespeichert und können über die API in einem Jupyter Notebook abgerufen und weiter analysiert werden.

## Voraussetzungen ✅

- **Python 3.8+** installiert
- **Git** installiert (um das Repository zu klonen)
- **Virtuelle Umgebung (venv)** zum Isolieren von Abhängigkeiten
- Bibliotheken: `FastAPI`, `Pandas`, `uvicorn`, `requests`

## Installation 🛠️

1. **Repository klonen**

   ```bash
   git clone https://github.com/username/hr_data_api_project.git
   cd hr_data_api_project
