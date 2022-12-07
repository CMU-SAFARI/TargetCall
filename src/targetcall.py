import os
import sys 

read_dir_path = sys.argv[1]
ref_path = sys.argv[2]
model_name = sys.argv[3]
out_dir_path = sys.argv[4]

batch=0
modeltype = ''

if model_name == "default":
    batch=512
    modeltype = 'default'
    
elif model_name == "TINYX1":
    batch=1600
    modeltype = 'tinynoskipx1'

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


model_path = '../bonito/models/' + model_name + '/'


print("\nbonito basecaller " + model_path + " " + read_dir_path + "/ --batchsize " + str(batch) + " --modeltype " + modeltype + " > " + out_dir_path + '/output.fastq')
os.system("bonito basecaller " + model_path + " " + read_dir_path + "/ --batchsize " + str(batch) +" --modeltype "+ modeltype + " > " + out_dir_path + '/output.fastq')
print("\npython fastq_to_fasta.py " + out_dir_path +  '/output.fastq ' + out_dir_path + '/output.fasta ')
os.system("python fastq_to_fasta.py " + out_dir_path + '/output.fastq ' + out_dir_path + '/output.fasta ')
print("\nminimap2 -a -x map-ont -t 16 " + ref_path + " " + out_dir_path + '/output.fasta ' + " > " + out_dir_path + '/output.sam ')
os.system("minimap2 -a -x map-ont -t 16 " + ref_path + " " + out_dir_path + '/output.fasta ' + " > " + out_dir_path + '/output.sam ')
print("\npython extract_filtered.py " + out_dir_path + '/output.sam ' + out_dir_path + '/readids.txt ')
os.system("python extract_filtered.py " + out_dir_path + '/output.sam ' + out_dir_path + '/readids.txt ')

