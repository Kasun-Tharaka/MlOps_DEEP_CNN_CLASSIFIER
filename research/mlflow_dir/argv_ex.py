import sys

default = 0.3

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else default
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else default

args = sys.argv
print(args)
print(alpha, l1_ratio)

# python filename.py 0.6 0.7

#argv converts value other type 
# in this case convert into float

#default it converts into str