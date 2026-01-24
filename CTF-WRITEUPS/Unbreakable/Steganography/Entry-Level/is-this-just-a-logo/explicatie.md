Ne spune ca trebuie sa aflam ca exista mai mult decat logo

Pasi pentru rezolvare:

1. folosim cateva tool-uri pe care putem extrage informatii utile despre o imagine
   Tol-urile le gasiti tot aici, intr-un alt txt, tooluri.txt
   
1.1  primul tool ar fi acesta  (strings), head ---> ne arata primele 10 lini la inceput:

                              strings download.png | head
Ne afiseaza:

IHDR
sRGB
'tEXtComment
Building a better workig world
IDATx^
ZDk-
%""J
DDDDDDD
/ED|
yP\/


Vedem ca spune: Building a better workig world

2. Folosim un alt tool cel mai folosit este: exiftool 
   acest tool vedem cand a fost creat, dimensiunea imagini, structura si cateva indici si unde a fost localizat
    
                                  exiftool download.png
Ne afiseaza:


                            ExifTool Version Number         : 13.25
                            File Name                       : download.png
                            Interlace                       : Noninterlaced
                            SRGB Rendering                  : Perceptual
                            C omment                         : Building a better workig world
                            Image Size                      : 1000x416
                            M egapixels                      : 0.416



Vedem la coment cu : Building a better working world


Acesta este flag-ul gasit: Building a better workig world


