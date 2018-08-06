def convert(n):
	a = n//8
	b = n%8
	l =[]
	for i in range(a):
		l.append(str(255))
	d,s=7,0
	for i in range(b):
		s+= 2**d
		d-=1
	l.append(str(s))
	while len(l) < 4:
		l.append(str(0))
	return '.'.join(l)
inp = int(input("enter the number"))
if inp > 32 or inp < 0:
	print("invalid input")

print(convert(inp))
	
