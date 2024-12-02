# Version 1 of _merge helper function 
# a[i] = the element at index i of array a
def _merge(leftArray, rightArray, array):
	i = 0 # left tracking position / index
	j = 0 # right tracking position / index
	n = len(array) # number of elements in the array

	for i in range(n):
	        if i >= len(leftArray):	# Means we've reached or passed the end of the array
			array[i] = rightArray[j]
			j += 1
		elif j >= len(rightArray): 
			array[i] = leftArray[i]
			i += 1 
		else: 
			a[i] = rightArray[j]
			j += 1 


def Merge_sort(array):
	if len(array) <= 1: 
		return array 
		
	mid = len(array) // 2 
	leftHalf = array[:mid]
	rightHalf = array[mid:]
	
	sorted_left_half = merge_sort(leftHalf)
	sorted_right_half = merge_sort(rightHalf)
	
	return _merge(sorted_left_half, sorted_right_half, array)
	










def _partition_f(a: List, start, end):
	pivot = a[start]
	i = start + 1 
	j = end - 1

	while i < j: 
		while i < end and a[i] < pivot: 
			i += 1 
		while j > start and a[j] >= pivot: 
			j -= 1 
		if i < j: 
			a[i], a[j], a[j], a[i]

	if a[j] > pivot: 
		a[j], a[end] = a[end], a[j]

	return i 


def _quick_sort_f(a: List, start, end):
	if start < end:
        	p = _partition_f(a, start, end)

        	# Recursion
        	_quick_sort_f(a, start, p - 1)  # first half
        	_quick_sort_f(a, p + 1, end)    # second half
    	elif start >= end:
        	return a


def _quick_sort_r(a: List, start, end):
	if start < end:
        	p = _partition_f(a, start, end)

        	# Recursion
        	_quick_sort_f(a, start, p - 1)  # first half
        	_quick_sort_f(a, p + 1, end)    # second half
    	elif start >= end:
        	return a


def quick_sort(a: List, p=True):
	"""
	sorts an ArrayList a using the quick sort algorithm.
	If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
	Otherwise, the quick sort algorithm uses the first element as pivot.
	"""
	if p:
		_quick_sort_r(a, 0, len(a) - 1) 
	else:
		_quick_sort_f(a, 0, len(a) - 1) 
	












