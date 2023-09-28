def content_with_word(word, instance, callback):

    response = []

    for item, process in enumerate(instance.queue):
        ocorrencias = []

        for line, l in enumerate(process['linhas_do_arquivo']):

            if word.lower() in l.lower():
                ocorrencias.append(callback(line, l))

        if len(ocorrencias) > 0:
            response.append({
                "palavra": word,
                "arquivo": instance.queue[item]['nome_do_arquivo'],
                "ocorrencias": ocorrencias
            })

    return response


def exists_word(word, instance):
    def callback(line, _):
        return {"linha": line + 1}

    return content_with_word(word=word, instance=instance, callback=callback)


def search_by_word(word, instance):
    def callback(line, content):
        return {"linha": line + 1, "conteudo": content}

    return content_with_word(word=word, instance=instance, callback=callback)
