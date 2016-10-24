import random
import math

def main():
	total_distance = 0
	total_step = 100
	x = [random.random() for i in range(total_step)]
	tag = [random.randrange(-1, 2, 2) for i in range(total_step)]
	total_x = 0
	total_y = 0
	for i in range(total_step):
		total_x += x[i] * tag[i]
		total_y += tag[i] * math.sqrt(1 - x[i]*x[i])
		total_distance = math.sqrt(total_x * total_x + total_y * total_y)
	return total_distance

#one step one meter, random direction, 100 steps total
if __name__ == '__main__':
	iteration = 100000
	avg_distance = 0
	distance = 0
	for i in range(iteration):
		distance += main()
	avg_distance = distance / iteration
	print "avg_total: ", avg_distance