Descrierea ne spune ca:

Scopul acestuia e sa ne logam folosind *SSH*. 
Gazda sa ne putem conecta este:

                          bandit.labs.overthewire.org
Pe portul

                                2220

Iar numele de utilizator este:

                              bandit0

Odata ce ne autentificam, putem accesa nivelul 1.


Dupa ce avem aceste informati folosim comanda aceasta:

                         ssh bandi0@bandit.labs.overthewire.org -p 2220
---
Explicatie: 

1. *bandit0* este numele de utilizator. 
2. *@* separator intre user si host(bandit.labs.overthewire.org) 
3. *bandit.labs.overthewire* adresa serverului, adica host
4. *-p* este specificarea portului.
5. *2220* acesta e portul
6. Si parola pentru *bandit0* este *bandit0*.

---


Dupa ce ai rulat comanda si ai introdus parola *bandit0*, ne va arata un prompt ca aceasta:

                                       bandit0@bandit:~$ 


Acum introducem comanda:

                                     ll

Si observam ca ne afiseaza cu:

                                   -rw-r--r--   1 root    root    3851 Oct 14 09:19 .bashrc
                                   -rw-r--r--   1 root    root     807 Mar 31  2024 .profile
                                   -rw-r-----   1 bandit1 bandit0  438 Oct 14 09:25 readme

Acum sa vedem ce se afla in acel fisier *readme*, folosim comanda:

                                  cat readme

Si ne afiseaza parola:

                 The password you are looking for is: ZLjTmM6FvvyRnrb2rfNWOZOTa6ip5If


Cu aceea parola ne putem conecta la *bandit1*




Challenge rezolvat !!!
Bafta :)))
