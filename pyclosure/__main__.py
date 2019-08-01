#!/usr/bin/env python3

import sys
import argparse

from utils.constants import *
from pyclosure import Compiler

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help = HELP_INPUT_FILE)
    parser.add_argument('--output', default = DEFAULT_OUT, help = HELP_OUTPUT_FILE)
    parser.add_argument('--level', default = LEVEL_SIMPLE, choices = [LEVEL_SIMPLE, LEVEL_WHITESPACE, LEVEL_ADVANCED], help = HELP_OPTIMIZATION_LEVEL)
    parser.add_argument('--extern', default = '', help = HELP_EXTERNAL_VARS)

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return

    comp = Compiler(args.input, args.output, args.level, args.extern)
    comp.compile()

if __name__ == "__main__":
    main()
