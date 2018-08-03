'''
Implement the function isListOfInts(), which takes a list, and checks if the list has
only "int" type values, as per the specification given below:
• The function should return True, if the list has only "int" type values, otherwise
should return False.
• The function should return True, if an empty list is passed as argument.
• If the argument is not of ‘list’ type, then the function should throw ValueError
exception, with the error message 'arg not of <list> type'
• The function should have only one return statement.
To test correctness of the function isListOfInts(),implement the function testList()
which is called as shown below and should produce output as indicated.
'''

import sys
def isWhiteLine(s):
    s.strip()
    if s=="":
        return True
    else:
        return False
with open(sys.argv[1]) as f:
    content = f.readLines()
    if isWhiteLine(content) is not True:
    print(content)
