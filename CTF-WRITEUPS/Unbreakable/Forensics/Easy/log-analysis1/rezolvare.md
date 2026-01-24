Ne spune ca un atacator a incercat sa arunce parolele
utilizatorului pe sistemul vizat, preferat niste comenzi ale terminalului. 

Noi trebuie doar sa gasim raspunsurile la urmatoarele intrebari:

 Q1. Care este comanda completă folosită pentru a arunca procesul lsass 
     pe sistemul vizat? (Puncte: 100)
     
 Q2. Care este adresa IP a computerului compromis? (Puncte: 100)

 Q3. Care este comanda folosită de atacator pentru a enumera toți utilizatorii
     sistemului? (Puncte: 100)

 Q4. Ce tehnică MITRE poate fi atribuită unui caz în care parolele sistemului 
     de operare sunt aruncate? Format steag <technique_ID>:<technique_name> 
     (Puncte: 100)

 Q5. Ce cod de eveniment Windows Security a fost declanșat atunci când 
     atacatorul a încercat să enumere grupurile locale existente pe sistemul 
     compromis? (Puncte: 100)

---

**Rezolvare:**

1. vedem ca trebuie sa extragem datele intr-un format de tip .zip,
   folosind comanda: 
                          
                         unzip log-analysis1.zip

   Si ne extrage urmatoarele fisiere:
   
  ...
  inflating: PhysicalDrive0_1/Ntfs/$LogFile  
  inflating: PhysicalDrive0_1/Ntfs/$MFT  
  inflating: PhysicalDrive0_1/Ntfs/$MFTMirr  
  inflating: SystemInfo/output.txt   
  inflating: processes.txt           
  inflating: services.txt            
  inflating: hoarderlog.json 
  ...


2. Observam ca ne-a extras directoarele, fisiere, dar si de tip .json, .evtx, .etl, etc...,
   
         hoarderlog.json  log-analysis1.zip  PhysicalDrive0_0  PhysicalDrive0_1  processes.txt  services.txt  SystemInfo


3. Daca observam bine, avem ceva la SystemInfo, poate acolo ne ofera ceva informatii sa putem raspunde la intrebarile de mai sus
   la directorul acela vedem ca la comanda: 
                           
                           
                             cat SystemInfo/output.txt
   
###**Ne afiseaza:**

...

                           Network Card(s):           1 NIC(s) Installed.\
                           [01]: Intel(R) 82574L Gigabit Network Connection\
                                 Connection Name: Ethernet0\
                                 DHCP Enabled:    No\
                                 IP address(es)\
                                 [01]: 10.0.8.16\
                                 [02]: fe80::2044:1feb:98c2:a511\
                           Hyper-V Requirements:   A hypervisor has been detected. Features required for Hyper-V will not be displayed.
                                 

Si vedem ip-ul computeru-lui, care ar fi:
                  
                       10.0.8.16  ---> Raspunsul la intrebarea Q2  

Analizand din informatiile de acolo, vedem ca nu mai gasim vreo solutie la celelalte intrebari ramase, ramane de a mai analiza si la celelalte.

---

4. Sa putem gasi comanda completa care ar arunca procesul **lsass** pe sistemul vizat, e sa folosim comanda:

                       grep -r "lsass" .
   
   Si aceasta comanda cauta peste tot, si ne-ar afisa raspunsul:

   
''''
 
./PhysicalDrive0_0/PowerShellHistory/Users/bitsentinel/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt:C:\Users\BITSEN~1\AppData\Local
 \Temp\Procdump\procdump.exe -aacepteula -ma lsass.exe passwords.txt
./PhysicalDrive0_0/PowerShellHistory/Users/bitsentinel/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt:C:\Users\BITSEN~1\AppData\Local
 \Temp\Procdump\procdump.exe -aacepteula -ma lsass.exe passwords
./PhysicalDrive0_0/PowerShellHistory/Users/bitsentinel/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt:C:\Users\BITSEN~1\AppData\Local
 \Temp\Procdump\procdump.exe -aacepteula -ma lsass.exe 
./PhysicalDrive0_0/PowerShellHistory/Users/bitsentinel/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt:psexec.exe -s -d -i lsass.exe 
./PhysicalDrive0_0/PowerShellHistory/Users/bitsentinel/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt:C:\Users\BITSEN~1\AppData\Local
 \Temp\Procdump\procdump64.exe -s -d -i lsass.exe
./PhysicalDrive0_0/PowerShellHistory/Users/bitsentinel/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt:C:\Users\BITSEN~1\AppData\Local
\Temp\Procdump\procdump64.exe -ma lsass.exe lsass.txt
grep: ./PhysicalDrive0_0/Ntuser/Users/bitsentinel/NTUSER.DAT: fișierul binar conține textul căutat

''''


Vedem ca la final este executat comanda: 

                       procdump64.exe -ma lsass.exe lsass.txt ---> Raspuns la intrebarea Q1
---
##**!!!! BONUS !!!!**

Sa putem da seama care comanda e ceea corecta, e sa observam cum a folosit la celelalte, cum ar fii comanda:
                                             
                                       procdump.exe -aacepteula -ma lsass.exe passwords.txt

