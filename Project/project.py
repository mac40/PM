'''
PROCESS MINING
project for the process mining course at the university of Padua

Project 1: How much variable is my event log?

author: Marco Baggio
mat: 1179124
'''
import argparse

import editdistance
import numpy as np
from nltk import jaccard_distance as jd
from pm4py.algo.filtering.log.variants import variants_filter
from pm4py.objects.log.importer.xes import factory as xes_import_factory

parser = argparse.ArgumentParser(
    description='Compute variability of the event log')
parser.add_argument('file', metavar='--file', type=str,
                    help='relative path to thelog file')
args = parser.parse_args()


def compute_variant_variability(log):
    '''
    compute and return the number of variants
    input:
        log = xes log
    output:
        number of variants in the log
    '''
    return(len(variants_filter.get_variants(log)))


def compute_edit_distance_variability(log, n=100):
    '''
    compute the average edit distance between traces
    input:
        log = xes log
        n = number of traces to analyze
    output:
        average edit distance between traces of the log

    comment:
        for testing purposes, the number of traces to be analyzed
        has been reduced to 100 in order to reduce the computational
        timers and get a faster result
    '''
    distances = []
    for index, trace_one in enumerate(log[0:n]):
        for trace_two in log[index+1:n]:
            distance = editdistance.eval(str(trace_one.attributes),
                                         str(trace_two.attributes))
        distances.append(distance)

    return np.average(distances)


def compute_my_variability(log, n=100):
    '''
    compute a measure of variability defined by me
    ---Jaccard distance---
    input:
        log = xes log
        n = number of traces to analyze
    output:
        average Jaccard distance between traces of the log
    '''
    distances = []
    for index, trace_one in enumerate(log[0:n]):
        for trace_two in log[index+1:n]:
            distance = jd(set(str(trace_one.attributes)),
                          set(str(trace_two.attributes)))
        distances.append(distance)

    return np.average(distances)


if __name__ == "__main__":

    log = xes_import_factory.apply(args.file)

    print("number of traces in the event log:" + str(len(log)))

    print("Number of variants in the event log: {}"
          .format(compute_variant_variability(log)))

    n = input("Select the number of traces to analyze (default 100): ")

    if not n:
        n = 100

    print("Average edit distance between {} traces of the event log: {}"
          .format(n, compute_edit_distance_variability(log, n)))

    print("Average Jaccard distance between {} traces of the event log: {}"
          .format(n, compute_my_variability(log, n)))
