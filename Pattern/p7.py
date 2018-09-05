n = int(input("Enter the number: ")) #This must be an odd number
c = '*'
for i in range(n):
    print(((c*(n-i-1)).rjust(n)+c+(c*(n-i-1)).ljust(n)).rjust(n*6)) 
