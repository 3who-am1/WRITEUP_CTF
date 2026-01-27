problema ne spune ca daca putem recupera secretul din interior al folder-ului format de .zip

 Q1. Ce este steagul? (Puncte: 100)
Sunt necesare unele criminalistice pe disc. Parola se pierde prin aceste discuri într-un format.jpg. Avem nevoie de el cât mai curând posibil.
Sculptura este, de asemenea, necesară.


Rezolvare:

1. prima data e sa descopunem fisierele din acel tip .zip, comanda folosita ar fi:
 
                                                  unzip forensics-disk.zip
   Ne afiseaza:

Archive:  forensics-disk.zip
  inflating: new_1.img               
  inflating: new_2.img               
  inflating: new_3.img               
                         

 Observam ca avem 3 imagini, cred ca 3 diferite, fata de ceilalti

2. Analizam imaginile extrase, dar observam ca nu arata nimic, e ca niste pagini goale, 
   dar enuntul si intrebarea ne spune ca sunt parole care se pierd prin aceste discuri pe format-ul jpg.

   Opaa... Ne spune "formate de jpg", dar noi avem extrase ".img" dar nu si ".jpg"
   
   Si daca nu era in enunt spus, puteam sa fi analizat de tip-ul fisierului si sa vedem ce informati are acela,
   comanda era:

                                  file new_1.img

   Si ne afiseaza:
   
  new_1.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, Exif Standard: [TIFF image data, little-endian, direntries=6, 
  orientation=upper-left, xresolution=164, yresolution=172, resolutionunit=2], baseline, precision 8, 1240x1748, components 3

  Si aici vedem ca e de tip-ul JPEG de imagine.
  
3. Sa putem vedea ce se afla in imaginile care le-am extras, e sa modficam extensiile, in loc de .img sa adaugam cu .jpg
   si comanda pe care ar veni este asa:
                             
                                   mv new_1.img new_1.jpg; mv new_2.img new_2.jpg; mv new_3.img new_3.jpg

   !!!! PE SCURT !!!!


               mv ---> este de a modifica fisierul,
                       sau de a muta in alt folder.

  !!!! PE SCURT !!!!

   Iar acum ca sa remodificat extensiile, ar trebui sa si functioneze imaginea sa o putem vizualiza:
 
                                    xdg-open new_1.jpg

    Si observam ca ne arata o parte din flag:
 
                                    CTF{232293t-    ---> o parte din flag

     Urmatoarea imagine ar fi:
                                    32dcvg33-bestdkfe}     ----> ultimul flag

     Si ultima imagine o vedem dar o parte e cam stearsa, dar ne putem da seama 
     ce scrie si acela ar fi flag-ul cum e la new_2.jpg


flag gasit: CTF{232293t-32dcvg33-bestdkfe}


Succes !!!! :)))

