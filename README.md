# PyClosure

A console application that allows you to easily compile and optimize
your JavaScript files in **batches** using the [Google Closure
Compiler](https://developers.google.com/closure/compiler/).

# Install

Run the following command.

``` sh
pip3 install pyclosure
```

# Usage

``` sh
usage: python -m pyclosure [-h] [--input <INPUT_FILE/INPUT_DIR>] [--output <OUTPUT_FILE/OUTPUT_DIR>] [--level {WHITESPACE_ONLY, SIMPLE_OPTIMIZATIONS,ADVANCED_OPTIMIZATIONS} --extern <COMMA_SEPARATED_VARS>]
```

### Arguments

  - `-h, --help` - show the help menu
  - `--input` - enter the input file or directory (for batch processing)
  - `--output` - enter the output file name/folder name (for single processing, the default value is `index.min.js`.)
  - `--level` - the type of compilation to be used for the variables.
      - Supported values:
          - `WHITESPACE_ONLY`
          - `SIMPLE_OPTIMIZATIONS`
          - `ADVANCED_OPTIMIZATIONS`
  - `--extern` (optional) - enter in variables you want in your compiled
    code separated by **semi-colons**.