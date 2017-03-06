#O(nlogn)
def quicksort(a):
	if len(a) < 2:
		return a
	pivot = a[0]
	a = a[1:]
	left = [i for i in a if i <= pivot]
	right = [i for i in a if i > pivot]
	return quicksort(left) + [pivot] + quicksort(right)

def heapsort(a):
	pass

def mergesort(a):
	pass

def insertsort(a):
	for i in xrange(1, len(a)):
		j = i - 1
		tmp = a[i]
		while j >= 0 and a[j] > tmp:
			a[j + 1] = a[j]
			j = j - 1
		a[j + 1] = tmp	
	return a

#O(n**2)
def bubblesort(a):
	for i in xrange(len(a) - 1, 0, -1):
		for j in xrange(0, i):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
				# tmp = a[j]
				# a[j] = a[j + 1]
				# a[j + 1] = tmp
	return a

def sort(a):
	print insertsort(a)
	print quicksort(a)
	print heapsort(a)
	print mergesort(a)
	print bubblesort(a)

if __name__ == "__main__":
	a = [100,21,42,52,231,66,32,51,199]
	sort(a)
