#! /usr/bin/env python3

#import the program argparse

import argparse
import Bio
import csv
from Bio import SeqIO

#cerate an ArgumentParser object ('parser') that will hold all the info necessary
#to parse the command line
def get_args():
    parser = argparse.ArgumentParser(description = "generates a genome sequence and the features")

# add a positional argument

    parser.add_argument("fasta", help="the genome sequence")
    parser.add_argument("gff", help="the features of the genome")
    
#parse the command line arguments so you can access parse arguments

    return parser.parse_args()

    genome = open(args.fasta, "r")
    features = open(args.gff, "r")

#use csv reader to parse gff file, use seqIO to parse fasta file, replace line by line code with the csv reader and get GC content
def csv():
    with open('watermelon.gff', 'r') as gff:

        csvreader = csv.reader(gff, delimiter='\t')
        fields = csvreader.rstrip('\n')

        for line in fields:
            if not line:
                continue
            else:
                pass
        for line_gff in features:
            line_gff = line_gff.rstrip('\n')
            fields = line.split('\t')
    #skip blanks
    #remove line breaks
    #print(line_gff)

#Parse the FASTA File using Biopython
def parse_fasta():
    
    for seqrecord in SeqIO.parse("watermelon.fsa", "fasta"):
        print("Description: " + seqrecord.description)
        print(len(seqrecord.seq))
    #print(seqrecord.seq)
    
#read file line by line starting at second line
#using the line counter we get it to start at line 2
def lines_fasta():
    line_counter = 1
    for lines_fasta in genome:
        if line_counter == 2:
            sequence = lines_fasta.rstrip('\n')
        #print(sequence)
        line_counter += 1

#if then statement to calculate reverse compliment 
def reverse():
    strand_type = gff[8]
    if strand_type == "-" :
        sequence.reverse_complement
    else:
        pass

#extract the DNA seqeuence from the genome for this feature (corresponds to the coordinates in GFF)    
def gc_content():
#print DNA sequences

    for lines in fields:
        start = (int(fields[3]) + 1)
        stop = (int(fields[4]) + 1)
        seqs = sequence[start:stop]
        print(seqs)

#calculate GC content for this feature
    length = len(seqs)
    nucG = seqs.count('G')
    nucC = seqs.count('C')

    GC = nucG + nucC

#frequency of GC

    freq = GC/length
    return(freq)

def main():

    args = get_args()

    #execute the program by calling main
if __name__ == "__main__":
    main()
