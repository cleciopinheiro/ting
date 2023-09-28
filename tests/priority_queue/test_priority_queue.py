from ting_file_management.priority_queue import PriorityQueue
import pytest


process_queue = [
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["um parágrafo qualquer"]
    },
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": ["um parágrafo qualquer"]
    }
]


def test_basic_priority_queueing():
    instance = PriorityQueue()

    assert instance.is_priority(process_queue[0]) is True
    assert instance.is_priority(process_queue[1]) is False

    instance.enqueue(process_queue[0])
    instance.enqueue(process_queue[1])

    assert len(instance.high_priority) == 1
    assert len(instance.regular_priority) == 1

    assert instance.search(0) == process_queue[0]

    instance.dequeue()

    assert len(instance.high_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        instance.search(10)
