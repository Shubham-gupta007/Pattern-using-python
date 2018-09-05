
n = int(input("Enter the number: "))
num = str(int(5))
for i in range(n,0,-1):
	print ('%s' % ((num*i).ljust(n)) + '%s' % ((num*i).rjust(n)))
	num = str(int(i-1))
for i in range(1,n+1):
	print ('%s' % ((num*i).ljust(n)) + '%s' % ((num*i).rjust(n)))
	num = str(int(1)+i)

