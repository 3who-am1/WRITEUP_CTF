Dupa ce am rezolvat la bandit10 si am obtinut parola, putem sa ne conectam la bandit11

Parola pentru bandit11 il puteti gasi la bandit10.

Rezolvare:

1. Sa ne conectam la bandit11, folosim aceasta comanda:

          ssh bandit11@bandit.labs.overthewire.org -p 2220

   Si introducem parola gasita de la bandit10.

2. Dupa ce ne-am conectat, folosim comanda aceasta:

                  ls -la 

   Si ne afiseaza:

 <p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/lscomanda8.png" width="50%"/></p>

Observam ca avem un fisier de tip `data.txt`

3. Daca folosim comanda:

                  cat data.txt

   Ne afiseaza:

                 Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4                                  

Observam ca sa rotit caracterele in Rot13, iar noi trebuie sa decifrem mesajul rotit cu 13 poziti


4. Pentru a decifra mesajul folosim comanda:

               echo -n "Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4" | rot13

  Daca nu functioneaza pe terminal cu aceea comanda, puteti sa
  accesati si de pe site-ul *cyberchef.com*

  Cum e in aceasta imagine de mai jos:

 <p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/cyberchef11.png" width="50%"/></p>


---
`BONUS`: 
  
  Iar pentru cei care nu au rot13 pe terminal si doresc sa aibe
  puteti creea un alias, cum e comanda de mai jos:

                       alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"

  Si apoi puteti aplica comanda pe care am mentionat mai sus.
---

si afiseaza acest mesaj:

The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4


---
Felicitari, ai rezolvat acest challenge

Mentionez faptul ca cu aceasta parola ne putem loga la bandit12
---

SUCCES mai departe :)))
----


