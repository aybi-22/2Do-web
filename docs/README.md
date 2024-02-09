# Schritte zum Ausführen der Anwendung

Um die Anwendung auszuführen, müssen folgende Schritte befolgt werden:

## Schritt 1: Python Virtual Environment einrichten

Richten Sie eine Python Virtual Environment ein und aktivieren Sie sie. Sie können dies mit dem Befehl auf UNIX-Systemen:

python -m venv venv
source venv/bin/activate                                                              

Oder auf Windows-Systemen:

python -m venv venv
venv\Scripts\activate


## Schritt 2: Installieren der erforderlichen Python-Pakete

Installieren Sie die erforderlichen Python-Pakete aus der requirements.txt-Datei, indem Sie den Befehl in der Befehlszeile ausführen:

pip install -r requirements.txt


## Schritt 3: Initialisieren der SQLite-Datenbank (Optional, aber empfohlen)

Optional, aber empfohlen: Initialisieren Sie die SQLite-Datenbank der Anwendung mit dem Befehl:

flask init-db


Beachten Sie, dass dies auch die Konfiguration der SQLAlchemy-Datenbank umfasst.

## Schritt 4: Webserver starten

Starten Sie den Webserver mit dem Befehl:

flask run --reload


## Schritt 5: Anwendung anzeigen

Besuchen Sie die Seite [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in Ihrem Webbrowser, um die Startseite der Anwendung anzuzeigen.
