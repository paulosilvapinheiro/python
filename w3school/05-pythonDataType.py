"""
Python Data Types

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType

"""

#STRING
x = "Hello World"	
print(type(x))	
#INT
x = 20		
print(type(x))	
#FLOAT
x = 20.5		
print(type(x))	
#COMPLEX
x = 1j	
print(type(x))	
#LIST
x = ["apple", "banana", "cherry"]
print(type(x))			
#TUPLE
x = ("apple", "banana", "cherry")
print(type(x))
#RANGE			
x = range(6)	
print(type(x))		
#DICTIONARY
x = {"name" : "John", "age" : 36}	
print(type(x))	
#SET	
x = {"apple", "banana", "cherry"}
print(type(x))			
#FROZENSET
x = frozenset({"apple", "banana", "cherry"})	
print(type(x))		
#BOOLEAN
x = True		
print(type(x))	
#BYTES
x = b"Hello"	
print(type(x))		
#BYTESARRAY
x = bytearray(5)
print(type(x))			
#MEMORYVIEW
x = memoryview(bytes(5))
print(type(x))			
#NONETYPE
x = None		
print(type(x))	