import argparse

parser = argparse.ArgumentParser()

parser.print_usage()

print("----post_change----")

parser.usage = "%(prog)s is run as :"

parser.print_usage()

print("---end---")

# Usage argument is used to display how to use the program,
# in case it is changed, one should also pass it appropriately to
# the sub_parsers.
#
# The usage takes old c style printf formatting given here:
# https://docs.python.org/3/library/stdtypes.html?printf-style-string-formatting=#printf-style-string-formatting
