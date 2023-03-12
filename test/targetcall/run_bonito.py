import os
import sys 

read_dir_path = sys.argv[1]
output_dir_path = sys.argv[2]
model_name = sys.argv[3]

dir_list = os.listdir(read_dir_path)
batch=0
modeltype = ''

if model_name == "TINYX011":
    batch=128
    modeltype = 'tinynoskipx011'


model_path = '../../bonito/models/' + model_name + '/'

for dir in dir_list:
    print("\nbonito basecaller " + model_path + " " + read_dir_path + dir + "/ --batchsize " + str(batch) + " --modeltype " + modeltype + " > " + output_dir_path + dir + ".fastq")
    os.system("bonito basecaller " + model_path + " " + read_dir_path + dir + "/ --batchsize " + str(batch) +" --modeltype "+ modeltype + " > " + output_dir_path + dir + ".fastq")
    os.system("rm " + output_dir_path + dir + "_summary.tsv")
