import os
import sys 

fastq_dir_path = sys.argv[1]

dir_list = os.listdir(fastq_dir_path)

# options: sam_file_path, readids_file_path, use_case
for dir in dir_list:
    test = dir.strip().split(".")
    print("\npython ../utils/fastq_to_fasta.py " + fastq_dir_path + dir + " " + fastq_dir_path + test[0] + ".fasta ")
    os.system("python ../utils/fastq_to_fasta.py " + fastq_dir_path + dir + " " + fastq_dir_path + test[0] + ".fasta ")
