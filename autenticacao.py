# Lista de usuários
usuario = []

def autentificacao(name3, password3):
    for autenti in usuario:
        if autenti['name'] == name3 and autenti['password'] == password3:
            return True
    return False
