import base64
import hashlib
import sys
#Genera un hash da un Base64
#come usare
#python allegati_hash.py base64_del_file.txt

if len(sys.argv) != 2:
    print("Uso: python allegati_hash.py <file_base64.txt>")
    sys.exit(1)

# File che contiene il Base64
input_file = sys.argv[1]

# Leggi il Base64 dal file
with open(input_file, "r", encoding="utf-8") as f:
    base64_data = f.read().strip()

# Decodifica
file_bytes = base64.b64decode(base64_data)

# Calcola SHA-256
sha256_hash = hashlib.sha256(file_bytes).hexdigest()

# Output pulito
print(sha256_hash)
