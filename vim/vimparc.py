def sort(a):
	if len(a) < 2:
		return a
	pivot = a[0]
	left = []
	right = []
	a = a[1:]
	left = [x for x in a if x < pivot]
	right = [x for x in a if x >= pivot]
	return sort(left) + [pivot] + sort(right)

if __name__ == "__main__":
	a = [1,3,4,8,2,5,3,6,7]
	print sort(a)
