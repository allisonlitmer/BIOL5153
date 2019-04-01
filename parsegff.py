
#!/bin/bash

#read the files in, open files

fasta = "watermelon.fsa"
fasta_file = open(fasta, "r")
genome = fasta_file.read()

filename = "watermelon.gff"
gff = open(filename, "r")


#reading line by line

for line in gff:
    #skip blanks

    #remove line breaks
    line = line.rstrip('\n')
    
#split based on tabs
#sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')

#fields = line.split('\t')
#print(fields[3], fields[4])

#extract the DNA seqeuence from the genome for this feature (corresponds to the coordinates in GFF)
substring = genome[378929:379011]


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