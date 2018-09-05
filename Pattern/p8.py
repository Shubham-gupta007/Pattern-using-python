#width = 10
n = int(input("Enter number: "))
num = 65

for i in range(n+1):	
	ch = chr(num-1)
	print('%s' % ((ch*i).ljust(n)))	
	num = num + 1
	



