#!/usr/bin/env python

# extract protein sequences given a list of core genes
# input should the output from getCoreGenes.py

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser("get proteins given a list of core genes")

parser.add_argument("--core_file", "-c", type = argparse.FileType("r"),
        nargs = 1, help = "the core genes file from getCoreGenes.py")
parser.add_argument("--proteins", "-p", type = str,
        nargs = 1, help = "the goodProteins.fasta file from orthoMCL")

args = parser.parse_args()

def getCoreProteins(core_file, protein_dict):
    for line in core_file:
        line = line.strip()
        cols = line.split("\t")
        cluster = cols[0]
        output = open(cluster + ".faa", "w")
        for protein in cols[1:]:
            SeqIO.write(protein_dict[protein], output, "fasta")

protein_dict = SeqIO.index(args.proteins[0], "fasta")
core_file = args.core_file[0]
getCoreProteins(core_file, protein_dict)
