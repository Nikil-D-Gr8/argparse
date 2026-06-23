import argparse

parser = argparse.ArgumentParser(add_help=False)

print(parser._actions)

parser = argparse.ArgumentParser(add_help=True)

print(parser._actions)

# add_help determines if add_argument is called on -h and --add_help
# without it you cant use the help flag.
