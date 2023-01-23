import math
a = float(input("Podaj przyprostokatna a trojkata!"))
b = float(input("Podaj przyprostokatna b trojkata!"))

class Triangle:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def hypotenuse(self):
		return math.sqrt(self.a ** 2 + self.b ** 2)

if __name__ == "main":
	a = float(input("Podaj przyprostokatna a trojkata! /n"))
	h = float(input("Podaj przyprostokatna b trojkata! /n"))

our_triangle = Triangle(a, b)

print(f'Przeciwprostokątna twojego trójkąta wynosi: {our_triangle.hypotenuse()}')

