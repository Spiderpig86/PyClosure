import http.client
import urllib.parse

class Compiler():

    def __init__(self, input_file, output_file, compilation_level, external_vars):
        self.input_file = input_file
        self.output_file = output_file
        self.compilation_level = compilation_level
        self.external_vars = external_vars

    def compile(self):
        pass