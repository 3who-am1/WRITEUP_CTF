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

 <p align="center"><img src="/writeups-Cyber_ctf/OverTheWire/bandit/imagini/xxd12.png" width="50%"/></p>


  Vedem ca avem siruri de hex-uri.


```REZUMAT PENTRU HEXDUMPS

Hexdumps sunt adesea folosite atunci când vrem să ne uităm la date care nu pot fi reprezentate în șiruri și, prin urmare, nu pot fi citite, așa că este mai ușor să ne uităm la valorile hex. Un hexdump are trei coloane principale. Prima arată adresa, a doua reprezentarea hexadecimală a datelor pe acea adresă și ultima arată datele reale ca șiruri (cu ‘.’ fiind valori hexadecimale care nu pot fi reprezentate ca șir). Există multe editori hexagonali, alegeți-l pe cel care vă place cel mai mult.

Pentru linia de comandă xxd poate fi folosit. xxd <input_file> <output_file> creează hexdumps. Când utilizați -r flag, întoarce hexdump-ul.

Hexdumps poate fi folosit pentru a afla tipul unui fișier. Fiecare tip de fișier are un număr magic/semnătură fișier. Poti gasi liste cu o colecție a acestor semnături diferite de fișiere online. Acest lucru este deosebit de important de știut, deoarece uneori fișierele ar putea să nu aibă finalul corect sau orice fișier pentru a identifica tipul acestuia.


```


