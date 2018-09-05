


n = int(input("Enter number: "))
num = 65

for i in range(n+1):	
	ch = chr(num-1)
	print('%s' % ((ch*i).ljust(n)))	
	num = num + 1

"""
o/p:

A    
BB   
CCC  
DDDD 
EEEEE

prblm
i have to print below pattern using ljust

A
BC
DEF
GHIJ
KLMNO


what should i do?

"""
