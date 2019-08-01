import unittest
import os
import sys
import shutil
sys.path.append('.')

from pyclosure import Compiler
from utils.constants import *

SINGLE_TEST_RES = 'function debounce(b,f,c){var a;return function(){var d=this,e=arguments,g=c&&!a;clearTimeout(a);a=setTimeout(function(){a=null;c||b.apply(d,e)},f);g&&b.apply(d,e)}}var myEfficientFn=debounce(function(){},250);window.addEventListener("resize",myEfficientFn);\n'

LEVEL_TEST_WHITESPACE = 'function hello(name){alert("Hello, "+name)}hello("New user");\n'
LEVEL_TEST_SIMPLE = 'function hello(a){alert("Hello, "+a)}hello("New user");\n'
LEVEL_TEST_ADVANCED = 'alert("Hello, New user");\n'

BATCH_TEST_1 = 'function once(a,c){var b;return function(){a&&(b=a.apply(c||this,arguments),a=null);return b}}var canOnlyFireOnce=once(function(){console.log("Fired!")});canOnlyFireOnce();canOnlyFireOnce();\n'
BATCH_TEST_2 = 'var getAbsoluteUrl=function(){var a;return function(b){a||(a=document.createElement("a"));a.href=b;return a.href}}();\n'

class TestCompiler(unittest.TestCase):

    def setUp(self):
        shutil.rmtree('tests/out')
        os.makedirs('tests/out')

        self.compiler = None

        self.TEST_SINGLE_DIR = 'tests/test_single'
        self.TEST_LEVELS_DIR = 'tests/test_levels'
        self.TEST_BATCH_DIR = 'tests/test_batch'
        self.OUTPUT_DIR = 'tests/out'
        self.OUTPUT_BATCH = 'tests/test_batch'

    def test_single(self):
        input_path = os.path.join(self.TEST_SINGLE_DIR, 'test_file_single.js')
        output_path = os.path.join(self.OUTPUT_DIR, 'test_file_single.js')

        self.compiler = Compiler(input_path, output_path)
        self.compiler.compile()

        contents = self._read_file(output_path)
        assert contents == SINGLE_TEST_RES

    def test_levels(self):
        input_path = os.path.join(self.TEST_LEVELS_DIR, 'test_file_level.js')
        output_path_whitespace = os.path.join(self.OUTPUT_DIR, 'test_file_whitespace.js')
        output_path_simple = os.path.join(self.OUTPUT_DIR, 'test_file_simple.js')
        output_path_advanced = os.path.join(self.OUTPUT_DIR, 'test_file_advanced.js')

        self.compiler = Compiler(input_path, output_path_whitespace, LEVEL_WHITESPACE)
        self.compiler.compile()
        self.compiler = Compiler(input_path, output_path_simple)
        self.compiler.compile()
        self.compiler = Compiler(input_path, output_path_advanced, LEVEL_ADVANCED)
        self.compiler.compile()

        assert self._read_file(output_path_whitespace) == LEVEL_TEST_WHITESPACE
        assert self._read_file(output_path_simple) == LEVEL_TEST_SIMPLE
        assert self._read_file(output_path_advanced) == LEVEL_TEST_ADVANCED

    def test_batch(self):
        input_path = self.TEST_BATCH_DIR
        output_path = self.OUTPUT_BATCH
        file_1 = os.path.join(output_path, 'test1.js')
        file_2 = os.path.join(output_path, 'test2.js')

        self.compiler = Compiler(input_path, output_path)
        self.compiler.compile()

        assert self._read_file(file_1) == BATCH_TEST_1
        assert self._read_file(file_2) == BATCH_TEST_2

    def _read_file(self, path):
        f = open(path, 'r')
        contents = f.read()
        f.close()
        return contents

    def tearDown(self):
        self.compiler = None

if __name__ == '__main__':
    unittest.main()