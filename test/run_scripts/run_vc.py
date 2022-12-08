import os
import sys 

relative_ref_path = sys.argv[1]
sam_dir_path = sys.argv[2]
bam_dir_path = sys.argv[3]
vcf_dir_path = sys.argv[4]
data_dir_path = sys.argv[5]

samtools_bin_path = '/mnt/batty-shared/tools/bin//samtools '
config_sam_path = '../utils/configure_sam.py '

dir_list = os.listdir(sam_dir_path)

for dir in dir_list:
    test = dir.strip().split(".")
    print("\npython" + config_sam_path + sam_dir_path + dir + ' ' + sam_dir_path + dir + '_2')
    os.system('python ' + config_sam_path + sam_dir_path + dir + ' ' + sam_dir_path + dir + '_2')
    os.system('mv ' + sam_dir_path + dir + '_2 ' + sam_dir_path + dir)

for dir in dir_list:
    test = dir.strip().split(".")
    print("\n" + samtools_bin_path + 'view -h ' + sam_dir_path + dir + " | " + samtools_bin_path + ' sort -l5 -m4G -@ 16 -o ' + bam_dir_path + test[0] + ".bam")
    os.system(samtools_bin_path + 'view -h ' + sam_dir_path + dir + " | " + samtools_bin_path + ' sort -l5 -m4G -@ 16 -o ' + bam_dir_path + test[0] + ".bam")
    print("\n" + samtools_bin_path + ' index -b ' + bam_dir_path + test[0] + ".bam")
    os.system(samtools_bin_path + ' index -b ' + bam_dir_path + test[0] + ".bam")

dir_list = os.listdir(bam_dir_path)

# BIN_VERSION="1.4.0"
for dir in dir_list:
    if 'bai' not in dir:
        test = dir.strip().split("/")
        name = test[-1].strip().split('.')
        input_dir = ' -v \"' + data_dir_path + '\":\"/input\"'
        output_dir = ' -v \"' + vcf_dir_path + '\":\"/output\"' 
        param1 = ' --model_type=WGS '
        param2 = ' --ref=/input/' + relative_ref_path
        param3 = ' --reads=/input/' + bam_dir_path.replace(data_dir_path, '') + dir
        param4 = ' --output_vcf=/output/' + name[0] + '.vcf.gz' 
        param5 = ' --output_gvcf=/output/' + name[0] + '.g.vcf.gz ' 
        param6 = ' --num_shards=48' 
        print('\n docker run ' + input_dir + output_dir + ' google/deepvariant:\"${BIN_VERSION}\" /opt/deepvariant/bin/run_deepvariant ' + param1 + param2 + param3 + param4 + param5 + param6 )
        os.system('docker run ' + input_dir + output_dir + ' google/deepvariant:\"1.4.0\" /opt/deepvariant/bin/run_deepvariant ' + param1 + param2 + param3 + param4 + param5 + param6 )
