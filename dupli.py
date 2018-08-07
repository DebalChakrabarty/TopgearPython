s  = input("Enter space separated integers")
l = s.split()
l = [int(x) for x in l]
print(l)
for i in l:
	while l.count(i) > 1:
		l.remove(i)
print("the list after deleting duplicate elements is {0}".format(l))



