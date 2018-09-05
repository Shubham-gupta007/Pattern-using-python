number = input("Enter a non negative integer for factorial : ")


def factorial(number):
	n = 1
	for i in range(number):
		n = n * (i+1)
	return n

print(factorial(number))
