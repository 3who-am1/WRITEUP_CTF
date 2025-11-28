Dupa cum observam avem un PDF prin care ar trebui sa facem niste analize prin el.
Tot ce ar trebui sa stim e sa gasim un steag ascuns, mai precis un flag format picoCTF{...[redacted]....}

Avem doua indici:
1. Nu te lăsa păcălit de textul vizibil; este doar o momeală!

2. Caută dincolo de suprafață indicii ascunse


Rezolvare:

1. folosim comanda: 
     strings confidential.pdf
 
   Si ne afiseaza:
 
''''
''''
''''
0000103726 00000 n 
0000104001 00000 n 
0000134886 00000 n 
0000135119 00000 n 
0000135530 00000 n 
0000135719 00000 n 
0000135979 00000 n 
0000158621 00000 n 
0000158855 00000 n 
0000159036 00000 n 
0000159291 00000 n 
0000178770 00000 n 
0000178794 00000 n 
0000178851 00000 n 
0000178908 00000 n 
trailer
/Size 49
/Root 3 0 R
/Info 2 0 R
startxref
181645
%%EOF


Nimic folositor din ceea ce vedem aici.


2. folosim comanda:
    exiftool confidential.pdf
   Si ne afiseaza:
 
ExifTool Version Number         : 13.25
File Name                       : confidential.pdf
Directory                       : .
File Size                       : 183 kB
File Modification Date/Time     : 2025:11:26 12:26:33+02:00
File Access Date/Time           : 2025:11:26 12:30:06+02:00
File Inode Change Date/Time     : 2025:11:26 12:26:51+02:00
File Permissions                : -rw-rw-r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Page Count                      : 1
Producer                        : PyPDF2
Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOGY5MWQ2OH0=
                                        

Din ceea ce ne-a afisat aici vedem ceva la Author ca un cod ciudatel, ne gandim sa il decriptam

3. folosim comanda:
     echo -n "cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOGY5MWQ2OH0=" | base64 -d
   Si ne afiseaza:

picoCTF{puzzl3d_m3tadata_f0und!_c8f91d68}


Flag: picoCTF{puzzl3d_m3tadata_f0und!_c8f91d69}


Succes !!! :))
