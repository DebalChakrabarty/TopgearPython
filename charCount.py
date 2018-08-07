'''3. Write a program to receive a string from keybord and check if the string has two 'e' in the characters. 
   If yes return True else False.'''




def charCount():
	a = raw_input("enter the string")
	l = list(a)
	print(l)
	if l.count('e')==2:
		return True
	else:
		return False
print(charCount())


