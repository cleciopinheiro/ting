import sys


def txt_importer(path_file):
    if ".txt" not in path_file:
        sys.stderr.write("Formato inválido")
    try:
        with open(path_file, "r") as file:
            return file.read().split("\n")

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
