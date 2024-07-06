import argparse


parser = argparse.ArgumentParser(description="Module Template")

parser.add_argument("-f", "--file", type=str, help="Please input filename")
parser.add_argument("--data-value", type=int, help="Please input integer value")

args = parser.parse_args()

print("argument-file:", args.file)

# WARNING 1: Command line argument `--data-value` is not used


def process_value(dataValue):
    pass


if __name__ == "__main__":
    # WARNING 2: Formal argument `dataValue` of function `process_value`
    #   spells like the command-line parameter `data_value`.
    #   Please make sure that the value `0` is not shadowing the command-line argument.
    process_value(0)
