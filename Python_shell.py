# welcome to the RC Python workshop.
# to get stared run your first code.


# use "#%%" to divide your code into cells
# use "#" to make comments to your code
#%%

# 1. Variables (Named storage for data) and data types
'''
 data types:
     int: Integer -> eg. 10
     Float: eg. 2.5
    complex: complex numbers -> eg. 3 + 4j
    str: string values -> eg. "Hello, World!
    bool: booleans -> eg. True/False
    list: lists -> eg. [1, 2, 3, 4, "stable"]
    tuple: tuples -> eg. (5, 6, 7, "stable")
    range: ranges -> eg. range(0, 10)
    dict: dictionaries -> eg. {"name": "Caivil", "age": 25}
    set: sets -> eg. {1, 2, 3, 4}

'''
a = 10
b = 15

print(a)
print(a,b)
print('a')

call = "good day sir"
print(call)
print(Call)

a1 = 20
print(a1)
#%%
#2. F String


#%%
#3. Comparison operator (==, !=, >, <, >=, <=) #output is boolean (True/False)
a = 8
b = 10

a == b # is a the SAME as b -> output: False
a!=b # is a NOT SAME as b -> output: True
a>b # a GREATER THAN b -> output: False
a<b # a LESS THAN b -> output: true
a>=b # a GREATER THAN OR EQUAL TO b -> output: False
a<=b # a LESS THAN OR EQUAL TO b -> output: True

#%%
# 4. logical operator (and or not)
a=5
b= 10

a<8 and a>6 # If one premise is false, the whole statement is false.

a<8 or a>10 # If one premise is true, the statement is true.

a!=b or a>b and a<=b # and has higher precedence than or

#%%
# 5. List


#%%
# 6.  Dictionary


#%%
# 7. Input function


#%%
# 8. IF statment
'''
if(conditional statement):
(statement to be executed)
'''


'''
################ GOLD PREDICTOR ACTIVITY ################

Instructions:
- Ask the user to enter the mass of a metal object.
- If the mass is between 35g and 60g (inclusive), it's GOLD!
- If it's less than 35g, it's too small to be gold.
- If it's more than 60g, it's too big to be gold.
- Use an f-string to show the exact mass in your output.

Example:
Input: 45
Output: We found Gold with a mass of 45g, boss!
'''

#%%
# 9. Defining a function



#return vs print
'''
# Difference between print() and return

- print():  
  * Shows the result on the screen immediately.  
  * Used to display output to the user.  
  * Does NOT send the result back for further use.

- return:  
  * Sends the result back to where the function was called.  
  * Allows you to save or reuse the result later in your program.  
  * Does NOT automatically display anything unless you print it.

'''

#%%
# 10. For Loop ( for repeatation and repeating a process)

#%%
# 11. While loop


#%%
#  12. Exception handling (#code is executed even when error occurs)
'''
common types of exceptions are:

ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero.
TypeError: Raised when an operation or function is applied to an object of inappropriate type.
ValueError: Raised when a built-in operation or function receives an argument that has the right
type but an inappropriate value.
IndexError: Raised when a sequence subscript is out of range.
KeyError: Raised when a dictionary key is not found.
FileNotFoundError: Raised when a file or directory is requested but doesn’t exist.
IOError: Raised when an I/O operation (such as a print statement, the built-in open() function or
a method of a file object) fails for an I/O-related reason.
ImportError: Raised when an import statement fails to find the module definition or when a from
... import fails to find a name that is to be imported.
MemoryError: Raised when an operation runs out of memory.
OverflowError: Raised when the result of an arithmetic operation is too large to be expressed by
the normal number format.
AttributeError: Raised when an attribute reference or assignment fails.
SyntaxError: Raised when the parser encounters a syntax error.
IndentationError: Raised when there is incorrect indentation.
NameError: Raised when a local or global name is not found
'''

# the flow of the code
'''
try:
    # risky code
except SomeError:
    # what to do if error happens
'''



##################################### WE ARE DONE!!!###############################################
#################### WELL DONE! THE STUDENT IS ONLY AS GOOD AS THE MASTER #########################
#%%################################################################################################