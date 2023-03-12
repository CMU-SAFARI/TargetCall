import os
import sys 
import time

model_name = sys.argv[1]
datadir = sys.argv[2] # should point to the directory where the fast5 & reds dir exist


print("Model Name: " + model_name)

# Python Script Paths
exedir = "../run_scripts/" # the path to HierarchyCall's test/run_scripts dir  
bonito_script_path = "./run_bonito.py "
filtered_bonito_script_path = "./run_bonito_params.py "
minimap_script_path = exedir + "run_minimap.py "
extract_read_ids_path = exedir + "run_extract_filtered.py "
convert_script_path = exedir + "run_convert.py "

# Reference Genome Paths
covid_ref_path = datadir + "refs/Severe_acute_respiratory_syndrome_coronavirus_2_isolate_Wuhan-Hu-1.mmi"
combined_viral_path = datadir + "refs/combined_viral.mmi"
human_ref_path = datadir + "refs/human.mmi"
human_chm13_ref_path = datadir + "refs/chm13.mmi"

# File Paths
fast5_path = datadir + "fast5/"
human_fast5_path = datadir + "fast5/human/"
covid_fast5_path = datadir + "fast5/virus/real/"

fastq_dir_path = datadir + '/covid/' + model_name + '/fastq/'
os.system("mkdir -p " + fastq_dir_path)
sam_dir_path = datadir + '/covid/' + model_name + '/sam/'
os.system("mkdir -p " + sam_dir_path)
readids_dir_path = datadir + '/covid/' + model_name + '/readids/'
os.system("mkdir -p " + readids_dir_path)
filtered_fastq_dir_path = datadir + '/covid/' + model_name + '/filtered-fastq/'
os.system("mkdir -p " + filtered_fastq_dir_path)

