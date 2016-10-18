def array_test():
	a = [1,2,3,4]

	a.pop()

	a.append(7)
	print 'Index of 7: ', a.index(7)	#returns the index of given value

	a.remove(1)
	print 'Remove 1: ', a

	a.reverse()
	print 'Reversed a: ', a
	print 'Sorted a: ', sorted(a)

	a.sort()
	print 'Sorted a: ', a

def main():
	array_test()

if __name__ == '__main__':
	main()
