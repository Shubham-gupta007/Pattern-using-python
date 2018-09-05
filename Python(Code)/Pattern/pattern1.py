
"""
r = int(input("Enter the no. rows: "))
for i in range(1,r+1):
	for j in range(1, i+1):
		print("*",end="")
	print()

thickness = int(input()) #This must be an odd number
c = '*'
for i in range(thickness+1):
    print((c*i).ljust(thickness))
"""

thickness = int(input()) #This must be an odd number
c ='*'
for i in range(thickness+1):
    print((c*i).ljust(thickness+1))

