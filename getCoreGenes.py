#!/usr/bin/env python

# get core genes from groups.txt produced by orthoMCL
# core genes occur in all genomes only once

import argparse


parser = argparse.ArgumentParser("get core genes from groups.txt")

parser.add_argument("groups_file", type = argparse.FileType("r"),
        nargs = 1, help = "the groups.txt file produced by orthoMCL")

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
    for cluster in groups_dict:
        if len(groups_dict[cluster]) == len(genome_names):
            print cluster

groups_dict, genome_names = readGroups(args.groups_file)
core_clusters = getCore(groups_dict, genome_names)

