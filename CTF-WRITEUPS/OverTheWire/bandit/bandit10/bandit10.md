Dupa ce am rezolvat la bandit9 si am obtinut parola, putem sa ne conectam la bandit10

Parola pentru bandit10 il puteti gasi la bandit9.

Rezolvare:

1. Sa ne conectam la bandit10, folosim aceasta comanda:

                 ssh bandit10@bandit.labs.overthewire.org -p 2220

  Si introducem parola gasita de la bandit9.


2. Dupa ce ne-am conectat, folosim comanda aceasta:

                                   ls -la 

  Si ne afiseaza:

<p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/lscomanda8.png" width="50%"/></p>

  Observam ca avem un fisier de tip `data.txt`

3. Daca folosim comanda:

                                cat data.txt

  Ne afiseaza: 

                               VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==

  Observam ca este codificat in Base64, iar noi trebuie sa il decodificam

4. Pentru a decodifica acel mesaj, folosim comanda:

                             echo -n "VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==" | base64 -d

  Ne afiseaza acest mesaj:

                                The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

---
`EXPLICATIE SCURTA`

1. `echo` → afișează text pe terminal

2. `-n` → opțiune care spune lui `echo` să **NU** adauge un "newline" (`\n`) la final (important pentru decodare corectă)

3. `"string"` → textul pe care vrei să-l procesezi (în cazul nostru, codul Base64)

4. `|` → **pipe**; trimite output-ul comenzii din stânga ca input comenzii din dreapta

5. `base64` → utilitarul care codează/decodează Base64

6. `-d` → opțiune pentru **decode** (decodare); implicit, `base64` codează


Cu toate acestea explicatii  sa format aceea comanda pe care noi l-am folosit 
 
---
Felicitari, ai rezolvat acest challenge

Mentionez faptul ca cu aceea parola ne putem loga la bandit11
---

SUCCES mai departe :)))
----
