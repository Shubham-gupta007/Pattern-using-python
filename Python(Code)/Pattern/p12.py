n = int(input("Enter number: "))
num = 65
ch = chr(num)
for i in range(n+1):
	print('%s' % ((ch*i).rjust(n)))
	num = num + i

