In aceaasta problema trebuie sa aflam o parola din acest fisier binar executabil

Rezolvare:

1. introducem comanda: 

                                            ls -la 

si ne afiseaza asta:
          
                                         total 28
                                         drwxr-xr-x 2 whoami whoami 4096 Nov 20 12:48 .
                                         drwxr-xr-x 3 whoami whoami 4096 Nov 20 12:44 ..
                                         -rw-r--r-- 1 whoami whoami 8488 Nov 20 12:47 cat.elf

Observam ca avem aceste permisiuni:
 
                                           cat.elf -rw-r--r--

##explicatie scurta:  

                                           r ---> citire
                                           w ---> scriere
                                           x ---> executare
                                           d ---> folder
                    
                    
sa putem face sa fie executabil introducem aceasta comanda:  

                                          chmod +x cat.elf
                   
*chmod +x = „fă fișierul ăsta executabil” (adică să-l poți rula direct cu ./nume_fisier)*

2. dupa ce am introdus comanda, introducem iar comanda ls -la si vedem ca sa remodificat sa poata rula
                            
                                                  ls -la 

                                      -rwxr-xr-x 1 whoami whoami 8488 Nov 20 12:47 cat.elf

Vedem ca sa remodificat si avem acolo un *x*, adica executabil 

3. sa putem rula e sa introducem asta: 
                
                                                   ./cat.elf
   Si ne afiseaza: 
 
                                            https://www.youtube.com/watch?v=oHg5SJYRHA0
                                            The password is: 1234567890
                                            Try Harder!

Vedem ca trebuie sa introducem o parola, dar nu o stim, suntem nevoiti sa facem o analiza la fisier

4. folosim comanda: 

                                            strings cat.elf | head

  si ne afiseaza: 

                                        /lib64/ld-linux-x86-64.so.2
                                       libc.so.6
                                        __isoc99_scanf
                                       puts
                                       __stack_chk_fail
                                      printf
                                      __cxa_finalize
                                       strcmp
                                      __libc_start_main
                                      GLIBC_2.7


Nu prea ne ajuta, asa ca folosim iar *strings* dar fara head.

=9 parola12 Well donH e, your H special H flag is:H ctf{a81H 8778ec7aH 9fc19887H 24ae3700H b
42e998eH b09450eaH b7f1236eH 53bfdcd9H 23878} d
H34%( AWAVI AUATL []A\A]A^A_ 
https://www.youtube.com/watch?v=oHg5SJYRHA0 The password is:
%1023[^
Try Harder!
;*3$"
GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 crtstuff.c


dupa cum putem vedea e ca de aici avem si parola dar si flag-ul cel dorit.


5. introducem parola gasita: *parola12*

                                       ./cat.elf


                               https://www.youtube.com/watch?v=oHg5SJYRHA0
                               The password is: parola12
                               Well done, your special flag is: ctf{a18778ec7a9fc1988724ae3700b42e998eb09450eab7f1236e53bfdcd923878}

---
FLAG GASIT: ctf{a18778ec7a9fc1988724ae3700b42e998eb09450eab7f1236e53bfdcd923878}
___

Succes !!! :))



