Avem parola ceea ce a fost stocata in fisierul *readme* la *bandit0*, si fiecare challenge rezolvat, unde gasim un sir de caractere, ila e parola, si cu fiecare challenge rezolvat
putem sa ne conectam si la *bandit1*, *bandit2* si tot asa.


Rezolvare:

1. Introducem aceasta comanda pentru a ne conecta la *bandit1*:

                               ssh bandi1@bandit.labs.overthewire.org -p 2220

   cu parola acesta: *ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5I*
 
   Dupa ce ne conectam, vedem ca se deschide un prompt


2. Introducem comanda:

                             ll

  Si vedem ca ne afiseaza:

<p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/imagini/llcomanda1.png" width="50%"/></p>


Sa putem afla ce se afla in acel fisier *-*, e sa folosim comanda *strings* sau *cat*

                            strings /home/bandit1/- 

Ne afiseaza: 263JGJPfgU6LtdEvgfWU1XP5yac29mF

--
!! Bonus!!

Poate va intrebati de ce nu am folosit direct:

                               strings -

E ca ne afiseaza toate optiunile cum sa folosim comanda *strings*, si nu ne afisa raspuns-ul dat.

Iar la *cat* e ca se asteapta sau ruleaza in gol, fara sa ne de-a un raspuns

Iar ca am scris comanda:

                           strings /home/bandit1/-
                                    sau
                           cat /home/bandit1/-


Faptul ca am scris si */home/bandit1/-*, am mentionat ce as dori sa aflu eu la un fisier.

Sper ca ati inteles !!

---


Mentionez faptul ca cu aceea parola aflata, putem sa ne conectam la *bandit2*


Bafta :)))


