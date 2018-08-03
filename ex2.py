''' 
Implement the function isWhiteLine(), which takes a string and returns TRUE if the
string contains only white space & tab characters.
Making use of the above function, write a program, which should read a file given as
command-line argument, and print only non-blank lines onto the standard output.
'''
def isListOfInts(l):
    if type(l) is not list:
        raise ValueError("arg not of <list> type")
    flag  = True
    for i in l:
        if type(i) is int:
            continue
        else:
            flag = False
    return flag

def testList():
    print(isListOfInts([]))
    print(isListOfInts([1]))
    print(isListOfInts([1,2]))
    print(isListOfInts([0]))
    print(isListOfInts(['1']))
    print(isListOfInts([1,'a']))
    print(isListOfInts(['a',1]))
    print(isListOfInts([1, 1.]))
    print(isListOfInts([1., 1.]))
    print(isListOfInts((1,2)))
testList()
