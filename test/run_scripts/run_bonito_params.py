import os
import sys 

read_dir_path = sys.argv[1]
output_dir_path = sys.argv[2]
read_ids_dir_path = sys.argv[3]
use_case = sys.argv[4]

dir_list = os.listdir(read_ids_dir_path)

batch=512
modeltype = 'default'

model_path = '../../bonito/models/default/'

for dir in dir_list:
    test = dir.strip().split(".")
    read_id_path = read_ids_dir_path + dir
    ffastq_path = output_dir_path + test[0].strip() + '.fastq'

    subdir = ''
    if 'human' in test[0]:
        subsubdir = test[0].strip().split("_")
        subdir = 'human/' + subsubdir[1]
    elif 'covid' in test[0]:
        subdir = 'virus/real/SARS-CoV-2'
    elif 'virus' in test[0]:
        subdir = 'virus/simulated/' + test[0][6:]
    else:
        if use_case == 'sepsis':
            subdir = 'sepsis-bacteria/' + test[0][9:]
        else:
            subdir = 'metagenomics-bacteria/' + test[0][9:]


    fast5_path = read_dir_path + subdir

    print("\nbonito basecaller " + model_path + " " + fast5_path + "/ --batchsize " + str(batch) +" --modeltype "+ modeltype + ' --read-ids ' + read_id_path + " > " + ffastq_path)
    os.system("bonito basecaller " + model_path + " " + fast5_path + "/ --batchsize " + str(batch) +" --modeltype "+ modeltype + ' --read-ids ' + read_id_path + " > " + ffastq_path )
    os.system("rm " + output_dir_path + test[0].strip() + "_summary.tsv")
