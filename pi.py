#import the math library and os library
from math import pi
from os import getenv
import os

env = 15

#Assign the value to of pi to a variable as float

my_float = float(pi)

#compute if there is a environmental variable present, if yes it will print that many digits of or pi of not default is 10

digits = int(os.getenv("DIGITS") or 10 )

print ("%.*f" % (digits, my_float))

os.getenv("DIGITS")
