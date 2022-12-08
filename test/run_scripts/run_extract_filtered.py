import os
import sys 

sam_dir_path = sys.argv[1]
readids_dir_path = sys.argv[2]
use_case = sys.argv[3]

dir_list = os.listdir(sam_dir_path)


# options: sam_file_path, readids_file_path, use_case
for dir in dir_list:
    test = dir.strip().split(".")
    print("\npython ../utils/extract_filtered.py " + sam_dir_path + dir + " " + readids_dir_path + test[0] + ".txt " + use_case)
    os.system("python ../utils/extract_filtered.py " + sam_dir_path + dir + " " + readids_dir_path + test[0] + ".txt " + use_case)
