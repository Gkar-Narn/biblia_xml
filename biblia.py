# Definição do Objeto Biblia
import xml.etree.ElementTree as ET
import string
import re
import sys

class Biblia(object):
	""" Define objeto Biblia """

	def __init__(self, arquivo):
		'''Inicializa o objeto com a Biblia XML'''
		self.arquivo = arquivo
		tree = ET.parse(arquivo)
		self.biblia = tree.getroot()
		self.v_livros = list(self.biblia.iter('livro'))
		
	def versao(self):
		'''Retorna a versão carregada da Biblia neste objeto'''
		return self.biblia.attrib['tipo']

	def livros(self):
		'''Retorna todos os livros da Biblia em uma lista'''
		liv = []
		for livro in self.v_livros:
			liv.append(livro.attrib['nome'])
		return liv

	def livro_frm(self, liv):
		'''Devolve o nome do livro no formato de leitura: 1 Samuel = Primeiro Samuel'''
		livro = liv
		if ('1' in liv):
			if (('Sam' in liv) or ('Reis' in liv) or ('Cr' in liv)):
				livro = liv.replace('1','Primeiro')
			else:
				livro = liv.replace('1','Primeira')
		elif ('2' in liv):
			if (('Sam' in liv) or ('Reis' in liv) or ('Cr' in liv)):
				livro = liv.replace('2','Segundo')
			else:
				livro = liv.replace('2','Segunda')
		elif ('3' in liv):
			livro = liv.replace('3','Terceira')
		return livro

	def qte_capitulos(self, liv):
		'''Retorna a quantidade de capitulos para um determinado livro'''
		for l in self.v_livros:
			if str.lower(l.attrib['nome']) == str.lower(liv):
				return len(list(l))

	def qte_versiculos(self, liv, cap):
		'''Retorna a quantidade de versículos para um determinado livro, capítulo'''
		for l in self.v_livros:
			if str.lower(l.attrib['nome']) == str.lower(liv):
				c = list(l)
				if 1 <= cap <= len(c):
					return len(list(c[cap-1]))					

	def isLivro(self, liv):
		'''Verificador interno para assegurar que determinado livro está dentro da biblia'''
		flag = False
		for l in self.v_livros:
			if str.lower(l.attrib['nome']) == str.lower(liv):
				flag = True
		return flag

	def versiculo(self, liv, cap, vers):
		'''Retorna o texto na referência: Livro, Capítulo, Versículo'''
		for l in self.v_livros:
			if str.lower(l.attrib['nome']) == str.lower(liv):
				c = list(l)
				if 1 <= cap <= len(c):
					v = list(c[cap-1])
					if 1 <= vers <= len(v):
						return v[vers-1].text
				break

	def print_capitulo(self, liv, cap=9999, arquivo=sys.stdout):
		'''Imprime na saída padrão todo o capítulo do livro indicado, podendo
		enviar para um arquivo'''
		if self.isLivro(liv):			
			if 1 <= cap <= self.qte_capitulos(liv):
				for v in range(self.qte_versiculos(liv, cap)):
					vers = v + 1
					print(self.versiculo(liv, cap, vers), file=arquivo)

	def print_intervalo(self, liv, cap=9999, vers_i=1, vers_f=9999, arquivo=sys.stdout):
		'''Imprime um intervalo de versículos, podendo enviar para um arquivo'''
		if self.isLivro(liv):			
			if 1 <= cap <= self.qte_capitulos(liv):
				pos = vers_i
				while pos <= vers_f:
					texto = self.versiculo(liv, cap, pos)
					if texto != None:
						print(self.versiculo(liv, cap, pos), file=arquivo)
					else:
						break
					pos+=1
