# untis_vertretungslisten
Umformatieren der Vertretungslisten, damit die Stunden
in der Vergangenheit nicht mehr dargestellt werden.

Das Skript wird einmal pro x Minuten ausgeführt (Laufzeit < 1 Sekunde) und
liest die html-Dateien von Untis ein. Dann macht es folgende Dinge:

- Alle Reglungen für heute und morgen einlesen
- Alle Regeln rausschmeißen, die schon in der Vergangenheit liegen
- Von den verbleibenden Regeln den Raumtausch optisch verbessern (Statt-Lehrer und Statt-Fach rausschmeißen, andere Farbe)
- Entfall deutlicher kennzeichnen "ENTF" statt --- und rote Farbe
- Immer 10 Regelungen pro Seite zusammenfassen und eine HTML-Datei generieren
