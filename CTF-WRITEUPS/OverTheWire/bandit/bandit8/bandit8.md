Dupa ce am rezolvat la bandit7 si am obtinut parola, putem sa ne conectam la bandit8

Parola pentru bandit8 il puteti gasi la bandit7.

Rezolvare:

1. Sa ne conectam la bandit8, folosim aceasta comanda:

              ssh bandit8@bandit.labs.overthewire.org -p 2220

Si introducem parola gasita de la bandit7.


2. Dupa ce ne-am conectat, folosim comanda aceasta:

                      ls -la 

  Ne afiseaza asta:

<p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/lscomanda8.png" width="50%"/></p>


Observam ca avem un fisier de tip *data.txt*

3. Daca folosim comanda:

                                cat data.txt
  
  Ne afiseaza:

<p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/catcomanda8.1.png" width="50%"/></p>


O groaza de parola, aliniate, dar nu stim care e ceea corecta, tinand cont ca enuntul
problemei ne spune ca: ( `este o singura linie de text care apare o singura data` )

Asa ca folosim aceasta comanda:

                                  sort data.txt | uniq -c

Si ne afiseaza asta:

<p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/sortcomanda8.2.png" width="50%"/></p>


Observam ca ne afiseza multe parole care se repeta, acela aratand cu `10` si numa o parola care nj se repeta si e una singura care chiar nu se repeta are cifra `1` si acela ar fi:

                               1 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM



---
`EXPLICATIE LA COMENZILE UTILIZATE`

1. `sort` este de a sorta in ordine de la a la z

2. `uniq` este de arata cate ori sa repetat acele fraze.

--- 

Felicitari, ai rezolvat acest challenge

Mentionez faptul ca cu aceea parola ne putem loga la bandit9
----
SUCCES mai departe :)))
---

  
