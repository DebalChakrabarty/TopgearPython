''' 9. Create a suitable object type and  check for file size of 0 bytes of the directory contents as shown below
02/15/2016              10:49 PM               962                     switchfinal.py
02/15/2016             10:49 PM               943                       switchfinal.py.bak
01/27/2016             11:46 AM                15                        t.py
03/31/2016            12:39 PM               840                        t1.py
01/25/2016            10:34 AM             2,407                      tc1.py
02/14/2017           09:13 AM                 0                           teat.py
03/15/2016          05:52 PM                 5                             tes.py '''


with open("dir.txt") as f:
	content = f.readlines()
	l=[]
	for i in content:
		l.append(i.split())
	for i in l:
		if i[3]=='0':
			print("file {0} created on {1} at {2} {3} is of size 0 bytes".format(i[4],i[0],i[1],i[2]))




