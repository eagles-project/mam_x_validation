from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass
# Settings are stored here.
settings = Object()
# Input is stored here.
input = Object()
input.life=[[42],]

# Output data is stored here.
output = Object()
output.ans=[[42],]
