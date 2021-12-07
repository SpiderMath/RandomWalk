from random import choice
from matplotlib import pyplot 

pyplot.axes(projection='3d')

def main(end: int, numberOfWalks: int = 10):
	for i in range(0, numberOfWalks):
		plotRandomWalk(end)

	pyplot.title(f'{numberOfWalks} Random Walks in 2 Dimensions')
	pyplot.show()


def plotRandomWalk(end: int):
	x, y, z = 0, 0, 0
	x_coordinates = []
	y_coordinates = []
	z_coordinates = []

	for i in range(0, end):
		direction = choice(['N', 'W', 'S', 'E', 'U', 'D'])

		if direction == 'N':
			y += 1
		elif direction == 'S':
			y -= 1
		elif direction == 'W':
			x -= 1
		elif direction == 'U':
			z += 1
		elif direction == 'D':
			z -= 1
		else:
			x += 1

		x_coordinates.append(x)
		y_coordinates.append(y)
		z_coordinates.append(z)

	pyplot.plot(x_coordinates, y_coordinates, z_coordinates)


if __name__ == '__main__':
	main(1000, 1)