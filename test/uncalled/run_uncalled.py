import os
import sys 

fast5_dir_path = sys.argv[1]
output_dir_path = sys.argv[2]
index_dir = sys.argv[3]
uncalled_exe = sys.argv[4]

dir_list = os.listdir(fast5_dir_path)

# IMPORTANT NOTE: always run this script after the command:
# conda activate uncalled
for dir in dir_list:
    # /home/bcavlak/.local/bin/uncalled
    outdir = " > " + output_dir_path + dir + ".paf "
    print("\n" + uncalled_exe + " map -t 8 " + index_dir + " " + fast5_dir_path + dir + outdir)
    os.system(uncalled_exe + " map -t 8 " + index_dir + " " + fast5_dir_path + dir + outdir)
