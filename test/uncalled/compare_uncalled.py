import os
import sys 
import time

datadir = sys.argv[1] # should point to the directory where the fast5 & reds dir exist
uncalled_exe = sys.argv[2]
model_name = 'uncalled'

# Python Script Paths
exedir = "../run_scripts/" # the path to HierarchyCall's test/run_scripts dir  
uncalled_script_path = "run_uncalled.py "
extract_read_ids_path = exedir + "run_extract_filtered.py "

# Reference Genome Paths
covid_index_path = datadir + "refs/uncalled_indices/covid"
combined_viral_index_path = datadir + "refs/uncalled_indices/combined_viral"
chm13_index_path = datadir + "refs/uncalled_indices/human_chm13"

# File Paths
fast5_path = datadir + "fast5/"
human_fast5_path = datadir + "fast5/human/"
covid_fast5_path = datadir + "fast5/virus/real/"

sam_dir_path = datadir + '/covid/' + model_name + '/sam/'
os.system("mkdir -p " + sam_dir_path)
readids_dir_path = datadir + '/covid/' + model_name + '/readids/'
os.system("mkdir -p " + readids_dir_path)
filtered_fastq_dir_path = datadir + '/covid/' + model_name + '/filtered-fastq/'
os.system("mkdir -p " + filtered_fastq_dir_path)

# RUN UNCALLED
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: index_dir, OPT4: uncalled_exe_path 
start_time = time.time()
os.system("python " + uncalled_script_path + human_fast5_path + " " + sam_dir_path + "human_" + ' ' + covid_index_path + ' ' + uncalled_exe)
end_time = time.time()
print("COVID Human UNCALLED execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + uncalled_script_path + covid_fast5_path + " " + sam_dir_path + "covid_" + ' ' + covid_index_path + ' ' + uncalled_exe)
end_time = time.time()
print("COVID Covid UNCALLED execution time: %s seconds " % (end_time - start_time))

# RUN extract filtered reads 
start_time = time.time()
os.system("python " + extract_read_ids_path + sam_dir_path + " " + readids_dir_path + " covid")
end_time = time.time()
print("COVID dataset extract read ids execution time: %s seconds " % (end_time - start_time))


# File Paths
fast5_path = datadir + "fast5/"
metagenomics_bacteria_fast5_path = datadir + "fast5/metagenomics-bacteria/"
simulated_virus_fast5_path = datadir + "fast5/virus/simulated/"

sam_dir_path = datadir + '/viral/' + model_name + '/sam/'
os.system("mkdir -p " + sam_dir_path)
readids_dir_path = datadir + '/viral/' + model_name + '/readids/'
os.system("mkdir -p " + readids_dir_path)
filtered_fastq_dir_path = datadir + '/viral/' + model_name + '/filtered-fastq/'
os.system("mkdir -p " + filtered_fastq_dir_path)

# RUN UNCALLED
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: index_dir, OPT4: uncalled_exe_path 
start_time = time.time()
os.system("python " + uncalled_script_path + metagenomics_bacteria_fast5_path + " " + sam_dir_path + "bacteria_" + ' ' + combined_viral_index_path + ' ' + uncalled_exe)
end_time = time.time()
print("VIRAL bacteria UNCALLED execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + uncalled_script_path + simulated_virus_fast5_path + " " + sam_dir_path + "virus_" + ' ' + combined_viral_index_path + ' ' + uncalled_exe)
end_time = time.time()
print("VIRAL virus UNCALLED execution time: %s seconds " % (end_time - start_time))

# RUN extract filtered reads 
start_time = time.time()
os.system("python " + extract_read_ids_path + sam_dir_path + " " + readids_dir_path + " viral")
end_time = time.time()
print("VIRAL dataset extract read ids execution time: %s seconds " % (end_time - start_time))

# File Paths
fast5_path = datadir + "fast5/"
human_fast5_path = datadir + "fast5/human/"
sepsis_fast5_path = datadir + "fast5/sepsis-bacteria/"

sam_dir_path = datadir + '/sepsis-chm13/' + model_name + '/sam/'
os.system("mkdir -p " + sam_dir_path)
readids_dir_path = datadir + '/sepsis-chm13/' + model_name + '/readids/'
os.system("mkdir -p " + readids_dir_path)
filtered_fastq_dir_path = datadir + '/sepsis-chm13/' + model_name + '/filtered-fastq/'
os.system("mkdir -p " + filtered_fastq_dir_path)

# RUN UNCALLED
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: index_dir, OPT4: uncalled_exe_path 
start_time = time.time()
os.system("python " + uncalled_script_path + human_fast5_path + " " + sam_dir_path + "human_" + ' ' + chm13_index_path + ' ' + uncalled_exe)
end_time = time.time()
print("SEPSIS-chm13 Human UNCALLED execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + uncalled_script_path + sepsis_fast5_path + " " + sam_dir_path + "bacteria_" + ' ' + chm13_index_path + ' ' + uncalled_exe)
end_time = time.time()
print("SEPSIS-chm13 sepsis UNCALLED execution time: %s seconds " % (end_time - start_time))

# RUN extract filtered reads 
start_time = time.time()
os.system("python " + extract_read_ids_path + sam_dir_path + " " + readids_dir_path + " sepsis")
end_time = time.time()
print("SEPSIS-chm13 dataset extract read ids execution time: %s seconds " % (end_time - start_time))
