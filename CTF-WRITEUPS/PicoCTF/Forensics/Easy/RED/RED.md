Problema ne spune ca, *ROSU ROSU ROSU ROSU*, asa ca trebuie sa descarcam
imaginea pe care ne o da ei.

Sugestiile lor sunt:

1. Imaginea pare pură, dar este totuși?

2. Roșu?Ged?Pat?Aed?

3. Verifică cum se numește Facebook acum.


Rezolvare:

1. Descarcam imaginea aceea cu extensia .png, si apoi sa-l vizualizam imaginea
   cu comanda:

                          xdg-open red.png

  Si observam o imagine rosie dar e micuta de fel, nimic de ascuns acolo
  si am decis sa folosim si comanda:

                          exiftool red.png 
  Si ne afiseaza:

                         ...
                         Compression                     : Deflate/Inflate
                         Filter                          : Adaptive
                         Interlace                       : Noninterlaced
                         Poem                            : Crimson heart, vibrant and bold,.Hearts flutter at your sight..Evenings glow softly red,.Cherries burst with sweet life..Kisses linger with your warmth..Love deep as merlot..Scarlet leaves falling softly,.Bold in every stroke.
                         Image Size                      : 128x128
                         Megapixels                      : 0.016

   Interesant cand vedem o poezie acolo scris de un author, dar observam ca 
   e scris intetionat numa sa ne atraga intentia si de a decifra
   aceea poezie care iti pierzi timp-ul degeaba, nu? asa ca hai sa trecem
   cu comenzile noastre.

   Aceasta este poezia ce-i care sunt pasionati de asa ceva :)))

                         Inimă purpurie, vibrantă și îndrăzneață,. 
                         Inimile tresaltă la vederea ta.. 
                         Serile strălucesc ușor roșu,. 
                         Cireșele explodează de viață dulce.. 
                         Sărutările persistă odată cu căldura ta..  
                         Iubire profundă ca merlotul.. 
                         Frunze stacojii cad ușor,. 
                         Îndrăzneață în fiecare mângâiere. 


2. Dupa ce am analizat cu *exiftool* si vazut aceea poezie, am decis sa 
   folosim si o comanda, cum ar fi:

                            strings red.png

   Care ne afiseaza tot poezie, care atrage si mai multa atentie de gandit 
   acolo.


3. Ultima comanda si nu ceea din urma este:

                             zsteg red.png 

   Care ne afiseaza toate datele posibile din metadate si extrage tot din 
   imagine, si raspuns-ul ar fi asta:

                b1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdD
                                              FtNHQzX2N1cjNfZjByXzU0ZG4zNTVff
                                              Q==cGljb0NURntyM2RfMXNfdGgzX3Vsd
                                              DFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ
                                              ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFt
                                             NHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb
                                              0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N
                                               1cjNfZjByXzU0ZG4zNTVffQ=="
                b1,rgba,msb,xy      .. file: OpenPGP Public Key
                b2,g,lsb,xy         .. text: "ET@UETPETUUT@TUUTD@PDUDDDPE"  

---
!!! MAI PE SCURT

            Sa aflati mai multe despre zsteg, puteti sa cititi si la Zsteg.md
---

4. Dupa cum putem observa, la *b1,rgba,lsb,xy* avem un cod codificat, in base64
   si trebuie sa il decodificam, folosim comanda:

                                             echo -n "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d 
 
  Si afiseaza: 

                                               picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355}
-----

!!!BONUS!!!

Cum se instaleaza *zsteg* pe Linux:

Folositi comanda: 
 
                                              sudo gem install zsteg 

Iar daca aveti erroare dupa ce instalati, folositi si aceste comenzi:

                                               update --system
                                               sudo gem install rake
                                               sudo gem install zsteg

Iar daca nu functioneaza, apelati la google, ca acela e ajutorul vostru, multa bafta !!!


-----


*-----*

FLAG: picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355}

*-----*
