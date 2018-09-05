number = input("Enter a non negative integer for factorial : ")

n = 1
for i in range(int(number)):
	n = n * (i+1)
print(n) 