# RUN LightCall
# OPT1: read_dir_path, OPT2: output_dir_path, OPT3: model_name
start_time = time.time()
os.system("python " + bonito_script_path + human_fast5_path + " " + fastq_dir_path + "human_" + ' ' +  model_name)
end_time = time.time()
print("COVID Human LightCall execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + bonito_script_path + covid_fast5_path + " " + fastq_dir_path + "covid_" + ' ' +  model_name)
end_time = time.time()
print("COVID Covid LightCall execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + convert_script_path + fastq_dir_path)
end_time = time.time()
print("COVID dataset fastq to fasta execution time: %s seconds " % (end_time - start_time))

# RUN SimCheck
# OPT1: ref_path, OPT2: fasta_dir_path, OPT3: sam_dir_path
start_time = time.time()
os.system("python " + minimap_script_path + covid_ref_path + " " + fastq_dir_path + " " + sam_dir_path)
end_time = time.time()
print("COVID dataset SimCheck execution time: %s seconds " % (end_time - start_time))

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
print("COVID basecalling after filter execution time: %s seconds " % (end_time - start_time))








# File Paths
fast5_path = datadir + "fast5/"
metagenomics_bacteria_fast5_path = datadir + "fast5/metagenomics-bacteria/"
simulated_virus_fast5_path = datadir + "fast5/virus/simulated/"

fastq_dir_path = datadir + '/viral/' + model_name + '/fastq/'
os.system("mkdir -p " + fastq_dir_path)
sam_dir_path = datadir + '/viral/' + model_name + '/sam/'
os.system("mkdir -p " + sam_dir_path)
readids_dir_path = datadir + '/viral/' + model_name + '/readids/'
os.system("mkdir -p " + readids_dir_path)
filtered_fastq_dir_path = datadir + '/viral/' + model_name + '/filtered-fastq/'
os.system("mkdir -p " + filtered_fastq_dir_path)

# RUN LightCall
# OPT1: read_dir_path, OPT2: output_dir_path, OPT3: model_name
start_time = time.time()
os.system("python " + bonito_script_path + metagenomics_bacteria_fast5_path + " " + fastq_dir_path + "bacteria_" + ' ' +  model_name)
end_time = time.time()
print("VIRAL bacteria LightCall execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + bonito_script_path + simulated_virus_fast5_path + " " + fastq_dir_path + "virus_" + ' ' +  model_name)
end_time = time.time()
print("VIRAL virus LightCall execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + convert_script_path + fastq_dir_path)
end_time = time.time()
print("VIRAL dataset fastq to fasta execution time: %s seconds " % (end_time - start_time))

# RUN SimCheck
# OPT1: ref_path, OPT2: fasta_dir_path, OPT3: sam_dir_path
start_time = time.time()
os.system("python " + minimap_script_path + combined_viral_path + " " + fastq_dir_path + " " + sam_dir_path)
end_time = time.time()
print("VIRAL dataset SimCheck execution time: %s seconds " % (end_time - start_time))

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
print("VIRAL basecalling after filter execution time: %s seconds " % (end_time - start_time))




# Sepsis with hg38
# File Paths
fast5_path = datadir + "fast5/"
human_fast5_path = datadir + "fast5/human/"
sepsis_bacteria_fast5_path = datadir + "fast5/sepsis-bacteria/"


fastq_dir_path = datadir + '/sepsis-hg38/' + model_name + '/fastq/'
os.system("mkdir -p " + fastq_dir_path)
sam_dir_path = datadir + '/sepsis-hg38/' + model_name + '/sam/'
os.system("mkdir -p " + sam_dir_path)
readids_dir_path = datadir + '/sepsis-hg38/' + model_name + '/readids/'
os.system("mkdir -p " + readids_dir_path)
filtered_fastq_dir_path = datadir + '/sepsis-hg38/' + model_name + '/filtered-fastq/'
os.system("mkdir -p " + filtered_fastq_dir_path)

# RUN LightCall
# OPT1: read_dir_path, OPT2: output_dir_path, OPT3: model_name
start_time = time.time()
os.system("python " + bonito_script_path + sepsis_bacteria_fast5_path + " " + fastq_dir_path + "bacteria_" + ' ' +  model_name)
end_time = time.time()
print("SEPSIS-hg38 Sepsis-bacteria LightCall execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + convert_script_path + fastq_dir_path)
end_time = time.time()
print("SEPSIS-hg38 dataset fastq to fasta execution time: %s seconds " % (end_time - start_time))

old_fastq_dir_path = datadir + '/covid/' + model_name + '/fastq/'
os.system("cp -r " + old_fastq_dir_path + 'human_* ' + fastq_dir_path)

# RUN SimCheck
# OPT1: ref_path, OPT2: fasta_dir_path, OPT3: sam_dir_path
start_time = time.time()
os.system("python " + minimap_script_path + human_ref_path + " " + fastq_dir_path + " " + sam_dir_path)
end_time = time.time()
print("SEPSIS-hg38 dataset SimCheck execution time: %s seconds " % (end_time - start_time))

# RUN extract filtered reads 
start_time = time.time()
os.system("python " + extract_read_ids_path + sam_dir_path + " " + readids_dir_path + " sepsis")
end_time = time.time()
print("SEPSIS-hg38 dataset extract read ids execution time: %s seconds " % (end_time - start_time))

# RUN basecalling on reads that pass the filter
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: read_ids_path, OPT4: use_case
start_time = time.time()
os.system("python " + filtered_bonito_script_path + fast5_path + " " + filtered_fastq_dir_path + ' ' + readids_dir_path + ' sepsis')
end_time = time.time()
print("SEPSIS-hg38 basecalling after filter execution time: %s seconds " % (end_time - start_time))


# File Paths
fast5_path = datadir + "fast5/"
human_fast5_path = datadir + "fast5/human/"
sepsis_bacteria_fast5_path = datadir + "fast5/sepsis-bacteria/"


fastq_dir_path = datadir + '/sepsis-chm13/' + model_name + '/fastq/'
os.system("mkdir -p " + fastq_dir_path)
sam_dir_path = datadir + '/sepsis-chm13/' + model_name + '/sam/'
os.system("mkdir -p " + sam_dir_path)
readids_dir_path = datadir + '/sepsis-chm13/' + model_name + '/readids/'
os.system("mkdir -p " + readids_dir_path)
filtered_fastq_dir_path = datadir + '/sepsis-chm13/' + model_name + '/filtered-fastq/'
os.system("mkdir -p " + filtered_fastq_dir_path)

# RUN LightCall
# OPT1: read_dir_path, OPT2: output_dir_path, OPT3: model_name

old_fastq_dir_path = datadir + '/sepsis-hg38/' + model_name + '/fastq/'
os.system("cp -r " + old_fastq_dir_path + '/* ' + fastq_dir_path)

# RUN SimCheck
# OPT1: ref_path, OPT2: fasta_dir_path, OPT3: sam_dir_path
start_time = time.time()
os.system("python " + minimap_script_path + human_chm13_ref_path + " " + fastq_dir_path + " " + sam_dir_path)
end_time = time.time()
print("SEPSIS-chm13 dataset SimCheck execution time: %s seconds " % (end_time - start_time))

# RUN extract filtered reads 
start_time = time.time()
os.system("python " + extract_read_ids_path + sam_dir_path + " " + readids_dir_path + " sepsis")
end_time = time.time()
print("SEPSIS-chm13 dataset extract read ids execution time: %s seconds " % (end_time - start_time))

# RUN basecalling on reads that pass the filter
# OPT1: fast5_dir_path, OPT2: output_dir_path, OPT3: read_ids_path, OPT4: use_case
start_time = time.time()
os.system("python " + filtered_bonito_script_path + fast5_path + " " + filtered_fastq_dir_path + ' ' + readids_dir_path + ' sepsis')
end_time = time.time()
print("SEPSIS-chm13 basecalling after filter execution time: %s seconds " % (end_time - start_time))
