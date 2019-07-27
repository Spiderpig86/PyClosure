"""App Constants
"""

from collections import namedtuple

#  Help Messages
HELP_INPUT_FILE = 'Name of the input file.'
HELP_OUTPUT_FILE = 'Name of the output file.'
HELP_OPTIMIZATION_LEVEL = 'The level of optimization for JavaScript files.'
HELP_EXTERNAL_VARS = 'Add external JS variaables and functions delimited with semicolons.'

# Default Values
DEFAULT_OUT = 'index.min.js'
DEFAULT_LEVEL = LEVEL_WHITESPACE

# Level Choices
LEVEL_WHITESPACE = 'WHITESPACE_ONLY'
LEVEL_SIMPLE = 'SIMPLE_OPTIMIZATIONS'
LEVEL_ADVANCED = 'ADVANCED_OPTIMIZATIONS'

# Types
Conf = namedtuple('Conf', ['output', 'compile_level'])

def default_conf():
    return Conf(
       output = DEFAULT_OUT,
       compile_level = DEFAULT_LEVEL
    )

def to_conf(conf):
    return Conf(
       output = conf['output'],
       compile_level = conf['compile_level']
    )