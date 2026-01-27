Dupa ce am rezolvat la bandit5 si am obtinut parola, putem sa ne conectam la bandit6

Parola pentru bandit6 il puteti gasi la bandit5.

Rezolvare:

1. Sa ne conectam la bandit6, folosim aceasta comanda:

                   ssh bandit6@bandit.labs.overthewire.org -p 2220
  Si introducem parola gasita de la bandit5.

2. Dupa ce ne-am conectat, folosim comanda asta:

                     ls -la
   
   Si afiseaza asta: 

<p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/lscomanda6.png" width="50%"/></p>

  Si observam ca nu avem nimic, unde sa putem afla parola.

3. Analizam enuntul problemei ce ne spune, si zice ca:

                    Parola este stocata intr-un server, si are proprietatile urmatoare:
                    este detinut de grupul bandit6
                    are 33 de octeti
                    este detinut de utilizatorul bandit7


  Asa ca suntem nevoiti sa folosim aceasta comanda:

                 find / -group bandit6 -user bandit7 -size 33c 2>/dev/null

  Si ne afiseaza:

                   /var/lib/dpkg/info/bandit7.password

4. Acum ca am aflat unde se poate afla, putem folosi comanda urmatoare:

                     strings /var/lib/dpkg/info/bandit7.password

Si ne afiseaza asta:    
 
                      morbNDkSW6jIlUc0ymOdMaLnOlFVAaj

---
!!EXPLICATIE LA COMANDA FOLOSITA

1. find / -group bandit6 -user bandit7 -size 33c 2>/dev/null

  find ---> de a cauta, ceea ce ai tu nevoie

  /    ---> radacina directorului

  -group si -user  ---> enuntul din aceea problema

  -size  ---> de a cauta acei octeti ca din enunt

  2>/dev/null ---> de a nu afisa care nu este permis, se incarca aiurea pe terminal

----

Felicitari, ai rezolvat acest challenge

Mentionez faptul ca cu aceea parola ne putem loga la *bandit7*

---
SUCCES mai departe :)))
---


