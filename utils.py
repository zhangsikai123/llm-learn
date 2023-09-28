import tiktoken


def count_tokens(text):
    return len(tiktoken.get_encoding("cl100k_base").encode(text))
