#!/usr/bin/env python

# get core genes from groups.txt produced by orthoMCL
# core genes occur in all genomes only once

import argparse


parser = argparse.ArgumentParser("get core genes from groups.txt")

parser.add_argument("groups.txt file", type = argparse.FileType("r"),
        nargs = 1, help = "the groups.txt file produced by orthoMCL")

args = parser.parse_args()



