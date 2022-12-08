import os
import sys 
import time

datadir = sys.argv[1] # should point to the directory where the fast5 & reds dir exist

# Python Script Paths
exedir = "../run_scripts/" # the path to HierarchyCall's test/run_scripts dir  
bonito_script_path = exedir + "run_bonito.py "
minimap_script_path = exedir + "run_minimap.py "
convert_script_path = exedir + "run_convert.py "

# Reference Genome Paths
combined_viral_path = datadir + "refs/combined_viral.mmi"

# File Paths
metagenomics_bacteria_fast5_path = datadir + "fast5/metagenomics-bacteria/"
simulated_virus_fast5_path = datadir + "fast5/virus/simulated/"

fastq_dir_path = datadir + "/viral/default/fastq/"
os.system("mkdir -p " + fastq_dir_path)
sam_dir_path = datadir + "/viral/default/sam/"
os.system("mkdir -p " + sam_dir_path)

# OPT1: read_dir_path, OPT2: output_dir_path, OPT3: model_name
start_time = time.time()
os.system("python " + bonito_script_path + metagenomics_bacteria_fast5_path + " " + fastq_dir_path + "bacteria_" + ' default')
end_time = time.time()
print("VIRAL bacteria basecalling execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + bonito_script_path + simulated_virus_fast5_path + " " + fastq_dir_path + "virus_" + ' default')
end_time = time.time()
print("VIRAL virus basecalling execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + convert_script_path + fastq_dir_path)
end_time = time.time()
print("VIRAL dataset fastq to fasta execution time: %s seconds " % (end_time - start_time))

# Align to  reference genomes using minimap2
# OPT1: ref_path, OPT2: fasta_dir_path, OPT3: sam_dir_path
start_time = time.time()
os.system("python " + minimap_script_path + combined_viral_path + " " + fastq_dir_path + " " + sam_dir_path)
end_time = time.time()
print("VIRAL dataset minimap2 after basecalling execution time: %s seconds " % (end_time - start_time))

# Reference Genome Paths
covid_ref_path = datadir + "refs/Severe_acute_respiratory_syndrome_coronavirus_2_isolate_Wuhan-Hu-1.mmi"

# File Paths
human_fast5_path = datadir + "fast5/human/"
covid_fast5_path = datadir + "fast5/virus/real/"

fastq_dir_path = datadir + "/covid/default/fastq/"
os.system("mkdir -p " + fastq_dir_path)
sam_dir_path = datadir + "/covid/default/sam/"
os.system("mkdir -p " + sam_dir_path)

# OPT1: read_dir_path, OPT2: output_dir_path, OPT3: model_name
start_time = time.time()
os.system("python " + bonito_script_path + human_fast5_path + " " + fastq_dir_path + "human_" + ' default')
end_time = time.time()
print("COVID Human basecalling execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + bonito_script_path + covid_fast5_path + " " + fastq_dir_path + "covid_" + ' default')
end_time = time.time()
print("COVID Covid basecalling execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + convert_script_path + fastq_dir_path)
end_time = time.time()
print("COVID dataset fastq to fasta execution time: %s seconds " % (end_time - start_time))

# Align to  reference genomes using minimap2
# OPT1: ref_path, OPT2: fasta_dir_path, OPT3: sam_dir_path
start_time = time.time()
os.system("python " + minimap_script_path + covid_ref_path + " " + fastq_dir_path + " " + sam_dir_path)
end_time = time.time()
print("COVID dataset minimap2 after basecalling execution time: %s seconds " % (end_time - start_time))

# Reference Genome Paths
human_ref_path = datadir + "refs/human.mmi"

# File Paths
human_fast5_path = datadir + "fast5/human/"
sepsis_bacteria_fast5_path = datadir + "fast5/sepsis-bacteria/"

fastq_dir_path = datadir + "/sepsis/default/fastq/"
os.system("mkdir -p " + fastq_dir_path)
sam_dir_path = datadir + "/sepsis/default/sam/"
os.system("mkdir -p " + sam_dir_path)

# OPT1: read_dir_path, OPT2: output_dir_path, OPT3: model_name
start_time = time.time()
os.system("python " + bonito_script_path + sepsis_bacteria_fast5_path + " " + fastq_dir_path + "bacteria_" + ' default')
end_time = time.time()
print("SEPSIS Sepsis-bacteria basecalling execution time: %s seconds " % (end_time - start_time))

start_time = time.time()
os.system("python " + convert_script_path + fastq_dir_path)
end_time = time.time()
print("SEPSIS dataset fastq to fasta execution time: %s seconds " % (end_time - start_time))

old_fastq_dir_path = datadir + "/covid/default/fastq/"
os.system("cp -r " + old_fastq_dir_path + 'human_* ' + fastq_dir_path)

# Align to  reference genomes using minimap2
# OPT1: ref_path, OPT2: fasta_dir_path, OPT3: sam_dir_path
start_time = time.time()
os.system("python " + minimap_script_path + human_ref_path + " " + fastq_dir_path + " " + sam_dir_path)
end_time = time.time()
print("SEPSIS dataset minimap2 after basecalling execution time: %s seconds " % (end_time - start_time))


