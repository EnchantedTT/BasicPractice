from linked_list import LinkedList

def main():
	l_list = LinkedList()

	print 'Init size:', len(l_list) 
	l_list.append(123)

	print 'Size after append:', len(l_list)

	print l_list

	l_list.push(11)
	l_list.push(45)
	print 'List after push:', l_list


	l_list.delete(123)
	#l_list.delete(11)
	print 'List after delete 11:', l_list

	l_list.pop()
	print 'Pop one:', l_list

	print 'contains 11: ', l_list.contains(11)

	l_list.push(53)
	l_list.push(78)
	l_list.push(22)
	l_list.push(9)
	print 'List before reverse: ', l_list

	l_list.reverse()
	print 'List after reverse: ', l_list	

if __name__ == "__main__":
	main()
