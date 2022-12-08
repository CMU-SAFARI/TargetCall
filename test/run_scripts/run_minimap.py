import os
import sys 

ref_path = sys.argv[1]
fasta_dir_path = sys.argv[2]
sam_dir_path = sys.argv[3]

dir_list = os.listdir(fasta_dir_path)

for dir in dir_list:
    test = dir.strip().split(".")
    print("\nbio minimap2 -a -x map-ont --secondary=no -t 40 " + ref_path + " " + fasta_dir_path + dir + " > " + sam_dir_path + test[0] + ".sam")
    os.system("minimap2 -a -x map-ont --secondary=no -t 40 " + ref_path + " " + fasta_dir_path + dir + " > " + sam_dir_path + test[0] + ".sam")
