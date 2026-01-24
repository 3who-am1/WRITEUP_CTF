**Zsteg** este un tool de detectare a steganografiei în imagini. 
Analizează date ascunse în biți sau canale de culoare.

Ce face?

1. Scanează biții individuali din fiecare pixel al unei imagini

   1.1 Extrage date ascunse în:

                           LSB (Least Significant Bit - cel mai puțin semnificativ bit) - cel mai folosit

                           Diverse combinații de canale (roșu, verde, albastru, alfa)

                           Ordine diferite (MSB/LSB - most/least significant bit)

   1.2 Detectă automat formate comune:
 
                           Text ASCII

                           Base64

                           Fișiere ZIP/PNG/PDF etc.

                           Checksum-uri

2. Când se folosește?

   2.1 În CTF-uri și investigații securitate, când:

                           Bănuiești că o imagine are ceva ascuns

                           Metadatele (exiftool) și strings-urile nu arată nimic

                           Provocarea sugerează steganografie (menționează "ascuns", "secret", "bit-uri")

                           Imaginea pare suspectă (dimension neobișnuit, culori uniforme)

3. Pe ce fișiere funcționează?

   3.1 Formate principale:

                           PNG - cel mai des folosit (suport canale multiple, transparență)

                           BMP - funcționează bine (format necomprimat)

                           GIF - limitat (paletă de culori)

   3.2 Formate cu probleme:

                           JPG/JPEG - NU recomandat (pierde date prin compresie)

                           SVG - nu are sens (format vectorial)

                           WEBP, HEIC - support limitat

   3.3 Exemplu logic simplu:

                          Imaginează-ți că fiecare pixel are o culoare ca un cod RGB: (255, 0, 127)

   3.4 zsteg verifică ultimii biți din fiecare număr:

                            255 în binar: 11111111 → ultimul bit e 1

                            0 în binar: 00000000 → ultimul bit e 0

                            127 în binar: 01111111 → ultimul bit e 1

4. Dacă citești toți ultimii biți din toți pixelii: 1 0 1 0 1 1 0 0... poți forma caractere ascunse.

   4.1 Comenzi uzuale:

                            bash
                            # Scanare completă (toate combinațiile)
                            zsteg imagine.png

                            # Scanare rapidă (doar setări comune)
                            zsteg -a imagine.png

                            # Extragere directă a datelor
                            zsteg -E "b1,rgba,lsb,xy" imagine.png > extras.bin
5. De ce e util?

   Pentru că ochiul uman nu vede diferențe mici în culori (schimbarea LSB-ului schimbă culoarea cu ±1), 
   dar calculatorul poate extrage aceste date să construiască mesaje, flag-uri, sau chiar fișiere întregi.

   Regula de bază: Când vezi o imagine într-un CTF și nu găsești flag-ul în metadate → folosește zsteg!
