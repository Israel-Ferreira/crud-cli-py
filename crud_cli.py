from os.path import exists
import json

import uuid

def criar_arquivo():
    with open("./books.json", "x") as f:
        print("Criando arquivo json")

        book =  {
            "id": str(uuid.uuid4()),
            "title": "As Crônicas de Nárnia: O Leão, A Feiticeira e O Guarda Roupa",
            "publisher": "Martins Fontes",
            "author": "C.S LEWIS"
        }

        books = [book]

        json.dump(books, f, indent=4,  separators=(',',': '))



def deletar_livro(id: str):
    pass


def atualizar_livro(id: str):
    pass


def mostrar_livros():
    file_exists =  exists("./books.json")

    if not file_exists:
        criar_arquivo()

    book_list = []

    with open("./books.json", "r") as json_file:
        book_list = json.load(json_file)


    for book in book_list:
        print(f"Livro: {book['title']}, Autor: {book['author']}, Editora: {book['publisher']}\n")



def mostrar_livro_por_id(id: str):
    file_exists =  exists("./books.json")

    if not file_exists:
        raise FileNotFoundError("error: Arquivo não encontrado")
    
    with open("./books.json", "r") as json_file:
        book_list =  json.load(json_file)

    book_obj = None

    for book in book_list:
        if book["id"] ==  id:
            book_obj = book


    print(book_obj)





def adicionar_livro():
    titulo_livro =  input("Titulo do Livro: ")
    editora =  input("Editora: ")

    autor_livro = input("Autor: ")

    livro =  {
        "id": str(uuid.uuid4()),
        "title": titulo_livro,
        "publisher": editora,
        "author": autor_livro
    }


    file_exists =  exists("./books.json")

    if not file_exists:
        criar_arquivo()

    list_obj = []

    with open("./books.json") as json_file:
        list_obj =  json.load(json_file)

    with open("./books.json", "w") as f:   
        list_obj.append(livro)
        json.dump(list_obj,f, indent=4,  separators=(',',': '))

    print(f"Livro {titulo_livro} foi adicionado com sucesso!!!")
            


if __name__ == "__main__":
    print("CRUD de Livros  - CLI \n")

    print("Selecione uma opção")

    msg = """
    1 - Adicionar Livro
    2 - Mostrar Livros
    3 - Buscar Livro por Id
    4 - Atualizar livro pelo id
    5 - Excluir livro pelo id
    """

    print(msg)
    crud_option =  int(input("Opção selecionada: "))


    if crud_option == 1:
        adicionar_livro()
    elif crud_option == 2:
        mostrar_livros()
    elif crud_option == 3:
        try:
            id =  input("Informe o id do livro: ")
            mostrar_livro_por_id(id)
        except FileNotFoundError as fe:
            print(fe)
