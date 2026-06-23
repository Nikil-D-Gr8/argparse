import argparse

parser = argparse.ArgumentParser(allow_abbrev=True)
parser.add_argument("--fruit")
parser.add_argument("--vegetables")

print(parser.parse_args(["--fru", "hi"]))

# allow abreviation accepts arguments
# as long as they can be mapped unambigously
