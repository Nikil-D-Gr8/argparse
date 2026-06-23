import argparse

parser = argparse.ArgumentParser()


def main():
    parser.prog = "Main Prog"
    parser.print_help()


if __name__ == "__main__":
    main()


# prog value is by default the base name of the file invoked with python i.e sys.argv[0]
# if a directory or zipfile was used, the interpreter along with sys.argv[0] is shown.
# when its a directory, python interpreter along with -m becomes part of prog.
