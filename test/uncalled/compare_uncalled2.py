import os
import sys 
import time

datadir = sys.argv[1] # should point to the directory where the fast5 & reds dir exist
model_name = 'uncalled'

# Python Script Paths
exedir = "../run_scripts/" # the path to HierarchyCall's test/run_scripts dir  
filtered_bonito_script_path = exedir + "run_bonito_params.py "

# File Paths
fast5_path = datadir + "fast5/"
human_fast5_path = datadir + "fast5/human/"
covid_fast5_path = datadir + "fast5/virus/real/"

sam_dir_path = datadir + '/covid/' + model_name + '/sam/'
readids_dir_path = datadir + '/covid/' + model_name + '/readids/'
filtered_fastq_dir_path = datadir + '/covid/' + model_name + '/filtered-fastq/'

# RUN basecalling on reads that pass the filter
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: read_ids_path, OPT4: use_case
start_time = time.time()
os.system("python " + filtered_bonito_script_path + fast5_path + " " + filtered_fastq_dir_path + ' ' + readids_dir_path + ' covid')
end_time = time.time()
print("COVID basecalling after UNCALLED execution time: %s seconds " % (end_time - start_time))


# File Paths
fast5_path = datadir + "fast5/"
metagenomics_bacteria_fast5_path = datadir + "fast5/metagenomics-bacteria/"
simulated_virus_fast5_path = datadir + "fast5/virus/simulated/"

sam_dir_path = datadir + '/viral/' + model_name + '/sam/'
readids_dir_path = datadir + '/viral/' + model_name + '/readids/'
filtered_fastq_dir_path = datadir + '/viral/' + model_name + '/filtered-fastq/'


# RUN basecalling on reads that pass the filter
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: read_ids_path, OPT4: use_case
start_time = time.time()
os.system("python " + filtered_bonito_script_path + fast5_path + " " + filtered_fastq_dir_path + ' ' + readids_dir_path + ' viral')
end_time = time.time()
print("VIRAL basecalling after UNCALLED execution time: %s seconds " % (end_time - start_time))
