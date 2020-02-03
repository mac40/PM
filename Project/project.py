'''
PROCESS MINING
project for the process mining course at the university of Padua

Project 1: How much variable is my event log?

author: Marco Baggio
mat: 1179124
'''
import argparse
import time

import numpy as np
from nltk import edit_distance as ed
from nltk import jaccard_distance as jd
from pm4py.algo.filtering.log.variants import variants_filter
from pm4py.objects.log.importer.xes import factory as xes_import_factory
from progress.bar import Bar

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
    '''

    # we first refactor every trace as a "space separated"
    # string of events in order to reduce the workload
    # of the pairwise comparison
    with Bar('Preprocessing', max=n) as bar:
        traces = []
        for trace in log[0:n]:
            events = []
            for event in trace:
                events.append(event["concept:name"])
            events = ' '.join(events)
            traces.append(events)
            bar.next()

    # we then proceed to calculate the pairwise distance
    # between each pair of traces
    with Bar('Edit dist', max=(n*(n-1)/2), suffix='%(percent)d%%') as bar:
        distances = []
        for index, trace_one in enumerate(traces):
            for trace_two in traces[index+1:]:
                distances.append(ed(trace_one, trace_two))
                bar.next()

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

    # As before we first refactor every trace as a list of events
    # in order to reduce the workload of the pairwise comparison
    with Bar('Preprocessing', max=n) as bar:
        traces = []
        for trace in log[0:n]:
            events = []
            for event in trace:
                events.append(event["concept:name"])
            traces.append(events)
            bar.next()

    # we then proceed to calculate the pairwise distance
    # between each pair of traces
    with Bar('Jaccard dist', max=(n*(n-1)/2), suffix='%(percent)d%%') as bar:
        distances = []
        for index, trace_one in enumerate(traces):
            for trace_two in traces[index+1:]:
                distances.append(jd(set(trace_one), set(trace_two)))
                bar.next()

    return np.average(distances)


if __name__ == "__main__":

    log = xes_import_factory.apply(args.file)

    print("number of traces in the event log:" + str(len(log)))

    start = time.time()
    print("Number of variants in the event log: {}"
          .format(compute_variant_variability(log)))
    print("Execution time = {}s".format(time.time()-start))

    n = input("Select the number of traces to analyze (default 5): ")

    # for testing purposes, the number of traces to be analyzed
    # has been reduced by default to 5 in order to reduce the computational
    # time and get a faster result
    if not n or n == "1":
        if n == "1":
            print("minimum traces required = 2")
        print("number of traces set to 5 by default")
        n = 5
    n = int(n)

    start = time.time()
    print("EDIT DISTANCE:")
    print("Average edit distance between {} traces of the event log: {}"
          .format(n, compute_edit_distance_variability(log, n)))
    print("Execution time = {}s".format(time.time()-start))

    start = time.time()
    print("JACCARD DISTANCE:")
    print("Average Jaccard distance between {} traces of the event log: {}"
          .format(n, compute_my_variability(log, n)))
    print("Execution time = {}s".format(time.time()-start))
