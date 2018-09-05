n = int(input("Enter number: "))
num = 69

for i in range(n+1):	
	ch = chr(num-1)
	print((ch*i).ljust(n))	
	num = num + 1
