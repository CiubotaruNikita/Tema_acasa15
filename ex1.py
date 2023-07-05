import os

def list_files_in_directory(path):
    if not os.path.isdir(path):
        print("Calea introdusă nu este o mapă.")
        return

    if not os.path.exists(path):
        print("Calea introdusă nu există.")
        return

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file in files:
        print(file)

path = input("Introduceți calea către directorul dorit: ")

list_files_in_directory(path)