# class Veiculo:
#     def __init__(self, nome, cor, tamanho):
#         self.nome = nome.title()
#         self.cor = cor
#         self.tamanho = tamanho
#
#     @property
#     def nome(self):
#         return self.nome
#
#     @nome.setter
#     def nome(self, novo_nome):
#         self.nome = novo_nome.title()
#
#
# class Carro(Veiculo):
#     def __init__(self, nome, cor, tamanho, rodas):
#         super().__init__(nome, cor, tamanho)
#         self.rodas = rodas
#
# class Barco(Veiculo):
#     def __init__(self, nome, cor, tamanho, helices):
#         super().__init__(nome, cor, tamanho)
#         self.helices = helices
#
# ######################################################################
#
# barco1 = Barco('nogueira', 'Branco', 'Grande', 2)
#
# print(barco1.tamanho)


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        # self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    # @property
    # def likes(self):
    #     return self._likes
    #
    # def dar_like(self):
    #     self._likes += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


##########################################################################################

vingadores = Filme('vingadores - guerra infinita', 2018, 160)

print(vingadores.nome)