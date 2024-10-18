from cadastro import cadas_liv

def remo_books():
    while True:
        opc = input('Digite 1 para remover um livro ou 2 para sair: ')
        if len(opc) > 1:
            print('Digite apenas 1 número.')
            continue

        if opc == '1':
            book = input('Digite o nome do livro para ser removido: ')
            for cadast in cadas_liv:
                if cadast["name_book"] == book:
                    cadas_liv.remove(cadast)
                    print(f'Livro "{book}" foi removido.')
                    break
            else:
                print('Livro não encontrado.')
        elif opc == '2':
            break