#! /usr/bin/env python3

#import the program argparse

import argparse
import Bio
import csv

#cerate an ArgumentParser object ('parser') that will hold all the info necessary
#to parse the command line

parser = argparse.ArgumentParser(description = "generates a genome sequence and the features")

# add a positional argument

parser.add_argument("fasta", help="the genome sequence")
parser.add_argument("gff", help="the features of the genome")

#parse the command line arguments so you can access parse arguments

args = parser.parse_args()

genome = open(args.fasta, "r")
features = open(args.gff, "r")

#use csv reader to parse gff file, use seqIO to parse fasta file, replace line by line code with the csv reader and get GC content

with open('watermelon.gff', 'r') as gff:
    csvreader = csv.reader(gff, delimiter='\t')

    for line in csvreader:
        if not line:
            continue
        else:
            feature_columns = (line[3], line[4])
            print(feature_columns)
            

for line_gff in features:
    line_gff = line_gff.rstrip('\n')
    #skip blanks
    #remove line breaks
    #print(line_gff)

#Parse the FASTA File using Biopython
from Bio import SeqIO
for seqrecord in SeqIO.parse("watermelon.fsa", "fasta"):
    print("Description: " + seqrecord.description)
    print(len(seqrecord.seq))
    #print(seqrecord.seq)
    
#read file line by line starting at second line
#using the line counter we get it to start at line 2
#solution 2 for reading starting at second line
line_counter = 1
for lines_fasta in genome:
    if line_counter == 2:
        sequence = lines_fasta.rstrip('\n')
        #print(sequence)
    line_counter += 1

#split based on tabs
#sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')


#extract the DNA seqeuence from the genome for this feature (corresponds to the coordinates in GFF)    

substring = sequence[378929:379011]

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

