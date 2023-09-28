from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    file_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas":  len(file),
        "linhas_do_arquivo": file
    }

    if len(instance.queue) == 0:
        instance.enqueue(file_process)
    else:
        for process in instance.queue:
            if path_file != process['nome_do_arquivo']:
                instance.enqueue(file_process)

    print(file_process, file=sys.stdout)


def remove(instance):
    if len(instance.queue) == 0:
        print('Não há elementos', file=sys.stdout)
    else:
        process = instance.dequeue()
        message = f"Arquivo {process['nome_do_arquivo']} removido com sucesso"
        print(message, file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
