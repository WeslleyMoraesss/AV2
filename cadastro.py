from autenticacao import autentificacao, usuario

# Lista de livros cadastrados
cadas_liv = []

def cadastrar_usuario():
    while True:
        opc = input('Digite 1 para fazer o cadastro ou 2 para sair: ')
        if len(opc) > 1:
            print('Digite apenas 1 número')
            continue
        if opc == '1':
            name = input('Nome: ')
            password = input('Senha: ')
            dic2 = {'name': name, 'password': password}
            usuario.append(dic2)
            print(f'O usuário "{name}" foi cadastrado com sucesso.')
        elif opc == '2':
            break

def cadastr_livr():
    while True:
        print('--- Cadastro de Livros ---')
        num1 = input('Digite 1 para registrar livros ou 2 para sair: ')
        if len(num1) > 1:
            print('Digite apenas 1 número.')
            continue

        if num1 == '1':
            name2 = input('Nome: ')
            password2 = input('Senha: ')
            if autentificacao(name2, password2):
                print("Login feito com sucesso!")
                name_book = input('Digite o nome do livro: ')
                author_name = input('Digite o nome do autor: ')
                dic = {'name_book': name_book, 'author_name': author_name}
                cadas_liv.append(dic)
                print(f'Livro "{name_book}" registrado com sucesso.')
            else:
                print('Nome ou senha inválidos. Tente novamente.')
        elif num1 == '2':
            break