import random

def bubble_sort(a):
	for i in range(0, len(a)-1):
		for j in range(0, len(a)-1-i):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j] 

	return a

def insertion_sort(a):
	for i in range(0, len(a)):
		key = a[i]
		j = i - 1
		while j >= 0 and key < a[j]:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = key

	return a

def merge_sort(a):
	n = len(a)
	if n == 1:
		return a

	left = a[:n//2]
	right = a[n//2:]
	left = merge_sort(left)
	right = merge_sort(right)
	return merge(left, right)

def merge(a, b):
	c = []
	while len(a) > 0 and len(b) > 0:
		if a[0] > b[0]:
			c.append(b[0])
			b.pop(0)
		else:
			c.append(a[0])
			a.pop(0)

	while len(a) > 0:
		c.append(a[0])
		a.pop(0)

	while len(b) > 0:
		c.append(b[0])
		b.pop(0)
	return c

def quick_sort(a, low, high):
	if len(a) == 0:
		return a

	if low < high:
		partition = part(a, low, high)
		quick_sort(a, low, partition-1)
		quick_sort(a, partition+1, high)

	return a

def part(a, low, high):
	min_index = low-1
	pivot = a[high]

	for i in range(low, high):
		if a[i] <= pivot:
			min_index+=1
			a[min_index], a[i] = a[i], a[min_index]

	a[min_index+1], a[high] = a[high], a[min_index+1]

	return min_index+1

if __name__ == '__main__':
	array = []
	for i in range(15):
		array.append(random.randrange(0,1001))
	print("Unsorted array:\n",array)
	print("With Quick sort:\n",quick_sort(array.copy(),0,len(array)-1))
	print("With Bubble sort:\n",bubble_sort(array.copy()))
	print("With Insertion sort:\n",insertion_sort(array.copy()))
	print("With Merge sort:\n",merge_sort(array.copy()))