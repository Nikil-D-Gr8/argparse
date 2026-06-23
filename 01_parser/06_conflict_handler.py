import argparse

parser = argparse.ArgumentParser(conflict_handler="resolve")

parser.add_argument("--foo", action="store_true")
parser.add_argument("--foo")

print(parser.parse_args(["--foo", "hi"]))

# Two actions cant exist with the same option
# in order for overriding previous option, the option resolve
# can be passed.
