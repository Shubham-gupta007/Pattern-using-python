

"""
n = int(input("Enter the size of array: "))
array = list()

print("Enter the number in the array: ")
for i in range(int(n)):
	n = input("num :")
	array.append(n)
print("Array: ", array )
print("sorted array: ", sorted(array))


"""


n = int(input("Enter the size of array1: "))
arr = input("Enter the number in array1: ")   # takes the whole line of n numbers
array1 = list(map(int,arr.split(' ')))

n = int(input("Enter the size of array2: "))
arr = input("Enter the number in array2: ")
array2 = list(map(int,arr.split(' ')))
def checkArray():
	if len(array1) == len(array2):
		return True
	else:
		return False
def sqr(x):		
	return(x**2) 
square = list(map(sqr, array1))
print("array:", array1)
print("Sorted array: ", sorted(array1))
print("Square:", square,  "\tsortedSquare:", sorted(square))
print(checkArray())




