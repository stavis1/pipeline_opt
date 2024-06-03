#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:15:34 2024

@author: anon
"""
### for interactive testing only
import os
os.chdir('/home/anon/Documents/hettich/SLT07_pipelineOpt/pipeline_opt/dev/')
import sys
sys.argv = sys.argv + '--options options.toml'
###

from pipeline_opt.options import options, validate_inputs, setup_workspace
args = options()

validate_inputs(args)
setup_workspace(args)
#preprocess_mzml(args)
    #this should produce a scan # -> RT mapping for the percolator/FlashLFQ adapter
    #or find a premade one listed in options.toml
#job_factory = load_parameters(args)
    #this object stores the available options for each parameter
    #and creates new jobs from completed
#completed = load_previous_save(args)
    #if restarting from a previous run this should read in the saved outcomes
    #otherwise initialize an empty completed runs object
#workers = initialize_workers(args)


