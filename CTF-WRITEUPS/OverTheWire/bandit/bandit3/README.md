# Bandit Level 2 → Level 3 | bandit3 | Writeup

**DESCRIEREA EXERCITIULUI:**

Parola pentru nivelul următor este stocată într-un fișier ascuns în aici director.

## Comenzi care poate fi necesar pentru a rezolva acest nivel:

       ls , cd , cat , file , du , find

### REZOLVARE:

Dupa ce am rezolvat la *bandit2* si am obtinut parola, putem sa ne conectam la *bandit3*.

Parola pentru *bandit3* il puteti gasi la *bandit2*

1. Sa ne conectam la *bandit3*, folosim aceasta comanda:

                             ssh bandit3@bandit.labs.overthewire.org -p 2220

  Si introducem parola gasita de la *bandit2*.


2. folosim aceasta comanda:

                               ll

  Si ne afiseaza:

<p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/llcomanda3.png" width="50%"/></p>

 
Observam ca avem un folder, si problema ne spune ca parola este stocata in folderul *inhere*

Asa ca, hai sa exploram, folosim comanda aceasta:

                              ll inhere

Si ne afiseaza:

                            -rw-r----- 1 bandit4 bandit3   33 Oct 14 09:26 ...Hiding-From-You


3. Ar trebui sa aflam ce se ascunde acolo, asa ca folosim comanda:

                              cat inhere/...Hiding-From-You

  Si ne afiseaza: 
 
                                   2WmrDFRmJIq3IPxneAaMGhap0pFhF3N
---
!!Bonus!!

##Notă: 
1. Fișierul `.Hiding-From-You` începe cu punct, ceea ce îl face **hidden file**, adica sa fie ascuns.
 
2. în Linux. De obicei, hidden files nu apar la `ls` simplu, dar la `ll` (alias pentru `ls -la`) apar.

---

Acest challenge e rezolvat.

Mentionez faptul ca cu aceea parola ne putem loga la *bandit4*

Bafta :)))


