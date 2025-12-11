Vedem ca trebuie sa descarcam un fisier de tip .png si sa vizualizam imaginea

pasi de rezolvare:

1. folosim exiftool, nu vedem ceva important doar ca la filter e ceva Adaptive 
2. folosim strings pentru metadate. nici-o informatie, doar siruri multe
3. folosim comanda xxd see.png, dar nici acolo ceva important de aflat, la final ce putem vedea .IEND.B
4. Deschidem imaginea si observam ca e o imagine de la mare, si vedem ceva scris acolo, acela e flag-ul
   dar e neclar, si neputand citind din aceea imagine

Explicatie:


1. Accesam site-ul: *https://georgeom.net/StegOnline/image*

2. Inseram imaginea si rulam la Red 5, vedem ca arata putin flag-ul dar pe final si aceea ar fi:

                                                           19d894dda0c8a7} ---> e doar o parte din flag (4)

3. Daca ne uitam la imagine normala vedem la inceput flag-ul:

                                                           ctf{335769a99feec ---> e doar o parte din flag (1)

   Vedem ca mai departe e totul neclar, asa trebuie sa apelam la niste tool-uri avansate:


4. Mai e un site avansat excesiv pentru analiza imaginilor se numeste: *https://29a.ch/photo-forensics/#forensic-magnifier*

5. inseram imaginea si ne ducem la Principal Component Analysis
   Si introducem asa la fiecare aparte: 

                                                     Input: Color
                                                     Mode: Projection
                                                     Component: 2
                                                     Linearize: bifat
                                                     Invert: bifat
                                                     Enchancement: Equalize Histogram
                                                     Opacity: 1.00

Observam ca sa inversat imaginea si e putin mai clar flag-ul
   
                                                          ef5e55ac464fe30a7c215856bc ---> o parte din flag (2)

   Acum ca am citit putin mai mult din flag, e sa modificam putin la Principal Component Analysis
   Sa putem descoperi urmatorul sir din flag 

6. Urmatorul ar fi:
   
                                                Input: Color
                                                Mode: Difference
                                                Component: 2
                                                Linearize: nebifat
                                                 Invert: bifat
                                               Enchancement: Stretch Contrast
                                               Opacity: 1.00

Observam ca putem citi si urmtorul sir de caractere din flag, si acel ar fi:

                                              4b8eb67b0e0 ---> o parte din flag (3)


SUCCESS !!! :)

---
FLAG: ctf{335769a9feecef5e55ac464fe30a7c215856bc4b8eb67b0e019d894dda0c8a7}
---
