








"""
Function to print a string and the length of the string
Parameters
    -string
Exceptions
    -If string is NULL, handles it.
Returns
    -No return value
"""
def printStringAndLength(string):
    try:
        print string
        length = len(string)
        print 'Length of string is ..'+str(length)
    except:
        print 'ERROR: A string input is needed'




if __name__=='__main__':
    print 'Hello world'
    printStringAndLength('Hello world')