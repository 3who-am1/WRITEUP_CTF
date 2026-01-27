Dupa ce am rezolvat la bandit11 si am obtinut parola, putem sa ne conectam la bandit12

Parola pentru bandit12 il puteti gasi la bandit11.

Rezolvare:

1. Sa ne conectam la bandit12, folosim aceasta comanda:

              ssh bandit11@bandit.labs.overthewire.org -p 2220

   Si introducem parola gasita de la bandit11.

2. Dupa conectare, e sa citim enuntul problemei care ne spune asa:

                    Parola pentru nivelul care urmeaza este stocata
                    in fisierul `data.txt`, care este un hexdump al
                    unui fisier care a fost comprimat in mod repetat
                    Pentru a rezolva aceasta problema , e sa cream
                    niste directoare, sa le putem lucra,
                    trebuie sa folosim un (mkdir) cu un nume
                    greu de ghicit.
                    Sau mai bine folosim comanda: (mktemp -d).
                    Iar apoi sa copiem datele folosind comanda (cp)
                    , si sa redenumim cu aceasta comanda:
                    mv (read the manpages!)


 Dupa ce avem aceste date obtinue, trebuie sa si aplicam.

3. Stim ca avem fisierul `data.txt`, sa putem citi folosim comanda:

                     strings data.txt

   Si ne afiseaza:

 <p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/xxd12.png" width="50%"/></p>


  Vedem ca avem siruri de hex-uri.


```
REZUMAT PENTRU HEXDUMPS

Hexdumps sunt adesea folosite atunci când vrem să ne uităm la date care nu pot fi 
reprezentate în șiruri și, prin urmare, nu pot fi citite, 
așa că este mai ușor să ne uităm la valorile hex. Un hexdump are trei coloane principale. 
Prima arată adresa, a doua reprezentarea hexadecimală a datelor pe acea adresă și ultima arată 
datele reale ca șiruri (cu ‘.’ fiind valori hexadecimale care nu pot fi reprezentate ca șir). 
Există multe editori hexagonali, alegeți-l pe cel care vă place cel mai mult.

Pentru linia de comandă xxd poate fi folosit.
xxd <input_file> <output_file> creează hexdumps. 
Când utilizați -r flag, întoarce hexdump-ul.

Hexdumps poate fi folosit pentru a afla tipul unui fișier. 
Fiecare tip de fișier are un număr magic/semnătură fișier. Poti gasi liste cu o colecție a 
acestor semnături diferite de fișiere online. 
Acest lucru este deosebit de important de știut, deoarece uneori fișierele ar 
putea să nu aibă finalul corect sau orice fișier pentru a identifica tipul acestuia.

Compresie este o metodă de codificare care are ca scop reducerea dimensiunii originale a unui fișier fără a pierde informații (sau a pierde doar cât mai puțin posibil).

gzip este o comandă de comprimare sau decomprimare (-d) fișiere. 
Un fișier ‘gzip’ se termină în general cu .gz.
bzip2 este o altă comandă care permite comprimarea și decomprimarea (-d) fișiere. 
Un fișier ‘bzip2’ se termină în general cu .bz2.
An Fișier arhivă este un fișier care conține unul sau mai multe fișiere și metadatele acestora.
Acest lucru poate permite o portabilitate mai ușoară.

tar este o comandă care creează fișiere de arhivă (-cf). 
De asemenea, permite extragerea acestor fișiere din nou (-xf). 
O arhivă tar se termină în general cu .tar.

```


3. Dupa teorie si cred ca ati inteles ce este, hai sa trecem la rezolvarile noastre
   cum sa mentionat si in enunt, sa cream un director cu nume greu de ghicit.
   Si sa fim in direcotr-ul `/tmp` asa cum a fost mentionat in enunt

   Sa putem fi in director, sa cream un folder, si sa copiem `data.txt` in folderul creat 
 
   E sa folosim aceste comenzi, cum e si in imagine:

 <p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/creare12.png" width="50%"/></p>

   Dupa comenzile introduse, sa analizem ce sa format la `hexdump_data`

   Folosim comanda:

                                  strings hexdump_data | head 

   Si ne afiseaza:

 <p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/strings12.1.png" width="50%"/></p>


  Dupa analize, trebui sa inversam hexdump-ul, si sa obtinem date reale:

   Folosim aceste comenzi: 

                                xxd -r hexdump_data compressed_data
                                ls
  Si ne afiseaza:

                                compressed_data  hexdump_data
  
  Acum ca avem acel fisier creat, daca il citim cu comanda:

                                cat compressed_data 
 
  Ne afiseaza: 

 <p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/compre.png" width="50%"/></p>

  ```
Notă: După cum sa menționat în partea de teorie, datele reale nu pot fi citite, 
hexdump-ul este mult mai clar de vizualizat.
  ```

4. Acum trebuie sa decoprimam datele.
   
   Sa putem afla ce sa decoprimam, trebuie sa ne uitam la primi octeti pentru a gasi semnatura fisierului


