import base64
import sys
import io

#-----Mostra contenuto archivio senza estrarlo, dal Base64
#---Come usarlo
# python archive_lurker_base64.py base64_del_file.txt

# ZIP
import zipfile

# 7z
try:
    import py7zr
except ImportError:
    py7zr = None

# RAR
try:
    import rarfile
except ImportError:
    rarfile = None

if len(sys.argv) != 2:
    print(f"Uso: python {sys.argv[0]} <file_base64.txt>")
    sys.exit(1)

file_b64 = sys.argv[1]

# Leggi Base64
try:
    with open(file_b64, "r", encoding="utf-8") as f:
        b64_data = f.read().strip()
except Exception as e:
    print(f"Errore nella lettura del file Base64: {e}")
    sys.exit(1)

# Decodifica in memoria
try:
    archive_bytes = base64.b64decode(b64_data)
except Exception as e:
    print(f"Errore nella decodifica Base64: {e}")
    sys.exit(1)

archive_stream = io.BytesIO(archive_bytes)

def list_zip():
    try:
        with zipfile.ZipFile(archive_stream) as zf:
            print("Formato ZIP:")
            for name in zf.namelist():
                print(name)
        return True
    except Exception:
        return False

def list_7z():
    if not py7zr:
        print("py7zr non installato, non posso leggere archivi 7z.")
        return False
    try:
        archive_stream.seek(0)
        with py7zr.SevenZipFile(archive_stream, mode='r') as z:
            print("Formato 7z:")
            for name in z.getnames():
                print(name)
        return True
    except Exception:
        return False

def list_rar():
    if not rarfile:
        print("rarfile non installato, non posso leggere archivi RAR.")
        return False
    try:
        archive_stream.seek(0)
        with rarfile.RarFile(archive_stream) as rf:
            print("Formato RAR:")
            for name in rf.namelist():
                print(name)
        return True
    except Exception:
        return False

# Prova i formati
if list_zip():
    sys.exit(0)

archive_stream.seek(0)
if list_7z():
    sys.exit(0)

archive_stream.seek(0)
if list_rar():
    sys.exit(0)

print("Formato non supportato o file corrotto.")
