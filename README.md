# HR - Data Project 🚀

Dieses Projekt demonstriert, wie man eine API in Python erstellt, um HR-Daten (Personaldaten) zu bereinigen und zu transformieren. Die Daten werden über einen API-Aufruf in einem Jupyter Notebook abgerufen und analysiert. Die API wird mit **FastAPI** erstellt und **Pandas** wird für die Datenverarbeitung verwendet.

## Projektstruktur 📂

Das Projekt basiert auf folgenden Komponenten:

- **data/**: Enthält die CSV-Dateien.
  - `personal.csv`: Beispiel-HR-Daten im CSV-Format.
  - `clean_data.csv`: Transformierte Daten (aus der Datenbereinigung).
  
- **src/**: Enthält alle Python-Skripte.
  - `main.py`: Haupt-API-Code.
  - `transform_data.py`: Skript zur Datenbereinigung und -transformation.

- **notebooks/**: Enthält das Jupyter Notebook für die Analyse.
  - `analysis_notebook.ipynb`: Notebook zur Analyse der transformierten Daten.

- **requirements.txt**: Liste der benötigten Bibliotheken.
- **README.md**: Dokumentation und Projektbeschreibung.
- **.gitignore**: Dateien, die nicht in das Repository aufgenommen werden sollen.

## Voraussetzungen ✅

- **Python 3.8+** installiert
- **Git** installiert (um das Repository zu klonen)

## Installation und Einrichtung 🛠️

### 1. Repository klonen

Klonen Sie das Repository von GitHub:

```bash
git clone https://github.com/username/hr_data_api_project.git
cd hr_data_api_project
