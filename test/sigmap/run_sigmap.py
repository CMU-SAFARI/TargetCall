import os
import sys 

fast5_dir_path = sys.argv[1]
output_dir_path = sys.argv[2]
ref_path = sys.argv[3]
index_dir = sys.argv[4]
sigmap_exe_path = sys.argv[5]

options = " -p /mnt/batty/bcavlak/bio/tools/sigmap/extern/kmer_models/r9.4_180mv_450bps_6mer/template_median68pA.model -t 128 "

dir_list = os.listdir(fast5_dir_path)

for dir in dir_list:
    refpath = " -r " + ref_path
    indexdir = " -x " + index_dir
    fast5dir = " -s " + fast5_dir_path + dir
    outdir = " -o " + output_dir_path + dir + ".paf "
    print("\n" + sigmap_exe_path + " -m " + refpath + options + indexdir + fast5dir + outdir)
    os.system(sigmap_exe_path + " -m " + refpath + options + indexdir + fast5dir + outdir)
