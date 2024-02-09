---
title: Design Decisions
nav_order: 3
---

{: .label }
[Jane Dane]

# [Design decisions]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Verwendung von Flask-SQLAlchemy für die Datenbankintegration



### Meta

Status
: **Decided** 

Updated
: 09-Feb-2024

### Problem statement

Wir müssen eine Flask-Erweiterung für die Integration einer relationalen Datenbank in unsere Anwendung wählen.

### Decision

Wir haben uns für die Verwendung von Flask-SQLAlchemy zur Datenbankintegration entschieden aufgrund seiner nahtlosen Integration in Flask und der vereinfachten Datenbankoperationen. Flask-SQLAlchemy bietet eine ORM-Schicht über SQLAlchemy, was es einfacher macht, mit Datenbanken in Flask-Anwendungen zu arbeiten.



### Regarded options

Raw SQLAlchemy: Wir könnten Raw SQLAlchemy für die Datenbankintegration verwenden, aber es erfordert mehr Konfiguration und Boilerplate-Code im Vergleich zu Flask-SQLAlchemy.


Flask-SQLAlchemy: Flask-SQLAlchemy ist eine Flask-Erweiterung, die eine einfache Integration mit SQLAlchemy bietet und es ermöglicht, Datenbankmodelle zu definieren und Datenbankabfragen mit minimalem Setup und Konfiguration auszuführen.
---


## 02: Verwendung von Flask für das Web-Framework


### Meta

Status
: **Decided** 

Updated
: 09-Feb-2024


### Problem statement

Wir müssen ein Web-Framework für unsere Anwendung wählen, um HTTP-Anfragen zu verarbeiten und Webseiten zu rendern.


### Decision

Wir haben uns entschieden, Flask als Web-Framework zu verwenden, aufgrund seiner Einfachheit, Flexibilität und leichten Lernkurve. Flask bietet eine minimale, aber leistungsfähige Grundlage für die Entwicklung von Webanwendungen und ermöglicht es uns, schnell und effizient Webseiten zu erstellen.


### Regarded options

Flask: Flask ist ein Microframework für Python, das eine einfache und modulare Struktur bietet und sich gut für kleine bis mittlere Webanwendungen eignet.


Django: Django ist ein Full-Stack-Webframework für Python, das eine umfassende Sammlung von Tools und Funktionen bietet, was es gut für komplexe Webanwendungen macht. Allerdings kann Django für kleinere Projekte überdimensioniert sein und eine steilere Lernkurve haben als Flask.
---


## 03: Verwendung von Werkzeug für die HTTP-Anfrageverarbeitung

### Meta

Status
: **Decided** 

Updated
: 09-Feb-2024


### Problem statement

Wir müssen ein Web-Framework für unsere Anwendung wählen, um HTTP-Anfragen zu verarbeiten und Webseiten zu rendern.


### Decision

Wir haben uns entschieden, Werkzeug als WSGI-Toolkit für die Verarbeitung von HTTP-Anfragen in unserer Flask-Anwendung zu verwenden. Werkzeug bietet eine Reihe von Tools und Utilities, die die Bearbeitung von HTTP-Anfragen erleichtern, wie z.B. Request- und Response-Objekte, Routenführung und Fehlerbehandlung.

### Regarded options

Werkzeug: Werkzeug ist das Standard-WSGI-Toolkit für Flask und bietet grundlegende Funktionen für die Verarbeitung von HTTP-Anfragen und die Interaktion mit dem Webserver.


WSGIRef: WSGIRef ist eine Referenzimplementierung des WSGI-Standards für Python und bietet eine grundlegende Infrastruktur für die Entwicklung von WSGI-Anwendungen. Allerdings ist es weniger benutzerfreundlich als Werkzeug und erfordert mehr manuelle Konfiguration.
---


## 04: Verwendung von Jinja2 für das Template-Rendering

### Meta

Status
: **Decided** 

Updated
: 09-Feb-2024


### Problem statement

Wir müssen ein Template-Rendering-Tool für unsere Flask-Anwendung wählen, um dynamische Webseiten zu generieren.

### Decision

Wir haben uns entschieden, Jinja2 als Template-Rendering-Tool zu verwenden, aufgrund seiner Einfachheit, Flexibilität und Integration mit Flask. Jinja2 ermöglicht es uns, Templates mit Platzhaltern und Kontrollstrukturen zu erstellen, um dynamische Inhalte auf Webseiten zu generieren.

### Regarded options

Jinja2: Jinja2 ist das Standard-Template-Rendering-Tool für Flask und bietet eine einfache Syntax sowie eine Vielzahl von Funktionen zur Generierung von dynamischen Webseiten.


Mako: Mako ist ein alternatives Template-Rendering-Tool für Python, das ähnliche Funktionen wie Jinja2 bietet. Allerdings ist es weniger verbreitet und integriert sich nicht so nahtlos in Flask wie Jinja2.

---
