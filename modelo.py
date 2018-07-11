# -*- coding: utf-8 -*-

#Classes Abstradas
from abc import ABCMeta, abstractmethod  # abstract base classes

from collections.abc import MutableSequence
from numbers import Complex

class Programa(metaclass = ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano        
        self._likes = 0
    
    def dar_like(self):        
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()  

    @abstractmethod 
    def __str__(self):
        pass

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'
        

class Serie(Programa):    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlist:
    def __init__(self, nome, programas):        
        self._programas = programas
        self.nome = nome

    def __getitem__(self, item):
       return self._programas[item] 
    
    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas
    



if __name__ == '__main__':
    
    vingadores = Filme('vingadores - guerra inifinta', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)

    tmep = Filme('todo mundo em pânico', 199,100)
    demolidor = Serie('Demolidor', 2016, 2)

    vingadores.dar_like()        
    vingadores.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    atlanta.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()                

    filmes_e_series = [vingadores, atlanta, demolidor, tmep]

    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

    print(f'Play List: {playlist_fim_de_semana.nome}')
    print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')
    for programa in playlist_fim_de_semana:
        #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
        print(programa)