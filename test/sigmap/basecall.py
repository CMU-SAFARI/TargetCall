import os
import sys 
import time

datadir = sys.argv[1] # should point to the directory where the fast5 & reds dir exist
model_name = 'sigmap'

exedir = "../run_scripts/" # the path to HierarchyCall's test/run_scripts dir  
filtered_bonito_script_path = "../targetcall/run_bonito_params.py "

# File Paths
fast5_path = datadir + "fast5/"

# Covid
readids_dir_path = datadir + '/covid/' + model_name + '/readids/'
filtered_fastq_dir_path = datadir + '/covid/' + model_name + '/filtered-fastq/'

# RUN basecalling on reads that pass the filter
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: read_ids_path, OPT4: use_case
start_time = time.time()
os.system("python " + filtered_bonito_script_path + fast5_path + " " + filtered_fastq_dir_path + ' ' + readids_dir_path + ' covid')
end_time = time.time()
print("COVID basecalling after sigmap execution time: %s seconds " % (end_time - start_time))

# Viral
readids_dir_path = datadir + '/viral/' + model_name + '/readids/'
filtered_fastq_dir_path = datadir + '/viral/' + model_name + '/filtered-fastq/'

# RUN basecalling on reads that pass the filter
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: read_ids_path, OPT4: use_case
start_time = time.time()
os.system("python " + filtered_bonito_script_path + fast5_path + " " + filtered_fastq_dir_path + ' ' + readids_dir_path + ' viral')
end_time = time.time()
print("VIRAL basecalling after sigmap execution time: %s seconds " % (end_time - start_time))


# Sepsis-chm13
readids_dir_path = datadir + '/sepsis-chm13/' + model_name + '/readids/'
filtered_fastq_dir_path = datadir + '/sepsis-chm13/' + model_name + '/filtered-fastq/'

start_time = time.time()
os.system("python " + filtered_bonito_script_path + fast5_path + " " + filtered_fastq_dir_path + ' ' + readids_dir_path + ' sepsis')
end_time = time.time()
print("SEPSIS-chm13 basecalling after filter execution time: %s seconds " % (end_time - start_time))


# Sepsis-hh38
readids_dir_path = datadir + '/sepsis-hg38/' + model_name + '/readids/'
filtered_fastq_dir_path = datadir + '/sepsis-hg38/' + model_name + '/filtered-fastq/'

start_time = time.time()
os.system("python " + filtered_bonito_script_path + fast5_path + " " + filtered_fastq_dir_path + ' ' + readids_dir_path + ' sepsis')
end_time = time.time()
print("SEPSIS-hg38 basecalling after filter execution time: %s seconds " % (end_time - start_time))
