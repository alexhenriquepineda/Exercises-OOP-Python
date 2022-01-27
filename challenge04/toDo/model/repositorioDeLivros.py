from .entity import Livro

class RepositorioDeLivros:

    def __init__(self) -> None:
        self.__livros = []

    def registrar_livros(self, titulo, autor, ano):
        novoLivro = Livro(titulo, autor, ano)
        self.__livros.append(novoLivro)
        print(f"Livro {titulo} cadastrado")
        print()

    def listar_livros(self):
        for livro in self.__livros:
            print(
                f'''
                id: {livro.id}
                Livro: {livro.titulo}
                Autor: {livro.autor}
                Ano: {livro.ano}
                '''
            )
            print()