def charCount():
	a = raw_input("enter the string")
	l = list(a)
	print(l)
	if l.count('e')==2:
		return True
	else:
		return False
print(charCount())


