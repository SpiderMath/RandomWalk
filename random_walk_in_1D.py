from random import choice
from matplotlib import pyplot 

def main(end: int, numberOfWalks: int = 10):
	for i in range(0, numberOfWalks):
		plotRandomWalk(end)
	pyplot.title('Random Walk in 1 Dimension')
	pyplot.show()


def plotRandomWalk(end: int):
	x, y = 0, 0
	x_coordinates = []
	y_coordinates = []

	for i in range(0, end):
		x += 1
		y += choice([-1, 1])
		x_coordinates.append(x)
		y_coordinates.append(y)

	pyplot.plot(x_coordinates, y_coordinates)


if __name__ == '__main__':
	main(10000)