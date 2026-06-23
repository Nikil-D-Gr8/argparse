import argparse

parser = argparse.ArgumentParser()

print("-------Before")

parser.print_help()

print("-------After")

parser.description = "This is the new description"
parser.epilog = "This is an epilog"

parser.print_help()


# By default description and epilog is empty and can be provided,
# it is line wrapped and can be controlled
# with the help of formatter_class""
