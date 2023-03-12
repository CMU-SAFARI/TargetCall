import os
import sys 
import time

datadir = sys.argv[1] # should point to the directory where the fast5 & reds dir exist
sigmap_exe = sys.argv[2]
model_name = 'sigmap'

# Python Script Paths
exedir = "../run_scripts/" # the path to HierarchyCall's test/run_scripts dir  
sigmap_script_path = "run_sigmap.py "
extract_read_ids_path = exedir + "run_extract_filtered.py "

# Reference Genome Paths
human_path = datadir + "refs/chm13.fasta "
human_index_path = datadir + "refs/sigmap_indices/chm13_human"

# File Paths
fast5_path = datadir + "fast5/"
human_fast5_path = datadir + "fast5/human/"
covid_fast5_path = datadir + "fast5/sepsis-bacteria/"

sam_dir_path = datadir + '/sepsis-chm13/' + model_name + '/sam/'
os.system("mkdir -p " + sam_dir_path)
readids_dir_path = datadir + '/sepsis-chm13/' + model_name + '/readids/'
os.system("mkdir -p " + readids_dir_path)
filtered_fastq_dir_path = datadir + '/sepsis-chm13/' + model_name + '/filtered-fastq/'
os.system("mkdir -p " + filtered_fastq_dir_path)

# RUN Sigmap
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: ref_path, OPT4: index_dir, OPT5: sigmap_exe_path 
start_time = time.time()
os.system("python " + sigmap_script_path + human_fast5_path + " " + sam_dir_path + "human_" + ' ' +  human_path + ' ' + human_index_path + ' ' + sigmap_exe)
end_time = time.time()
print("SEPSIS-chm13 Human Sigmap execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + sigmap_script_path + covid_fast5_path + " " + sam_dir_path + "bacteria_" + ' ' +  human_path + ' ' + human_index_path + ' ' + sigmap_exe)
end_time = time.time()
print("SEPSIS-chm13 bacteria Sigmap execution time: %s seconds " % (end_time - start_time))

# RUN extract filtered reads 
start_time = time.time()
os.system("python " + extract_read_ids_path + sam_dir_path + " " + readids_dir_path + " sepsis")
end_time = time.time()
print("SEPSIS-chm13 dataset extract read ids execution time: %s seconds " % (end_time - start_time))

