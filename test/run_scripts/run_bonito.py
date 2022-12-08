import os
import sys 

read_dir_path = sys.argv[1]
output_dir_path = sys.argv[2]
model_name = sys.argv[3]

dir_list = os.listdir(read_dir_path)
batch=0
modeltype = ''

if model_name == "default":
    batch=512
    modeltype = 'default'
    
elif model_name == "TINYX1":
    batch=1600
    modeltype = 'tinynoskipx1'

elif model_name == "TINYX0111":
    batch=1600
    modeltype = 'tinynoskipx0111'

elif model_name == "TINYX011":
    batch=3200
    modeltype = 'tinynoskipx011'

elif model_name == "TINYX01":
    batch=6400
    modeltype = 'tinynoskipx01'
    
elif model_name == "TINYX2":
    batch=12800
    modeltype = 'tinynoskipx2'

elif model_name == "TINYX3":
    batch=25600
    modeltype = 'tinynoskipx3'

elif model_name == "TINYX4":
    batch=51200
    modeltype = 'tinynoskipx4'


model_path = '../../bonito/models/' + model_name + '/'

for dir in dir_list:
    print("\nbonito basecaller " + model_path + " " + read_dir_path + dir + "/ --batchsize " + str(batch) + " --modeltype " + modeltype + " > " + output_dir_path + dir + ".fastq")
    os.system("bonito basecaller " + model_path + " " + read_dir_path + dir + "/ --batchsize " + str(batch) +" --modeltype "+ modeltype + " > " + output_dir_path + dir + ".fastq")
    os.system("rm " + output_dir_path + dir + "_summary.tsv")
