#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:17:00 2024

@author: anon
"""

import argparse
import sys
import os

class InputError(Exception):
    pass

class options():
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--options', actions = 'store', required=False, default=False,
                            help = 'The options toml file', metavar = 'options.toml')
        parser.add_argument('-p', '--print', actions = 'store', required=False, default=False,
                            help = 'Print the options toml file with the specified name', metavar = 'options.toml')
        args = parser.parse_args()
        if args.print:
            #copy options.toml to args.print
            sys.exit(0)
        
        if not args.options:
            raise InputError('One of -o or -p must be used.')
        
        import tomllib
        import logging        
        
        with open(args.options) as options:
            self.__dict__.update(tomllib.load(options))
        self.opfile = os.path.abspath(args.options)
        
        #set up logger
        self.logs = logging.getLogger('pipeline_opt')
        self.logs.setLevel(10)
        formatter = formatter = logging.Formatter('%(asctime)s | %(levelname)s: %(message)s')

        logfile = logging.FileHandler(os.path.join(self.working_directory, 'pipeline_opt.log'))
        logfile.setLevel(10)
        logfile.setFormatter(formatter)
        self.logs.addHandler(logfile)
        
        logstream = logging.StreamHandler()
        logstream.setLevel(self.log_level)
        logstream.setFormatter(formatter)
        self.logs.addHandler(logstream)


def validate_inputs(args):
    pass

def setup_workspace(args):
    import shutil
    
    os.chdir(args.working_directory)
    os.mkdir(args.output)
    os.mkdir(args.temp_dir)
    
    shutil.copy2(args.optfile, os.path.join(args.output, os.path.basename(args.optfile)))
    
    #I'll need to do substantially more work here to set up the initial temporary directories
    






