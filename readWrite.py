def readWrite():
	with open("input.txt") as f:
		content =f.readlines()
		print(content)
		wc=0
		cc=0
		yield len(content)
		for i in content:
			for k in i:
				if k.isspace():
					wc+=1
				else:
					cc+=1
		yield wc+1
		yield cc
	

a,b,c = readWrite()

print("no of lines {0} \nno of words {1}\nno of characters {2}".format(a,b,c))


	
		
