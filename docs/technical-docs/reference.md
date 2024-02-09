---
title: Reference
parent: Technical Docs
nav_order: 4
---



# Reference documentation
{: .no_toc }



<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Funktionen zur Verwaltung von Aufgaben (To-Do-Listen)

### `function_definition()`

**Route:** `/2DO/`

**Methods:** `/POST GET/`

**Purpose:** Ermöglicht Benutzern das Hinzufügen und Anzeigen von Aufgaben in ihrer To-Do-Liste.

**Route:** /delete_task/int:index

**Methods:** ` /GET/`

**Purpose:** Löscht eine Aufgabe aus der To-Do-Liste anhand ihres Index.


**Sample output:**

![2DO](../assets/images/2DO.png)


---

## Funktionen zur Verwaltung von Ereignissen (Kalender)

**Route:** ` /2DATE/`

**Methods:** `POST GET`

**Purpose:** Ermöglicht Benutzern das Hinzufügen und Anzeigen von Ereignissen in ihrem Kalender.

**Route:**  /view_document/<filename>

**Methods:** GET

**Purpose:** Zeigt das hochgeladene Dokument mit dem angegebenen Dateinamen an.

**Sample output:**

![2DATE](../assets/images/2DATE.png)
![2DATE2](../assets/images/2DATE2.png)

---

### Funktionen zur Verwaltung von Dokumenten und Notizen

**Route:** `/2DOC/` 

**Methods:** POST GET

**Purpose:** Ermöglicht Benutzern das Hochladen von Dokumenten und das Hinzufügen von Notizen.


**Route:** /view_document/<filename>

**Methods:** GET

**Purpose:** Zeigt das hochgeladene Dokument mit dem angegebenen Dateinamen an.



**Sample output:**

![2DOC](../assets/images/2DOC.png)

---

