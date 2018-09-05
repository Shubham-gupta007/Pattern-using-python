n = int(input("enter the number:"))
c = '*'
for i in range(n,-1,-2):
	print((c*i).ljust(n))



n = int(input("enter the number:"))
c = '*'
for i in range(n+1):
	print((c*i).rjust(n) + c + (c*i).ljust(n))
for i in range(n, -1,-1):
	print((c*i).rjust(n) + c + (c*i).ljust(n))



n = int(input("enter the number:"))
c = '*'
for i in range(n+1):
	print((c*i).ljust(n))
for i in range(n-1,-1,-1):
	print((c*i).ljust(n))