5. Pentru `gzip` fisiere comprimate antetul este `\x1F\X8B\X08`, cum putem vedea la prima linie la `hexdump_data`,
   Observam ca este , si acum putem adauga sfarsitul corect al fisierului, redenumind fisierul si decoprima 
   fisierul cu `gzip -d`

   Folosim urmatoarele comenzi:

                               mv compressed_data compressed_data.gz
                               ls
   Ne afiseaza:

                              compressed_data.gz  hexdump_data

   Acum folosim comanda:

                               gzip -d compressed_data.gz
                               ls
   Ne afiseaza:

                                 compressed_data  hexdump_data
----
Ce am facut mai exact:

La fisierul `compressed_data` am modificat cu extensia `.gz`

Iar apoi cu comanda: `gzip -d` am extras fisierul din extensia `.gz`

---

6. Cu toate acestea, daca folosim comanda: 

                                    xxd compressed_data
  
   Observam ca la prima linie sa modificat, si de acolo pana la capat tot la fel a ramas:

                                    00000000: 425a 6839 3141 5926 5359 cc46 b52d 0000  BZh91AY&SY.F.-..


7. Dupa ce vedem ca sa modificat, observam ca la `BZ = 425a` este semnatrua pentru `bzip`, iar urmatori 
   doi octeti `h = 68`. Cu asta putem sa redenumim fisierul cu finalul de fisier corespunzator `(.bz2)` si il
   putem decoprima cu `bzip2 -d`

   Folosim urmatoarele comenzi:

                                     mv compressed_data compressed_data.bz2
                                     ls
 
   Si ne afiseaza asta:
 
                                     compressed_data.bz2  hexdump_data

   Folosim comanda pentru decoprimare a extensiei .bz2:

                                     bzip2 -d compressed_data.bz2
                                     ls
 
  Si ne afiseaza:

                                     compressed_data  hexdump_data

  Dupa toate aceste, vedem ca fişierul e încă comprimat. xxd arată că este ‘gzip’ comprimat din nou. 
  Așa că repetăm pașii anteriori, redenumind și decomprimând.

8. Repetam aceea comanda:

                                      mv compressed_data compressed_data.gz
                                      gzip -d compressed_data.gz
                                      strings compresse_data | xxd 

   si ne afiseaza:

  <p align="center"><img src="/CTF-WRITEUPS/OverTheWire/bandit/imagini/xxd12.2.png" width="50%"/></p>


   Observam ca nu e totul complet, dar vedem ca la prima linie este `data5.bin` care e un nume de fisier `binar`


9. Acum sa putem extrage aceea fila `data5.bin`, e sa folosim aceasta comanda:

                                      mv compressed_data compressed_data.tar
                                      tar -xf compressed_data.tar
                                      ls

  Si ne afiseaza:
   
                                       compressed_data.tar  data5.bin  hexdump_data


  Acum sa vedem ce se afiseaza, vedem ca e alt fisier cu numele `data6.bin` dupa ce am folosit comanda:

                                      strings data5.bin | xxd


10. Folosim iar comanda:

                                         mv data5.bin data5.bin.tar
                                         tar -xf data5.bin.tar
                                         ls
   
   Si ne afiseaza:
 
                                          compressed_data.tar  data5.bin.tar  data6.bin  hexdump_data

 Observam ca avem `data6.bin`, iar apoi sa folosim comanda aceasta:

                                           bzip2 -d data6.bin

 Ne afiseaza acest mesaj: 
 
                                            bzip2: Can't guess original name for data6.bin -- using data6.bin.out

  Iar daca folosim comanda:

                                        strings data6.bin.out 

  Ne sppune ca mai este un alt fisier, si acela e:  `data8.bin`


11. Folosim comanda:

                                         tar -xf data6.bin.out
                                         ls

   Ne afiseaza:
 
                                           compressed_data.tar  data5.bin.tar  data6.bin.out  data8.bin  hexdump_data


Acum ca avem `data8.bin` e sa modificam si sa aiba extensia `.gz`

Folosim urmatoarele comenzi: 

                                            mv data8.bin data8.gz
                                            ls
                                            gzip -d data8.gz
                                            cat data8

Si ne afiseaza:
 
                                           The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn


### Rețetă pentru hexdump + compresie repetată:

1. `xxd -r` → inversează hexdump-ul

2. `file` sau `xxd | head` → verifică semnătura

3. `mv` → adaugă extensia corectă (.gz, .bz2, .tar)

4. `gzip -d` / `bzip2 -d` / `tar -xf` → decomprimă

5. Repeti de la pasul 2 până obții text clar


----
Greu, nu?
incet incet, puteti invata de toate
----
---
Felicitari, ai rezolvat acest challenge

Mentionez faptul ca cu aceasta parola ne putem loga la bandit13
----
SUCCES mai departe :)))


 
