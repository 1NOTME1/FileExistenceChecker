#SPRAWDZANIE CZY PLIK ISTNIEJE W DANEJ LOKALIZACJI Z PLIKU .TXT
import os

def check_files_from_file(file_path):
    with open(file_path, "r") as f:
        for line in f:
            path = line.strip()
            if os.path.isfile(path):
                print(f"Plik {path} istnieje w danej lokalizacji!")
            else:
                print(f"Plik {path} nie istnieje w danej lokalizacji!")

file_path = r"C:\Users\USER_NAME\Desktop\file_existence_checker\pdf_names.txt"

check_files_from_file(file_path)
