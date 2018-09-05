#width = 10
n = int(input("Enter the number: "))
num = str(int(1))
for i in range(n+1):
	print ('%s' % ((num*i).ljust(n)))
	num = str(int(1)+i)


n = int(input("Enter the number: "))
num = str(int(9))
for i in range(n+1):
	print ('%s' % ((num*i).rjust(n)))
	num = str(int(9)-i)
	#num2 = str(int(1)+ i) + str(int(i))
	#print(num2) 




n = int(input("Enter the number: "))
num = str(int(1))
for i in range(n+1):
	print ('%s' % ((num*i).ljust(n)))
	num = str(int(1)+i)


n = int(input("Enter the number: "))
num = str(int(5))
for i in range(n,-1,-1):
	print ('%s' % ((num*i).ljust(n)))
	num = str(int(i-1))

n = int(input("Enter the number: "))
num = str(int(5))
for i in range(n,-1,-1):
	print ('%s' % ((num*i).rjust(n)))
	num = str(int(i-1))


n = int(input("Enter the number: "))
num = str(int(5))
for i in range(n,-1,-1):
	print ('%s' % ((num*i).ljust(n)) + '%s' % ((num*i).rjust(n)))
	num = str(int(i-1))



n = int(input("Enter the number: "))
num = str(int(1))
for i in range(n+1):
	print ('%s' % ((num*i).ljust(n)) + '%s' % ((num*i).rjust(n)))
	num = str(int(1)+i)



n = int(input("Enter the number: "))
num = str(int(5))
for i in range(n,0,-1):
	print ('%s' % ((num*i).ljust(n)) + '%s' % ((num*i).rjust(n)))
	num = str(int(i-1))
for i in range(n):
	print ('%s' % ((num*i).ljust(n)) + '%s' % ((num*i).rjust(n)))
	num = str(int(1)+i)

