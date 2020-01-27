'''
PROCESS MINING
project for the process mining course at the university of Padua

Project 1: How much variable is my event log?

author: Marco Baggio
mat: 1179124
'''
import argparse

import numpy as np
from nltk import jaccard_distance as jd
from nltk import edit_distance as ed
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
    with Bar('Edit distance', max=n*(n-1)/2, suffix='%(percent)d%%') as bar:
        distances = []
        for index, trace_one in enumerate(log[0:n]):
            events_one = []
            for event in trace_one:
                events_one.append(event["concept:name"])
            events_one = ' '.join(events_one)
            for trace_two in log[index+1:n]:
                events_two = []
                for event in trace_two:
                    events_two.append(event["concept:name"])
                events_two = ' '.join(events_two)
                distances.append(ed(events_one, events_two))
                bar.next()

    return np.average(distances)


def compute_my_variability(log, n=100, suffix='%(percent)d%%'):
    '''
    compute a measure of variability defined by me
    ---Jaccard distance---
    input:
        log = xes log
        n = number of traces to analyze
    output:
        average Jaccard distance between traces of the log
    '''
    with Bar('Jaccard distance', max=n*(n-1)/2) as bar:
        distances = []
        for index, trace_one in enumerate(log[0:n]):
            events_one = []
            for event in trace_one:
                events_one.append(event["concept:name"])
            for trace_two in log[index+1:n]:
                events_two = []
                for event in trace_two:
                    events_two.append(event["concept:name"])
                distances.append(jd(set(events_one), set(events_two)))
                bar.next()

    return np.average(distances)


if __name__ == "__main__":

    log = xes_import_factory.apply(args.file)

    print("number of traces in the event log:" + str(len(log)))

    print("Number of variants in the event log: {}"
          .format(compute_variant_variability(log)))

    n = input("Select the number of traces to analyze (default 5): ")

    '''
    for testing purposes, the number of traces to be analyzed
    has been reduced by default to 5 in order to reduce the computational
    time and get a faster result
    '''
    if not n or n == "1":
        if n == "1":
            print("minimum traces required = 2")
        print("number of traces set to 5 by default")
        n = 5
    n = int(n)

    print("Average edit distance between {} traces of the event log: {}"
          .format(n, compute_edit_distance_variability(log, n)))

    print("Average Jaccard distance between {} traces of the event log: {}"
          .format(n, compute_my_variability(log, n)))
