---
title: App Structure
parent: Technical Docs
nav_order: 1
---

{: .label }
[Jane Dane]

### App Strcture:


Die Struktur der "2DO"-App ist gut organisiert und bietet eine klare Trennung der verschiedenen Komponenten, um eine einfache Wartung und Erweiterung zu ermöglichen. Hier sind einige wichtige Merkmale der App-Struktur:


**Verzeichnisstruktur**: Die Anwendung ist in logisch benannte Verzeichnisse unterteilt, die verschiedene Aspekte der Anwendung enthalten, z. B. Templates, statische Dateien und Routen.


**Routen**: Die Routing-Logik ist klar definiert und in separaten Dateien organisiert, um eine bessere Übersichtlichkeit zu gewährleisten. Jede Route ist einer spezifischen Funktion zugewiesen, die entscheidet, welche Daten dem Benutzer angezeigt werden.


**Datenbankintegration**: Die Anwendung verwendet SQLAlchemy zur Interaktion mit der SQLite-Datenbank. Das Datenbankmodell ist gut strukturiert und definiert die Beziehungen zwischen den verschiedenen Entitäten wie Benutzern und Aufgaben.


**Templates und Views**: Die HTML-Templates und View-Funktionen sind in separaten Dateien organisiert, um die Trennung von Präsentation und Logik zu unterstützen. Dadurch wird der Code sauberer und leichter verständlich.


**Statische Dateien**: Statische Ressourcen wie CSS-Dateien und Bilder sind in separaten Verzeichnissen organisiert und über entsprechende URLs zugänglich gemacht, um eine effiziente Bereitstellung zu ermöglichen.
