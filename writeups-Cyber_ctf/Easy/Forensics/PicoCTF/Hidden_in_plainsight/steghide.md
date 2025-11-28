🔍 Ce este steghide?

steghide este un tool folosit în steganografie — ascunde sau extrage fișiere din alte fișiere (de obicei imagini sau audio).

🧩 Funcțiile principale

Există două operații mari:

1. embed — ascunde un fișier într-o imagine
2. extract — extrage un fișier ascuns dintr-o imagine
🛠 Explicația parametri-lor principali
-cf (cover file)

Fișierul „acoperire” în care ascunzi ceva.
Ex: imaginea principală img.jpg.

-ef (embed file)

Fișierul pe care vrei să-l ascunzi.
Ex: secret.txt.

-sf (stego file)

Fișierul care conține deja ceva ascuns și din care vrei să extragi.
Ex: img.jpg cu payload.

-p (password)

Parola folosită pentru criptarea datelor ascunse.

-xf (extract file)

Numele fișierului rezultat după extracție.
