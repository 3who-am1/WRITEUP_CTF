def alternative_decrypt():
    # Lista de numere ca string
    key_str = "102,11,179,235,102,12,112,102,4,233,238,102,23,149,102,18,237,121,102,10,105,31,16,54,131"
    key = key_str.encode('utf-8')
    
    with open('my_secret_book_draft.secure.old', 'rb') as f:
        encrypted = f.read()
    
    decrypted = bytearray()
    for i, byte in enumerate(encrypted):
        decrypted.append(byte ^ key[i % len(key)])
    
    try:
        text = decrypted.decode('utf-8')
        print("Decrypted with string key:")
        print(text[:500])
        if "ctf{" in text:
            with open('flag.txt', 'w') as f:
                f.write(text)
    except Exception as e:
        print(f"Error: {e}")

alternative_decrypt()
