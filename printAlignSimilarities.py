#!/usr/bin/env python

# get percent similarity between core alignments

import sys
from Bio import AlignIO

align_file = AlignIO.read(sys.argv[1], "fasta")

def findDiffs(first, second):
    A=list(first)
    B=list(second)
    count=0
    gaps=0
    for n in range(0, len(A)):
        if A[n]==B[n]:
            if A[n]!="-":
                count=count+1
            else:
                gaps=gaps+1

    return 100*(count/float((len(A)-gaps)))

def allVsAll(align):
    for first in align:
        print "\n"
        for second in align:
            print first.name, "\t", second.name, "\t", findDiffs(first, second)

allVsAll(align_file)
