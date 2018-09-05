

n = int(input("enter the number:")) #This must be an odd number
c = '*'
for i in range(n+1):
	print((c*i).ljust(n))



n = int(input("Enter the number:"))
c = '*'
for i in range(n+1):
	print((c*i).rjust(n))


n = int(input("enter the number:"))
c = '*'
for i in range(n+1):
	print((c*i).ljust(n) + (c*i).rjust(n))

n = int(input("enter the number:"))
c = '*'
for i in range(n+1):
	print((c*i).rjust(n) + c + (c*i).ljust(n))

