class Nodo:

	def __init__(self, valor):
		self.valor = valor
		self.hijos  = []

	def agregar_hijo(self, hijo):
		self.hijos.append(hijo)	
	
	def imprimirme(self):
		print(self.valor+ '\n')
		print(self.hijos, '\n')