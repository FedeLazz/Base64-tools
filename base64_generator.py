import base64
import sys
import os

#-----Genera un base64 del file
#-----Come usare
#python base64_generator.py file_esempio.zip



def main():
    if len(sys.argv) != 2:
        print(f"Uso: python {os.path.basename(__file__)} <percorso_file_zip>")
        sys.exit(1)

    zip_path = sys.argv[1]

    if not os.path.isfile(zip_path):
        print(f"Errore: il file '{zip_path}' non esiste.")
        sys.exit(1)

    try:
        with open(zip_path, "rb") as f:
            zip_bytes = f.read()
        zip_base64 = base64.b64encode(zip_bytes).decode("utf-8")
        print(zip_base64)
    except Exception as e:
        print(f"Errore durante la lettura o conversione: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
