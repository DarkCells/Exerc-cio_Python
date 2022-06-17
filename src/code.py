#python3.10

"""
@author DarkCells
"""
from datetime import datetime

class Jogador(object):
	def __init__(self, nome, posicao, dataNascimento, nacionalidade, altura, peso):
		self.nome = nome
		self.posicao = posicao
		self.dataNascimento = dataNascimento
		self.nacionalidade = nacionalidade
		self.altura = altura
		self.peso = peso

	def calcularIdade(birthDate):
		data_atual = date.today()
		dataNascimento = int(input('Qual a sua data de nascimento'))
		data_actual = data_atual.year()
		idade = data_atual - dataNascimento
		print(idade)

"""
	def CalcularAposentadoria(self):
		if idade == '40'or idade == '38' or idade == '36':
			pass
"""
