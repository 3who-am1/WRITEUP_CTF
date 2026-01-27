# Riddle Registry - PicoCTF | Forensics | Easy | Writeup

**DESCRIEREA EXERCITIULUI:**

Bună, anchetator îndrăzneț! 📄🔍 Ai dat peste un PDF ciudat plin cu ceea ce nu pare altceva decât o prostie confuză. Dar atenție! 
Nu totul este așa cum apare. În mijlocul haosului se află un steag evaziv de comori ascuns care așteaptă să fie descoperit.
Găsiți fișierul PDF aici Document confidențial ascuns și descoperiți steagul în metadate.

**SUGESTII:**

1. Nu te lăsa păcălit de textul vizibil; este doar o momeală!

2. Caută dincolo de suprafață indicii ascunse

## INTELEGEREA CERINTEI:

Dupa cum observam avem un PDF prin care ar trebui sa facem niste analize prin el.
Tot ce ar trebui sa stim e sa gasim un steag ascuns, mai precis un flag format picoCTF{...[redacted]....}

**Rezolvare:**

1. folosim comanda: 
                            
                           strings confidential.pdf
  
   Si ne afiseaza:
 
                              ''''
                              ''''
                              ''''
                              0000103726 00000 n 
                              0000104001 00000 n 
                              0000134886 00000 n 
                              0000159291 00000 n 
                              0000178770 00000 n 
                              0000178908 00000 n  
                              trailer
                              /Size 49
                              /Root 3 0 R
                              /Info 2 0 R
                              startxref
                              181645
                              %%EOF
                              ''''''
                              '''''

Nimic folositor din ceea ce vedem aici.


2. folosim comanda:
                        
                              exiftool confidential.pdf
   
Si ne afiseaza:
 
                            ExifTool Version Number         : 13.25
                            File Name                       : confidential.pdf
                            Directory                       : .
                            File Size                       : 183 kB
                            File Modification Date/Time     : 2025:11:26 12:26:33+02:00
                            Linearized                      : No
                            Page Count                      : 1
                            Producer                        : PyPDF2
                            Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOGY5MWQ2OH0=
                                        

Din ceea ce ne-a afisat aici vedem ceva la Author ca un cod ciudatel, ne gandim sa il decriptam

3. folosim comanda:
               
                echo -n "cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOGY5MWQ2OH0=" | base64 -d

   Si ne afiseaza:

picoCTF{puzzl3d_m3tadata_f0und!_c8f91d68}


##**Flag:** picoCTF{puzzl3d_m3tadata_f0und!_c8f91d69}

---
**Succes !!! :))**
---
