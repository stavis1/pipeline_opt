#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:14:42 2024

@author: anon
"""


class worker():
    def __init__(self, args):
        self.__dict__.update(args.worker_args)
        
    def calc_metrics(self, result):
        pass
    
    def run_comet(self, comet_params):
        pass
    
    def run_percolator(self, percolator_params):
        pass
    
    def run_flashlfq(self, flashlfq_params):
        pass
    
    def run_pipeline(self, params):
        self.run_comet(self, params['comet'])
        self.run_percolator(self, params['percolator'])
        self.run_flashlfq(self, params['flashlfq'])

def initialize_workers(args):
    pass


