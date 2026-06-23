import argparse

parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

parser.add_argument("--number")

print("with argparse default supressed", parser.parse_args())

parser = argparse.ArgumentParser(argument_default="hi")

parser.add_argument("--number")

print("without argparse default supressed", parser.parse_args())

# argument_default is used to globally set defaults for attributes
# it can be used to supress attribute creation too.
#
# argument_default works similar to default inside add_argument
# and set_default() for parser but globally
