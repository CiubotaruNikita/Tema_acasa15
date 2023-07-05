import os

def list_files_in_directory(path):
    if not os.path.isdir(path):
        print("Calea introdusă nu este o mapă.")
        return

    if not os.path.exists(path):
        print("Calea introdusă nu există.")
        return

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def rename_files_in_directory(path, prefix=""):
    files = list_files_in_directory(path)
    files.sort(key=lambda f: os.path.getctime(os.path.join(path, f)))

    index = 1
    for file in files:
        filename, extension = os.path.splitext(file)
        new_filename = f"{prefix}{index}{extension}"
        new_filepath = os.path.join(path, new_filename)
        old_filepath = os.path.join(path, file)
        os.rename(old_filepath, new_filepath)
        index += 1

path = input("Introduceți calea către directorul dorit: ")

prefix = input("Introduceți prefixul dorit (lăsați gol pentru a nu adăuga un prefix): ")

rename_files_in_directory(path, prefix)