Enuntul ne spune ca trebuie sa intelegem acest fisier rau intetionat. 
Ne avertizeaza ca aceasta provocare contine Malware Real, si ar trebui sa testam intr-un
mediu **SANDBOX** la intreaga provocare, si putem rezolva doar folosind **VirusTotal**

**REZOLVARE**

 Q1. Care este SHA256 al dosarului dat?
     (Puncte: 100)

 Q2. Care este numele de familie malware? 
     (Puncte: 100)

 Q3. Ce tip de malware este folosit pentru analiză? 
     (Puncte: 100)

 Q4. Furnizați data creării fișierului rău intenționat, așa cum este prezentat în VirusTotal 
     (Puncte: 100)
   Format steag: VirusValoare totală

 Q5. Care este IP-ul rău intenționat care a fost marcat ca rău intenționat utilizat de 
   eșantionul de malware dat? 
     (Puncte: 100)

---

1. La prima intrebare ne spune, care este SHA256 al dosarului dat?
   Sa stim care este SHA256 putem folosi comanda aceasta:
 

                 sha256sum "malware-sample"

Ne afiseaza:
 
        4c1dc737915d76b7ce579abddaba74ead6fdb5b519a1ea45308b8c49b950655c  malware-sample
---

**!!! ATENTIE !!!**

 Comanda 1: (echo -n "malware-sample" | sha256sum) calculeaza hash pentru text
 Comanda 2: (sha256sum "malware-sample") calculeaza hash pentru fisier
 
 EXEMPLU:
 Comanda 1:

              echo -n "malware-sample" | sha256sum

1a5c2f8782e1fb86c5ffc3c090fdc2fa45c23040f72716003f790d1132c2f48d  -

  Comanda 2:

              sha256sum "malware-sample"

4c1dc737915d76b7ce579abddaba74ead6fdb5b519a1ea45308b8c49b950655c  malware-sample

---

2. La a doua intrebare ne spune care este numele familiei malware?
   Sa cunoastem familia malware e sa analizam fisierul de pe site-ul metionat, **VirusTotal.com**.
   Accesam site-ul, acolo la file, apasam pe optiunea "Choose file" si inseram **Malwere-sample**.
   Dupa ce am inserat, observam ca ne apare acolo pe "Popular threat label" si in dreapta vedem "Family labels".
   Si acolo ne spune ca sunt **petya**, **petr** si **diskcoder**, asa ca il lu-am pe prima varianta si acela ar fi raspuns-ul: petya

          Petya ---> raspuns la intrebarea Q2

3. La a treia intrebare ne spune ce tip de malware este folosit pentru analiza?
   Ca analiza de malware a fost folosita, e sa observam tot de pe **VirusTotal** si acolo ne spune 
   tot in tabelul acela in care ne informeaza la  "Popular threat label", observam ca este "trojan.petya", si nu numa acolo, 
   vedem si mai jos ca trojan e cel mai folosit, cum ar fi: (Trojan.Win32, Trojan.ransom.UAC, TRJ/WLT.b, etc..),
   si acela ar fi raspuns-ul: Trojan
  
        Trojan ---> raspuns la intrebarea Q3

4. La a patra intrebare ne spune sa furnizam data creari a unui fisier rau intentionat, asa cum este prezentat in **VirusTotal**.
   Sa putem da seama care este prezentat in **VirusTotal** si sa gasim data creari e sa accesam la "Details" si mai jos la "History",
   vedem ca la "Creation Time" ne afiseaza data creari, (Creation Time: 2016-01-30 02:56:43 UTC)  
   
        2016-01-30 02:56:43 UTC ---> raspuns la intrebarea Q4

5. La ultima intrebare ne spune ca, care ar fi ip-ul rau intentionat care a fost marcat ca rau intentionat utilizat de esantiorul de malware
   Sa putem afla ip-ul acela, ar trebui sa analizam tot pe **VirusTotal** la **Relations**
   si mai jos la **Contacted IP addresses** vedem ca is vreo 45 de ip-uri, dar cel mai relevant raspuns ar fi prima optiune intotdeauna de luat
   iar acela ar fi: 13.107.4.53

        13.107.4.53 ---> raspuns la intrebarea Q5
---
### SUCCES !!!! :))))
---

**RASPUNS**

Q1. SHA256 al dosarului dat este:
           4c1dc737915d76b7ce579abddaba74ead6fdb5b519a1ea45308b8c49b950655c

Q2. Numele familiei malware este:
           Petya

Q3. Tip de malware folosit este:
          Trojan

Q4. Data creari a fisierului rau intetionat este:
         2016-01-30 02:56:43 UTC

Q5. Ip-ul rau intentionat este:
         13.107.4.53




  
