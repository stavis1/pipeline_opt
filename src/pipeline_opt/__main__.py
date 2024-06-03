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

from pipeline_opt.options import options, validate_inputs
args = options()

from pipeline_opt.support_utils import load_previous_save, preprocess_mzml, process_results, setup_workspace
from pipeline_opt.worker_utils import initialize_workers
from pipeline_opt.scheduler_utils import genetic_algorithm

validate_inputs(args)
setup_workspace(args)
scan_rt_map = preprocess_mzml(args)
    #this should produce a scan # -> RT mapping for the percolator/FlashLFQ adapter
    #or find a premade one listed in options.toml
completed = load_previous_save(args)
    #if restarting from a previous run this should read in the saved outcomes
    #otherwise initialize an empty completed runs object
workers = initialize_workers(args)
    #we just instantiate the objects here, no coomplecate logic
optimizer = genetic_algorithm(args)
    #again just instantiate here all logic comes next
    #params options files should be read in under __init__
results = optimizer.fit(scan_rt_map, completed, workers)
process_results(results, args)


