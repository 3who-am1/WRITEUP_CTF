Enuntul problemei ne spune sa putem citi aceasta fila: unr.docx

Rezolvare: 

1. introducem comanda aceasta sa putem vedea ce tip de fisier e:
           
                   file unr.docx
   
  Si ne afiseaza asta:
         
                    unr.docx: 7-zip archive data, version 0.4

2. folosim comanda "exiftool" si observam ca ne da o avertizare precum: 
           
                   [minor] Folosește opțiunea Duplicate pentru a extrage etichetele 
                   pentru toate cele 23 de fișiere

3. folosim "strings", nu ne afiseaza nimic nou

4. Ar trebui totusi sa accesam acel fisier

Explicatie:

1. sa putem descopunem aceea fila, introducem aceasta comanda:
                  
                            7z x unr.docx
  
 Vedem ca ne decoprimeaza si afiseaza tot feluri de foldere si fisere cum ar fi:
                
                   '[Content_Types].xml'     docProps   _rels   unr.docx   word

2. sa putem gasi raspunsul la acest challenge in toate aceste fisiere si foldere, e sa analizam 
   si sa cautam fiecare folder si fisier si sa citim ce ne trasmite din fiecare parte

3. Am constatat ca la folderul "word/embeddings"
 
   Vedem ceva cu "Microsoft_PowerPoint_Presentation.pptx" 
   Stiind ca e in powerpoint, trebuie sa vedem ce contine

4. si din acel powerpoint ne afiseaza acest mesaj:
         
                            <35vsdeGHR> ---> flag gasit
         
   Congratulations!You solved the challenge


flag: <35vsdeGHR>


Succes, mic hacker !!! :))


