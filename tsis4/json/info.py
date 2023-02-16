#JSON is a syntax for storing and exchanging data.
import json #import module for json
z=json.loads(x) #convert some x json to py 
z=json.dumps(x) #convert visa versa
"""
you can convert these datatypes into json:
dict
list
tuple
string
int
float
True
False
None
"""
json.dumps(x, indent=4) #indent is formatting 
json.dumps(x, indent=4, separators=(". ", " = ")) #separators in formatting
json.dumps(x, indent=4, sort_keys=True) #filter by alphabet
