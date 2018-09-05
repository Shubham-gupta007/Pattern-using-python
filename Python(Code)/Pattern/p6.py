n = int(input("enter the number:"))
c = '*'
for i in range(-1,n+1,2):
	print((c*i).ljust(n))

