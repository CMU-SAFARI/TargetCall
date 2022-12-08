import os
import sys 
import time

datadir = sys.argv[1] # should point to the directory where the fast5 & reds dir exist
model_name = 'default'

print("Model Name: " + model_name)

# Python Script Paths
exedir = "../run_scripts/" # the path to HierarchyCall's test/run_scripts dir  
minimap_script_path = exedir + "run_minimap.py "
convert_script_path = exedir + "run_convert.py "
vc_script_path = exedir + "run_vc.py "


# Reference Genome Paths
covid_ref_path = datadir + "refs/Severe_acute_respiratory_syndrome_coronavirus_2_isolate_Wuhan-Hu-1.mmi"
combined_viral_path = datadir + "refs/combined_viral.mmi"
bacterial_ref_path = datadir + "refs/bacterial.mmi"

# File Paths
fastq_dir_path = datadir + '/covid/' + model_name + '/fastq/'
sam_dir_path = datadir + '/covid/' + model_name + '/filtered-sam/'
os.system("mkdir -p " + sam_dir_path)
bam_dir_path = datadir + '/covid/' + model_name + '/bam/'
os.system("mkdir -p " + bam_dir_path)
vcf_dir_path = datadir + '/covid/' + model_name + '/vcf/'
os.system("mkdir -p " + vcf_dir_path)


# OPT1: ref_path, OPT2: fasta_dir_path, OPT3: sam_dir_path
start_time = time.time()
os.system("python " + minimap_script_path + covid_ref_path + " " + fastq_dir_path + " " + sam_dir_path)
end_time = time.time()
print("COVID dataset read mapping execution time: %s seconds " % (end_time - start_time))

# RUN DeepVariant 
start_time = time.time()
os.system("python " + vc_script_path + " refs/Severe_acute_respiratory_syndrome_coronavirus_2_isolate_Wuhan-Hu-1.fasta " + " " + sam_dir_path + " " + bam_dir_path + " " + vcf_dir_path + " " + datadir)
end_time = time.time()
print("COVID dataset variant calling execution time: %s seconds " % (end_time - start_time))








# File Paths
fastq_dir_path = datadir + '/viral/' + model_name + '/fastq/'
sam_dir_path = datadir + '/viral/' + model_name + '/filtered-sam/'
os.system("mkdir -p " + sam_dir_path)
bam_dir_path = datadir + '/viral/' + model_name + '/bam/'
os.system("mkdir -p " + bam_dir_path)
vcf_dir_path = datadir + '/viral/' + model_name + '/vcf/'
os.system("mkdir -p " + vcf_dir_path)

# OPT1: ref_path, OPT2: fasta_dir_path, OPT3: sam_dir_path
start_time = time.time()
os.system("python " + minimap_script_path + combined_viral_path + " " + fastq_dir_path + " " + sam_dir_path)
end_time = time.time()
print("VIRAL dataset read mapping execution time: %s seconds " % (end_time - start_time))

# RUN DeepVariant 
start_time = time.time()
os.system("python " + vc_script_path + " refs/combined_viral.fasta " + " " + sam_dir_path + " " + bam_dir_path + " " + vcf_dir_path + " " + datadir)
end_time = time.time()
print("VIRAL dataset variant calling execution time: %s seconds " % (end_time - start_time))






# File Paths
fastq_dir_path = datadir + '/sepsis/' + model_name + '/fastq/'
sam_dir_path = datadir + '/sepsis/' + model_name + '/filtered-sam/'
os.system("mkdir -p " + sam_dir_path)
bam_dir_path = datadir + '/sepsis/' + model_name + '/bam/'
os.system("mkdir -p " + bam_dir_path)
vcf_dir_path = datadir + '/sepsis/' + model_name + '/vcf/'
os.system("mkdir -p " + vcf_dir_path)

# OPT1: ref_path, OPT2: fasta_dir_path, OPT3: sam_dir_path
start_time = time.time()
os.system("python " + minimap_script_path + bacterial_ref_path + " " + fastq_dir_path + " " + sam_dir_path)
end_time = time.time()
print("SEPSIS dataset read mapping execution time: %s seconds " % (end_time - start_time))

# RUN DeepVariant 
start_time = time.time()
os.system("python " + vc_script_path + " refs/bacterial.fasta " + " " + sam_dir_path + " " + bam_dir_path + " " + vcf_dir_path + " " + datadir)
end_time = time.time()
print("SEPSIS dataset variant calling execution time: %s seconds " % (end_time - start_time))
