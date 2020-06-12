
		minimun = i

		for i in range(i+1, n):

			if (array[j] < array[minu]):

				minimum = j
		#Swap the minimum element with the first element of the unsorted part
		temp = array[i]
		aray[i] = array[minimum]
		array[minimum] = temp

	return array

print(selectionSort(array))