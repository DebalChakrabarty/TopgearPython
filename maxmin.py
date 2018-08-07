''' 6. Create 3 Lists ( list1,list2,list3) with numbers and perform following operations
         a) Create Maxlist by taking 2 maximum elements from each list.
         b) Find average value from all the elements of Maxlist.
         c) Create a MinlIst by taking 2 minimum elements from each list 
         d) Find the average value from all the elements of Minlist '''


import random 

def maxGenerator(l):
	mi = min(l)
	for i in l:
		if i >mi and i!=max(l):
			mi = i
	yield max(l)
	yield mi	
def minGenerator(l):
	mi = max(l)
	for i in l:
		if i<mi and i!=min(l):
			mi = i
	yield min(l)
	yield mi
def average(l):
	s = 0
	for i in l:
		s+=i
	return s/len(l)

list1,list2,list3=[],[],[]
maxList=[]
minList=[]

def randomGenerator():
	for i in range(10):
		list1.append(random.randint(1,1000))
		list2.append(random.randint(1,1000))
		list3.append(random.randint(1,1000))
	return 1
randomGenerator()

maxList.extend(list(maxGenerator(list1)))
maxList.extend(list(maxGenerator(list2)))
maxList.extend(list(maxGenerator(list3)))

minList.extend(list(minGenerator(list1)))
minList.extend(list(minGenerator(list2)))
minList.extend(list(minGenerator(list3)))

print("the maxList is {0} \nthe minList is {1}".format(maxList,minList))

print("the average of maxList = {0}\nThe average of minList ={1}".format(average(maxList),average(minList)))


