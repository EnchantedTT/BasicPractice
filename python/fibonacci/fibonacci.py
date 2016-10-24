def fibonacci(number):
	if number <= 0:
		return 0
	elif number == 1:
		return 1
	elif number == 2:
		return 1
	else:
		return fibonacci(number - 1) + fibonacci(number - 2)

if __name__ == "__main__":
	for i in range(10):
		print fibonacci(i)