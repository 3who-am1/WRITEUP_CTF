# Forensics – CTF Writeups

Această secțiune este dedicată **Digital Forensics** în context CTF (Capture The Flag). Aici documentez metode reale de analiză, gândire investigativă și pași tehnici folosiți pentru a rezolva challenge-uri de tip forensics, exact așa cum se întâmplă într-o investigație din lumea reală.

Scopul nu este doar rezolvarea exercițiilor, ci **formarea mentalității unui forensic analyst / threat hunter**: observare, corelare de artefacte, validare și concluzii bazate pe dovezi.

---

## Ce este Digital Forensics

Digital Forensics reprezintă procesul de:

* colectare
* analiză
* interpretare
* documentare

al dovezilor digitale, astfel încât acestea să poată fi folosite pentru:

* identificarea unui atac
* analiza malware
* atribuirea unei activități malițioase
* înțelegerea impactului

În CTF-uri, aceste concepte sunt simulate prin fișiere, loguri, imagini de disc, dump-uri de memorie sau artefacte de rețea.

---

## Structura repository-ului

```
Forensics
    ├── Easy
    │   └── i-got-a-virus
    │       ├── imagini
    │       │   ├── creatia-fisierului.png
    │       │   ├── ip-rauintentionat.png
    │       │   └── VirusTotalFamily.png
    │       └── README.md
    ├── Entry-Level
    │   └── basic-coms
    │       ├── imagini
    │       │   ├── Detail.png
    │       │   ├── Hex.png
    │       │   ├── http.png
    │       │   ├── StreamHTTP.png
    │       │   └── wireshark.png
    │       └── README.md
    ├── Medium
    │   └── forensics-disk
    │       ├── flag.txt
    │       └── README.md
    └── README.md

```

### De ce această structură

* **Claritate** – fiecare challenge este izolat
* **Scalabilitate** – ușor de extins
* **Indexare SEO** – Google indexează README-urile individual
* **Profesionalism** – seamănă cu documentație reală

---

## Niveluri de dificultate

### Entry-level

* Noțiuni de bază
* Observație și logică
* Fișiere simple

### Easy

* Introducere în tool-uri forensics
* Analiză de bază (hash, metadata, strings)

### Medium

* Corelare de artefacte
* Analiză malware statică
* Loguri și trafic de rețea

### Hard

* Analiză avansată
* Timeline reconstruction
* Atacuri complexe

### Insane

* Gândire critică
* Simulări realiste
* Multiplă sursă de dovezi

---

## Ce vei găsi în aceste writeup-uri

### Analiză fișiere

* tip fișier (file)
* entropie
* strings
* structură internă

### Malware Forensics

* hash-uri (MD5 / SHA1 / SHA256)
* semnături
* familie malware
* comportament suspect

### Metadata

* timestamp-uri
* autor
* sistem de operare
* tool-uri folosite

### Network Forensics

* IP-uri malițioase
* ASN & geolocație
* conexiuni suspecte
* trafic anormal

### Memory & Disk Analysis

* fișiere șterse
* procese ascunse
* artefacte persistente

### Threat Intelligence

* VirusTotal
* reputație IP
* corelare cu atacuri cunoscute

---

## Tool-uri utilizate

* strings / file / hexdump
* exiftool
* binwalk
* VirusTotal
* Wireshark
* Autopsy
* Volatility
* grep / awk / sed

---

## Structura unui writeup individual

Fiecare challenge conține un README.md propriu cu:

* Nume challenge
* Platformă (CyberEDU)
* Categorie
* Dificultate
* Descriere
* Analiză pas cu pas
* Dovezi (imagini)
* Concluzie

Această abordare reflectă **raportarea profesională din forensics**.

---

## De ce acest repository

* Arată procesul de gândire, nu doar răspunsul
* Demonstrează competență reală
* Este util pentru recrutori și CTF players
* Creează o amprentă digitală profesională

---

## Disclaimer

Toate materialele sunt folosite exclusiv în scop educațional.
Nu încurajez activități ilegale.

---

> "Forensics is not about guessing. It’s about evidence."
