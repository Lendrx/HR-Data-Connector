import pandas as pd

# CSV-Datei laden
df = pd.read_csv("personal.csv")

# Leere Werte entfernen
df.dropna(inplace=True)

# Neue Spalte „Total Salary“ berechnen
df["Total Salary"] = df["hourly_rate"] * df["hours_worked"]

# Ergebnis speichern
df.to_csv("clean_data.csv", index=False)
