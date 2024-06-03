#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:57:41 2024

@author: anon
"""

import os

def preprocess_mzml(args):
    pass

def load_previous_save(args):
    pass

def process_results(results, args):
    pass


def setup_workspace(args):
    import shutil
    
    os.chdir(args.working_directory)
    os.mkdir(args.output)
    os.mkdir(args.temp_dir)
    
    shutil.copy2(args.optfile, os.path.join(args.output, os.path.basename(args.optfile)))
    
    #I'll need to do substantially more work here to set up the initial temporary directories
    

