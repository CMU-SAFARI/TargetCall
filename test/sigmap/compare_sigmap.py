import os
import sys 
import time

datadir = sys.argv[1] # should point to the directory where the fast5 & reds dir exist
sigmap_exe = sys.argv[2]
model_name = 'sigmap'

# Python Script Paths
exedir = "../run_scripts/" # the path to HierarchyCall's test/run_scripts dir  
sigmap_script_path = "run_sigmap.py "
filtered_bonito_script_path = exedir + "run_bonito_params.py "
extract_read_ids_path = exedir + "run_extract_filtered.py "

# Reference Genome Paths
covid_ref_path = datadir + "refs/Severe_acute_respiratory_syndrome_coronavirus_2_isolate_Wuhan-Hu-1.fasta "
combined_viral_path = datadir + "refs/combined_viral.fasta "
covid_index_path = datadir + "refs/sigmap_indices/covid"
combined_viral_index_path = datadir + "refs/sigmap_indices/combined_viral"

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

# RUN Sigmap
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: ref_path, OPT4: index_dir, OPT5: sigmap_exe_path 
start_time = time.time()
os.system("python " + sigmap_script_path + human_fast5_path + " " + sam_dir_path + "human_" + ' ' +  covid_ref_path + ' ' + covid_index_path + ' ' + sigmap_exe)
end_time = time.time()
print("COVID Human Sigmap execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + sigmap_script_path + covid_fast5_path + " " + sam_dir_path + "covid_" + ' ' +  covid_ref_path + ' ' + covid_index_path + ' ' + sigmap_exe)
end_time = time.time()
print("COVID Covid Sigmap execution time: %s seconds " % (end_time - start_time))

# RUN extract filtered reads 
start_time = time.time()
os.system("python " + extract_read_ids_path + sam_dir_path + " " + readids_dir_path + " covid")
end_time = time.time()
print("COVID dataset extract read ids execution time: %s seconds " % (end_time - start_time))

# RUN basecalling on reads that pass the filter
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: read_ids_path, OPT4: use_case
start_time = time.time()
os.system("python " + filtered_bonito_script_path + fast5_path + " " + filtered_fastq_dir_path + ' ' + readids_dir_path + ' covid')
end_time = time.time()
print("COVID basecalling after sigmap execution time: %s seconds " % (end_time - start_time))




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

# RUN BaseConv
# OPT1: read_dir_path, OPT2: output_dir_path, OPT3: model_name
start_time = time.time()
os.system("python " + sigmap_script_path + metagenomics_bacteria_fast5_path + " " + sam_dir_path + "bacteria_" + ' ' +  combined_viral_path + ' ' + combined_viral_index_path + ' ' + sigmap_exe)
end_time = time.time()
print("VIRAL bacteria Sigmap execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + sigmap_script_path + simulated_virus_fast5_path + " " + sam_dir_path + "virus_" + ' ' +  combined_viral_path + ' ' + combined_viral_index_path + ' ' + sigmap_exe)
end_time = time.time()
print("VIRAL virus Sigmap execution time: %s seconds " % (end_time - start_time))

# RUN extract filtered reads 
start_time = time.time()
os.system("python " + extract_read_ids_path + sam_dir_path + " " + readids_dir_path + " viral")
end_time = time.time()
print("VIRAL dataset extract read ids execution time: %s seconds " % (end_time - start_time))

# RUN basecalling on reads that pass the filter
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: read_ids_path, OPT4: use_case
start_time = time.time()
os.system("python " + filtered_bonito_script_path + fast5_path + " " + filtered_fastq_dir_path + ' ' + readids_dir_path + ' viral')
end_time = time.time()
print("VIRAL basecalling after sigmap execution time: %s seconds " % (end_time - start_time))
