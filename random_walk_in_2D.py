from random import choice
from matplotlib import pyplot 

def main(end: int, numberOfWalks: int = 10):
	for i in range(0, numberOfWalks):
		plotRandomWalk(end)

	pyplot.title('Random Walk in 2 Dimensions')
	pyplot.show()


def plotRandomWalk(end: int):
	x, y = 0, 0
	x_coordinates = []
	y_coordinates = []

	for i in range(0, end):
		direction = choice(['N', 'W', 'S', 'E'])

		if direction == 'N':
			y += 1
		elif direction == 'S':
			y -= 1
		elif direction == 'W':
			x -= 1
		else:
			x += 1

		x_coordinates.append(x)
		y_coordinates.append(y)

	pyplot.plot(x_coordinates, y_coordinates)


if __name__ == '__main__':
	main(10000, 10)