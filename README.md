# Base64-tools
Python tools to generate, hash and inspect base64-encoded files and archives.



---

Base64 Generator (`base64_generator.py`)
Permette di convertire qualsiasi file (ZIP, RAR, 7z, PDF, ecc.) in Base64.

Uso: `python base64_generator.py "<percorso_file>"`
Esempio: `python base64_generator.py "file_esempio.zip" > file_base64.txt`

L’output viene salvato in `file_base64.txt`. Il Base64 generato può essere usato con altri strumenti senza modificare il contenuto dell’archivio.

---

Archive Lurker (`archive_lurker_base64.py`)
Permette di visualizzare i nomi dei file contenuti in un archivio (ZIP, 7z, RAR) senza estrarre nulla.

Requisiti opzionali: `py7zr` per 7z (`pip install py7zr`), `rarfile` per RAR (`pip install rarfile`). ZIP è supportato nativamente da Python.

Uso: `python archive_lurker_base64.py <file_base64.txt>`

Il programma legge il Base64 dal file e prova ad aprire ZIP, 7z e RAR in memoria. Stampa i nomi dei file senza scrivere nulla su disco. Se il formato non è supportato o il Base64 è corrotto, mostra: “Formato non supportato o file corrotto.”

---

Base64 to Hash (`base64_to_hash.py`)
Permette di calcolare l’hash SHA-256 di un file a partire dal Base64 senza estrarlo.

Uso: `python base64_to_hash.py <file_base64.txt>`
Esempio: `python base64_to_hash.py file_base64.txt`

Il programma restituisce la stringa dell’hash SHA-256 del file originale.

---

Note: tutti i tool operano in memoria, leggendo Base64 e mostrando solo informazioni. 
Il Base64 può essere molto lungo, quindi salvarlo in un file .txt Assicurarsi che il Base64 sia completo---

> Note: This code was created using ChatGPT and then personally tested and modified for this project.






ENG


---

Base64 Generator (`base64_generator.py`)
Allows you to convert any file (ZIP, RAR, 7z, PDF, etc.) to Base64.

Usage: `python base64_generator.py "<file_path>"`
Example: `python base64_generator.py "example_file.zip" > file_base64.txt`

The output is saved in `file_base64.txt`. The generated Base64 can be used with other tools without modifying the content of the archive.

---

Archive Lurker (`archive_lurker_base64.py`)
Allows you to view the names of files inside an archive (ZIP, 7z, RAR) without extracting anything.

Optional requirements: `py7zr` for 7z (`pip install py7zr`), `rarfile` for RAR (`pip install rarfile`). ZIP is natively supported by Python.

Usage: `python archive_lurker_base64.py <file_base64.txt>`

The program reads the Base64 from the file and tries to open ZIP, 7z, and RAR archives in memory. It prints the file names without writing anything to disk. If the format is not supported or the Base64 is corrupted, it displays: “Unsupported format or corrupted file.”

---

Base64 to Hash (`base64_to_hash.py`)
Allows you to calculate the SHA-256 hash of a file from Base64 without extracting it.

Usage: `python base64_to_hash.py <file_base64.txt>`
Example: `python base64_to_hash.py file_base64.txt`

The program outputs the SHA-256 hash string of the original file.

---

Note: All tools operate in memory, reading Base64 and displaying only information.
Base64 can be very long, save it in a .txt file. Make sure the Base64 is complete.

---




> Note: This code was created using ChatGPT and then personally tested and modified for this project.
