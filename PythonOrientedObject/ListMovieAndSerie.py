#show list the Movie, Serie, of TV-show
#it has name, year and likes
#Movie have duration
#Series have season
class Progroma():
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome= novo_nome.title()

    def __str__(self):
        return f'{programa.nome} - {programa.ano} - {programa.likes}'

class Filme(Progroma):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{programa.nome} - {programa.ano} - {programa.duracao} Min - {programa.likes}'

class Serie(Progroma):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):# magic method that textualize result how string
        return f'{programa.nome} - {programa.ano} - {programa.temporadas} Temporadas - {programa.likes}'

class Playlist: 
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):# Dunder Methods knowing like magic - iterate the function 
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores ultimate', 2018, 160)
sete_vidas = Filme('sete vidas', 2008, 100)
friends = Serie('friends', 1999, 10)
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
vingadores.dar_likes()
friends.dar_likes()
friends.dar_likes()
friends.dar_likes()
sete_vidas.dar_likes()
sete_vidas.dar_likes()
sete_vidas.dar_likes()
sete_vidas.dar_likes()
sete_vidas.dar_likes()


filme_e_serie = [vingadores, atlanta, friends, sete_vidas]
playlist_fim_de_semana = Playlist('Fim de semana', filme_e_serie)
print(f'{playlist_fim_de_semana.nome}')
print(f'Tamanho da lista: {len(playlist_fim_de_semana   )}')

for programa in playlist_fim_de_semana: #exemple that Polymorphis,'in' need date be iterable
    print(programa)

