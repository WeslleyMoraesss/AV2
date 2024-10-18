from cadastro import cadas_liv

def return_list():
    if not cadas_liv:
        print('Nada foi armazenado na lista de livros.')
    else:
        for livro in cadas_liv:
            print(f"Nome: {livro['name_book']}, Autor: {livro['author_name']}")