Vedem din start ca scrierea e gresita, dar e si lipsa de comanda necompletata

Al doilea, si al treilea tot e gresit

                                        procdump64.exe -s -d -i lsass.exe

Iar aceasta comanda este incorectă și nu va face ce îți dorești (adică să-ți instaleze un driver persistent pentru a dump-ui LSASS ori de câte ori vrei, fără să mai 
ai nevoie de procdump rulând).


comanda corecta din ceea ce vedem este aceasta: 
                   
                                procdump64.exe -ma lsass.exe lsass.txt

Deci bagare de seama comenzile si cerintele autorului pentru a putea raspunde la intrebari.

---

5. Sa putem gasi comanda atacatorului pentru a enumera toti utilizatori sistemului este sa analizam istoricul comenzilor folosite de el,
   asa cum am gasit comanda la intrebarea **Q1** in folder-ul: 

                      ./PhysicalDrive0_0/PowerShellHistory/Users/bitsentinel/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt

   aici gasim si comanda care enumera toti utilizatori, tinand cont ca acela ar fi ("net user", "whoami", "wmic", etc ...)
   
   Acum sa ne putem confirma sa fie ceea corecta e sa folosim comanda:
 
        
                strings ConsoleHost_history.txt | grep -iE "(net user|wmic|whoami)"


Afiseaza: **net users**

                                              net users ---> raspuns la intrebarea Q3


6. Tehnica MITRE poate fi atribuita in cazul parolelor de operare care sunt 
   aruncate ar fi analizand pe internet care atac poate fi.
   Accesam: MITRE ATT&CK Enterprise Matrix
   Trebuie sa gasim OS Credential Dumping, acela ar fi T1003
   
   Deja am gasit raspunsul, acela ar fi: 
 
                    T1003:OS Credential Dumping  ---> Raspuns la intrebarea Q4

  T1003:OS  ---> <technique_ID>
  Credential Dumping ----> <technique_name>


---
##**!!!! EXPLICATIE !!!!**

Ce este **Mitre att&ck?**

**MITRE ATT&CK** este o bază de cunoștințe globală, accesibilă gratuit, creată de organizația non-profit MITRE. Ea documentează tacticile, tehnicile și procedurile 
(TTP-uri) ale adversarilor cibernetici, bazate pe observații reale din atacuri. Scopul principal este să ajute echipele de securitate (din sectorul privat, 
guvernamental sau comunitatea cybersecurity) să dezvolte modele de amenințări, metodologii de apărare și soluții colaborative pentru o securitate mai eficientă.
Componente principale:

**Matricea ATT&CK:** O structură organizată pe etape ale atacului (ex: Reconnaissance, Initial Access, Execution, Persistence, Defense Evasion, până la Impact), cu peste 
200 de tehnici detaliate.
Alte variante: Pentru Mobile, ICS (sisteme de control industrial) și Cloud.

Este un instrument esențial în threat intelligence, folosit pentru simulări de atacuri (red teaming) și detectare proactivă. Site-ul oferă resurse deschise, navigabile
și actualizate constant.

---


7.  cod-ul evenimentul al windows-ului security care a declansat de atacator care a incercat sa enumere grupurile locale existente compromise ar fi aceasta:
   
Fisierul care ar contine evenimentele ar fi: 
    
                               PhysicalDrive0_0/Events/Windows/System32/winevt/Logs/Security.evtx

                               strings PhysicalDrive0_0/Events/Windows/System32/winevt/Logs/Security.evtx 
  
Dupa comanda **strings**, ne afiseaza tot feluri de metadate si nimic folositor, am folosit si comanda "cat" dar nici acolo nimic.

Asa ca ar trebui sa apelam la niste tool-uri avansate, cum ar fi:
                 
                   CyberChef, gigasheet.com, LogViewPlus, Tad, DuckDB, etc...

Mai usor e sa accesam site-ul **gigasheet.com**, ne logam acolo, si observam ca ne spune sa inseram un fisier, facem ce ne spune si vedem ca chiar ne afiseaza toate datele.


Din ceea ce vedem, codul **4798** apare ce-l mai des

                                      4798 ---> Raspuns la intrebarea Q5
 


Link explicatie la acel cod il gasiti aici:  

                             https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4798

---
Raspuns: 

Q1: Comanda completa folosita pentru a arunca procesul lsass pe sistemul viza este:
 
                       procdump64.exe -ma lsass.exe lsass.txt


Q2: Care este adresa IP a computerului compromis?
 
                        10.0.8.16


Q3: Care este comanda folosită de atacator pentru a enumera toți utilizatorii sistemului?
     
                       net users


Q4. Ce tehnică MITRE poate fi atribuită unui caz în care parolele sistemului de operare sunt aruncate? 
    Format steag <technique_ID>:<technique_name>

                       T1003:OS Credential Dumping


 Q5. Ce cod de eveniment Windows Security a fost declanșat atunci când atacatorul a încercat să enumere 
     grupurile locale existente pe sistemul compromis?

                   4798
---


##**Succes !!!! :))**

---
