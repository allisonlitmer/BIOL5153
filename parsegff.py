#! /usr/bin/env python3

#import the program argparse

import argparse

#cerate an ArgumentParser object ('parser') that will hold all the info necessary
#to parse the command line

parser = argparse.ArgumentParser(description = "generates a genome sequence and the features")

# add a positional argument

parser.add_argument("fasta", help="the name of the job" ,type=argparse.FileType("r"))
parser.add_argument("gff", help="the features of the genome",type=argparse.FileType("r"))

#parse the command line arguments so you can access parse arguments

args = parser.parse_args()

#genome = open(args.fasta, "r")
#features = open(args.gff, "r")

#reading line by line

for line in args.gff:
    #skip blanks

    #remove line breaks
    line = line.rstrip('\n')
    print(line)

#split based on tabs
#sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')

#fields = line.split('\t')
#print(fields[3], fields[4])

#extract the DNA seqeuence from the genome for this feature (corresponds to the coordinates in GFF)
substring = args.fasta[378929:379011]

#print the DNA sequence for this feature
print(substring)

#calculate GC content for this feature
length = len(substring)
nucG = substring.count('G')
nucC = substring.count('C')

GC = nucG + nucC

#frequency of GC

freq = GC/length
print(freq)
