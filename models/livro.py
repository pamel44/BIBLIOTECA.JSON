# Classe Livro Esta Classe Representa um Livro Dentro do Sistema


class Livro:
    # Construtor
    def __init__(self, titulo, autor, ano):
        # Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano


# Propriedade (GETTER)
# Permite acessar o título mesmo sendo privado


    @property
    def titulo(self):
        return self.__titulo


# SETTER
# Permite alterar título com validação


    @titulo.setter
    def titulo(self, novo_titulo):
        if len(novo_titulo) < 2:
            print("Título inválido!")
        else:
            self.__titulo = novo_titulo


# Método para mostrar dados


    def exibir(self):
        self.__log()
        print("Título: ", self.__titulo)
        print("Autor: ", self.__autor)
        print("Ano: ", self.__ano)


# Método privado


    def __log(self):
        print("(LOG) Livro Acessado")


# Converter para dicionario necessário para salvar em JSON


    def para_dict(self):
        return {
            "Titulo": self.__titulo,
            "Autor": self.__autor,
            "Ano": self.__ano
        }

# Método estático
    @staticmethod
    def categoria_padrao():
        return "Literatura"
