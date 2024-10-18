from cadastro import cadastrar_usuario, cadastr_livr
from remocao import remo_books
from listagem import return_list

def menu():
    print('Bem-vindo ao menu da biblioteca')
    while True:
        opc2 = input(
            'Pressione 1 para cadastrar usuário, 2 para registrar livros, '
            '3 para remover livros, 4 para listar livros e 5 para sair: ')
        if len(opc2) > 1:
            print('Digite apenas 1 único número')
            continue
        if opc2 == '1':
            cadastrar_usuario()
        elif opc2 == '2':
            cadastr_livr()
        elif opc2 == '3':
            remo_books()
        elif opc2 == '4':
            return_list()
        elif opc2 == '5':
            print('Saindo do sistema...')
            break

if __name__ == "__main__":
    menu()
