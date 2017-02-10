def binarysearch(a, x, start, end):
	if start >= end:
		return -1
	else:
		mid = (end + start) / 2
		if x == a[mid]:
			return mid
		elif x > a[mid]:
			start = mid + 1
		else:
			end = mid
		return binarysearch(a, x, start, end)

def binarysearch2(a, x):
	start = 0
	end = len(a)
	while(start < end):
		mid = (end + start) / 2
		if x == a[mid]:
			return mid
		elif x > a[mid]:
			start = mid + 1
		else:
			end = mid
	return -1

if __name__ == "__main__":
	a = [i for i in range(1000)]
	print binarysearch(a, 44, 0, len(a))
	print binarysearch2(a, 44)