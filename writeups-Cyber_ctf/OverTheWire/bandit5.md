Dupa ce am rezolvat la *bandit4* si am obtinut parola, putem sa ne conectam la *bandit5*

Parola pentru *bandit5* il puteti gasi la *bandit4*.

Rezolvare:

1. Sa ne conectam la *bandit5*, folosim aceasta comanda:

                          ssh bandit5@bandit.labs.overthewire.org -p 2220

  Si introducem parola gasita de la *bandit4*.


2. Dupa ce ne-am conectat, folosim aceasta comanda:

                               ll

   Si ne afiseaza:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/llcomanda3.png" width="50%"/></p>


Observam ca avem un folder, folosim aceasta comanda:

                              ll inhere

Si ne afiseaza:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/llcomanda5.1.png" width="50%"/></p>


Vedem ca avem multe foldere, de la *00* pana la *19*.

3. sa vedem ce se afiseaza in acele foldere, folosim aceasta comanda:

                           ll inhere/maybehere00; ll inhere/maybehere01

  Si ne afiseaza asta:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/llcomanda5.2.png" width="50%"/></p>


Dupa ce am analizat, observam ca la fiecare fisier *executabil* care este *-file1* sau cum se observa fiecare permisiune *-rwxr-x---* 
vazand care incepe cu *x*, astea se numesc executabile.

Enuntul ne spune ca: Parola se afla intrun director la o fila care nu este *EXECUTABIL* si sa contina *1033 de octeti*.

In cazul nostru, din imaginea de sus la *maybehere00 si la 01* nu vedem niciun octet cu *1033*.

Trebuie sa exploram, sa putem gasi.

 
4. Sa putem rezolva direct acest challenge, folosim comanda aceasta:

                      ll inhere/* | grep 1033

  Si ne afiseaza: 

-rw-r-----  1 root bandit5 1033 Oct 14 09:26 .file2


Dupa ce ca am aflat, dar nu vedem in ce director se afla, putem
folosi si aceasta comanda utila:

                   ll inhere/*/.file2

Si ne afiseaza:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/llcomanda5.3.png" width="50%"/></p>

Acum ca am aflat in ce directoare se poate afla, putem folosi urmatoarea comanda.

5. Folosim comanda aceasta:

                    ll inhere/*/.file2 | grep 1033

  Si ne afiseaza:

                    -rw-r----- 1 root bandit5 1033 Oct 14 09:26 inhere/maybehere07/.file2


Dupa ce am gasit acei octeti, cum spune si in cerinta *1033*, putem citi acel fisier.

Folosim comanda: 

                    strings inhere/maybehere07/.file2

Si ne afiseaza:

                          HasnPhtq9AVKe0dmk45nxy20cvUa6EG

---
!!EXPLICATIE LA FIECARE COMANDA


1. ll inhere/* | grep 1033 

1.1:  Comanda *grep* e sa caute ceea ce ai tu nevoie prin multe fisiere si foldere
1.2:  /*  ----> aceasta este directorul care citeste tot ce contine in el cu ajutorul (*)

2. ll inhere/*/.file2

2.1: /*/.file2    ----> ne spune unde se afla si in ce folder.

3. ll inhere/*/.file2 | grep 1033

3.1: aici am folosit in plus cu *grep 1033* pentru a cauta acei octeti

4. strings inhere/maybehere07/.file2

4.1: Comanda *strings* sa citeasca ce e in acel fisier.

---

----
!!EXPLICATIE LA FIECARE APARTE DE PERMISIUNI, EXECUTABILE, ETC


1. drwxr-xr-x

  d ---> folder
  r ---> citire
  w ---> scriere
  x ---> executabil

---

Felicitari ai rezolvat acest cahllenge

Mentionez faptul ca cu aceea parola ne putem loga la *bandit6*.

---
SUCCES mai departe :)))
---
