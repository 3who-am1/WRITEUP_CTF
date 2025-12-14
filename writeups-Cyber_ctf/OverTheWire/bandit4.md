Dupa ce am rezolvat la *bandit3* si am obtinut parola, putem sa ne conectam la *bandit4*

Parola pentru *bandit4* il puteti gasi la *bandit3*.

Rezolvare:

1. Sa ne conectam la *bandit4*, folosim aceasta comanda:

                          ssh bandit4@bandit.labs.overthewire.org -p 2220

  Si introducem parola gasita de la *bandit3*.


2. Dupa ce ne-am conectat, folosim aceasta comanda:

                                 ll

  Si ne afiseaza:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/llcomanda3.png" width="50%"/></p>


Observam ca avem un folder, folosim aceasta comanda:

                                 ll inhere

  Si ne afiseaza:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/llcomanda4.1.png" width="50%"/></p>


Vedem ca avem multe fisiere de la *00* pana la *09*


3. Comanda ceea mai usoara sa ne afiseze tot ce contine in acele fisiere, decat sa repeti fiecare data aceeasi comanda, putem folosi:
   folosim comanda aceasta:

                                 strings inhere/*

   Si ne afiseaza:

                               6);/:
                               Y["#
                               4QYVPkxZOOEOO5pTW81FB8j8lxXGUQw 
                               [h+|

---
!!BONUS!!

1. *strings*  ---> afiseaza toate mesajele aflate, chiar si cele binare
2. (*)        ---> sunt pentru toate fisierele
3. */*        ---> este directorul aflat cu mai multe fisiere.


---
Felicitari, ai rezolvat acest challenge

Mentionez faptul ca cu aceea parola ne putem loga la *bandit5*.

Succes mai departe :))))
---
