s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)

"""
i/p:hello world or 123ab

"""
