#!/usr/bin/env python

# get core genes from groups.txt produced by orthoMCL
# core genes occur in all genomes only once

import argparse


parser = argparse.ArgumentParser("get core genes from groups.txt")

parser.add_argument("groups_file", type = argparse.FileType("r"),
        nargs = 1, help = "the groups.txt file produced by orthoMCL")
parser.add_argument("--output", "-o", type = argparse.FileType("w"),
        nargs = 1, help = "a name for the output file")

args = parser.parse_args()


def readGroups(file_name):
    """ create a dict of cluster and proteins present
    also get unique genome names using a set """
    groups_dict = {}
    genome_set = set()
    for line in file_name[0]:
        line = line.strip()
        cols = line.split(":")
        cluster = cols[0]
        proteins = cols[1].strip().split(" ")
        groups_dict[cluster] = proteins
        # now get unique genome names from the protein name
        for protein in proteins:
            genome_set.add(protein.split("|")[0])
    return groups_dict, genome_set

def getCore(groups_dict, genome_names):
    core_clusters = []
    genome_names = list(genome_names)
    for cluster in groups_dict:
        # create a list of proteins in cluster to check against all genomes
        protein_list = []
        for protein in groups_dict[cluster]:
            protein_list.append(protein.split("|")[0])
        # check if the cluster contains proteins from all genomes only once (no dups)
        if sorted(protein_list) == sorted(genome_names):
            args.output[0].write(cluster + "\t" + "\t".join(groups_dict[cluster]) + "\n")

groups_dict, genome_names = readGroups(args.groups_file)
core_clusters = getCore(groups_dict, genome_names)
