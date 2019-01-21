import sys

args = sys.argv

if len(args) < 4:
    raise Exception("argument num should be 4")

x, y, z = args[1:]

print("{}時の{}は{}".format(x, y, z))
