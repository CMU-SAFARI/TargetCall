import os
import sys

sam_path = sys.argv[1]
modified_sam_path = sys.argv[2]

sam_file = open(sam_path)
modified_sam_file = open(modified_sam_path, 'w')

for line in sam_file:
    if line.startswith('@'):
        line = line.strip()
        modified_sam_file.write(line + '\n')
    else:
        fields = line.strip().split('\t')
        new_field =  "?" * len(fields[9])
        modified_sam_file.write('\t'.join([str(i) for i in fields[0:10]]) + "\t")
        modified_sam_file.write(new_field + "\t")
        modified_sam_file.write('\t'.join([str(i) for i in fields[11:]]) + '\n')
