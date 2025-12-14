Dupa ce am rezolvat la bandit8 si am obtinut parola, putem sa ne conectam la bandit9

Parola pentru bandit9 il puteti gasi la bandit8.

Rezolvare:

1. Sa ne conectam la bandit9, folosim aceasta comanda:

                 ssh bandit9@bandit.labs.overthewire.org -p 2220

  Si introducem parola gasita de la bandit8.


2. Dupa ce ne-am conectat, folosim comanda aceasta:

                             ls -la
 
   Ne afiseaza asta:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/lscomanda8.png" width="50%"/></p>


   Observam ca avem un fisier de tip `data.txt`

3. Daca folosim comanda:

                                    cat data.txt

   Ne afiseaza:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/catcomanda9.1.png" width="50%"/></p>


  Observam ca ne afiseaza numa caractere ciudate, greu de decifrat, asa ca folosim comanda:

                                      strings data.txt

   Si ne afiseaza asta:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/stringscomanda9.2.png" hight="50%"/></p>


  multe caractere dar putem sa le citim, enuntul problemei ne spune ca e ceva legat de asta `==` 

  Si am decis sa folosim comanda completa de a putea decifra este:

                                      strings data.txt | grep ==

  SI ne afiseaza asta:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/stringscomanda9.3.png" width="50%"/></p>


  Observam ca avem parola si aceea este:

                                       FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey


----
Felicitari, ai rezolvat acest challenge

Mentionez faptul ca cu aceea parola ne putem loga la bandit10
---

SUCCES mai departe :)))
----


