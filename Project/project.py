'''
PROCESS MINING
project for the process mining course at the university of Padua

Project 1: How much variable is my event log?

author: Marco Baggio
mat: 1179124
'''
from pm4py.objects.log.importer.xes import factory as xes_import_factory
from pm4py.algo.filtering.log.variants import variants_filter

import argparse

parser = argparse.ArgumentParser(
    description='Compute variability of the event log')
parser.add_argument('file', metavar='N', type=str, help='log file')
args = parser.parse_args()


def compute_variant_variability(log):
    '''
    compute and return the number of variants
    '''
    variants = variants_filter.get_variants(log)
    return(len(variants))


def compute_edit_distance_variability(log):
    '''
    compute the average edit distance between traces
    '''
    pass


def compute_my_variability(log):
    '''
    compute a measure of variability defined by me
    '''
    pass


if __name__ == "__main__":

    log = xes_import_factory.apply(args.file)

    print("number of variants of the event log: " +
          str(compute_variant_variability(log)))
