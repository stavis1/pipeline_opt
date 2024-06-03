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

#read input
#intiialize worker pool

#



