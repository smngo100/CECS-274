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
			
        
# Version 2 of _merge helper function 
def _merge(leftArray, rightArray, array):
	i = 0 # left tracking position
	j = 0 # right tracking position  
	n = len(array) # number of elements in the array
	
	while i < len(leftArray) and j < len(rightArray): 
		if leftArray[i] < rightArray[j]:
			result.append(left[i])
			i += 1 
		else:
			result.append(right[j]
			j += 1 


def Merge_sort(array):
	if len(array) <= 1: 
		return array 
		
	mid = len(array) // 2 
	leftHalf = array[:mid]
	rightHalf = array[mid:]
	
	sorted_left_half = merge_sort(leftHalf)
	sorted_right_half = merge_sort(rightHalf)
	
	return _merga(sorted_left_half, sorted_right_half, array)
	

    

