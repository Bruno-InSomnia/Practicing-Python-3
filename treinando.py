class Favorites:
    def __init__(self, nome, year, duration):
        self._nome = nome
        self.year = year
        self.duration = duration

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    # def __str__(self):
    #     return f'Song Title: {self.nome}, {self.year} - Duration: {self.duration}min'


class Movie(Favorites):
    def __init__(self, nome, year, duration, director):
        super().__init__(nome, year, duration)
        self.director = director

    def __str__(self):
        return f'Song Title: {self.nome}, {self.year} by {self.director} - Duration: {self.duration}min'

class Song(Favorites):
    def __init__(self, nome, year, duration, singer):
        super().__init__(nome, year, duration)
        self.singer = singer

    def __str__(self):
        return f'Song Title: {self.nome}, {self.year} by {self.singer} - Duration: {self.duration}min'


#####################################################################################


jorge = Song('Jorge', 10, 2, 'John Travolta')
#
# todos_favoritos = [jorge]
#
# for musica_ou_filme in todos_favoritos:
#     print(musica_ou_filme)

print(jorge)
# songum = Song('do i wanna know', 2014, 5, 'artic monkeys')
#
# print(songum.nome)
