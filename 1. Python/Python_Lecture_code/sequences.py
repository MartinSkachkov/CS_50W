name = "Harry"
print(list(name))

l = [1, 2.34, "h"]
print(l)

coord = (1, 2)
print(coord[0])

s = set()

# note that the elements themselves must be immutable
s.add(1)
#s.add([1,2])
s.add("hello")
s.remove(1)

print(s[0])