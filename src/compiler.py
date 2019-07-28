import http.client
import os
import urllib.parse

from threading import Thread
from utils.constants import *

class Compiler():

    def __init__(self, input_file, output_file, compilation_level = LEVEL_SIMPLE, external_vars = ''):
        self.input_file = input_file
        self.output_dir = output_file
        self.compilation_level = compilation_level
        self.external_vars = external_vars

    def compile(self):
        """Builds request to compile the file.
        """
        
        # Check if we searching a directory or not
        if os.path.isdir(self.input_file):
            # NOTE: Only searches for single level depth for now
            files = [f for f in os.listdir(self.input_file) if os.path.isfile(os.path.join(self.input_file, f))]

            self._process_batch(files)
        else:
            self._process_single(self.input_file, self.output_dir)

    def _process_batch(self, files):
    
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        workers = [
            Thread(target = self._process_single, args = (file_path, os.path.join(self.output_dir, file_path), self.input_file)) for file_path in files
        ]

        for worker in workers:
            worker.start()

        # Wait for completion
        for worker in workers:
            worker.join()

    def _process_single(self, input_file_name, output_file, root = './'):
        path = os.path.join(root, input_file_name)
        js_code = open(path, 'r')

        params = urllib.parse.urlencode([
            ('js_code', js_code.read()),
            ('compilation_level', self.compilation_level),
            ('output_format', 'text'),
            ('output_info', 'compiled_code'),
            ('js_externs', self.external_vars)
        ])

        js_code.close()
        self._forward_request(params, output_file)

    def _forward_request(self, params, path):
        headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        conn = http.client.HTTPSConnection('closure-compiler.appspot.com')
        conn.request('POST', '/compile', params, headers)
        response = conn.getresponse()
        data = response.read()
        output_code = open(path, 'w+')
        output_code.write(data.decode('utf-8'))
        output_code.close()
        conn.close()
