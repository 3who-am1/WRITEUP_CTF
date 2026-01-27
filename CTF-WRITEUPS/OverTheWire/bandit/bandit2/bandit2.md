Dupa ce am rezolvat la *bandit1* si am obtinut parola, putem conecta la *bandit2*.

Parola pentru *bandit2* puteti gasi la *bandit1*

Rezolvare:

1. Sa ne conectam la *bandit2*, folosim aceasta comanda:

                            ssh bandit2@bandit.labs.overthewire.org -p 2220

  Si introducem parola gasita de la *bandit1*.


2. folosim aceasta comanda:

                              ll

   Si ne afiseaza: 

<p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/llcomanda2.png" width="50%"/></p>


Observam ca avem un fisier *--spaces in this filename--*


3. Sa putem face acest challenge, procedam cum am procedat si la *bandit1*
   Cu aceasta comanda:

                              strings ./--spaces\ in\ this\ filename--

   Si ne afiseaza: 

                              MNk8KNH3Usiio41PRUEoDFPqfxLPlSm 

---
!!Bonus !!

Poate va intrebati de ce e scris cu: 

                              /--spaces\ in \ this\ filename--

Asa a fost introdus dupa ce am scris comanda: *./--* si am apasat pe TAB(sa completeze automat).

--- 

Mentionez faptul ca cu aceea parola aflata, putem conecta la *bandit3*

Bafta :)))
