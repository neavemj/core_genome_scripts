#!/usr/bin/env python

# get percent similarity between core alignments
# alignment is normal file produced by muscle
## could turn this into a triangle comparison ##

import argparse
from Bio import AlignIO         # requires biopython


parser = argparse.ArgumentParser("print the percent similarity between all alignments in an alignment file")

parser.add_argument("--alignment_file", "-a", type = str,
        nargs = 1, help = "alignment file as produced by Muscle")

args = parser.parse_args()

align_file = AlignIO.read(args.alignment_file[0], "fasta")


def findDiffs(first, second):
    # this function does the base by base comparison
    A = list(first)
    B = list(second)
    count = 0
    gaps = 0
    for n in range(0, len(A)):
        if A[n] == B[n]:
            if A[n] != "-" and A[n] != " ":
                count += 1
            else:
                gaps += 1

    return (count / float((len(A) - gaps))) * 100

def allVsAll(align):
    # compare all alignments against all others (all-vs-all)
    for first in align:
        print "\n"
        for second in align:
            print first.name, "\t", second.name, "\t", findDiffs(first, second)

allVsAll(align_file)
