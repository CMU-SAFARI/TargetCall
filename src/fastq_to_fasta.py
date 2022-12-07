import os
import sys

fastq_path = sys.argv[1]
fasta_path = sys.argv[2]

fastq_file = open(fastq_path)
fasta_file = open(fasta_path, 'w')

for idx, line in enumerate(fastq_file):
    if idx % 4 == 0 or idx % 4 == 1:
        line = line.strip()
        fasta_file.write(line + '\n')

os.system("rm " + fastq_path)
