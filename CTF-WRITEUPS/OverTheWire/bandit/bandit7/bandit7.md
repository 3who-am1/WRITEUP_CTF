Dupa ce am rezolvat la bandit6 si am obtinut parola, putem sa ne conectam la bandit7

Parola pentru bandit7 il puteti gasi la bandit6.

Rezolvare:

1. Sa ne conectam la bandit7, folosim aceasta comanda:

            ssh bandit6@bandit.labs.overthewire.org -p 2220

  Si introducem parola gasita de la bandit6.

2. Dupa ce ne-am conectat, folosim comanda aceasta:

                              ls -la

  Si afiseaza asta:
 
<p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/lscomanda7.png" width="50%"/></p>
 

Observam ca avem un fisier de tip *data.txt*


3. Daca folosim comanda:

                            cat data.txt

  Afiseaza multe, dar multe parole, unele gresite, numa una e corecta.
  
  Dupa enunt ne spune ca e un cuvant langa *millionth*, dar nu stim unde

  Enuntul ne da niste sugesti de comenzi precum:

                       grep, man, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd


4. Dupa sugestiile lor, vedem ca este mentionat *grep*
   
   Folosim comanda:

                        grep "millionth" data.txt

   Si ne afiseaza:

                       millionth       dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc


---
Felicitari, ai rezolvat acest challenge

Mentionez faptul ca cu aceea parola ne putem loga la bandit8

---
SUCCES mai departe :)))
---

