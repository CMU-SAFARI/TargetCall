import os
import sys

sam_file_path = sys.argv[1]
readids_file_path = sys.argv[2]

test = sam_file_path.strip().split(".")
sam_file = open(sam_file_path)
seq_dict = {}
for line in sam_file:
    if not line.startswith("@"):
        line = line.strip()
        words = line.split()

        if(words[0] not in seq_dict.keys()):
            seq_dict[words[0]] = "not aligned"

        if test[-1] == 'sam':
            if words[2] != "*":
                seq_dict[words[0]] = "aligned"

        elif test[-1] == 'paf':
            if words[5] != "*":
                seq_dict[words[0]] = "aligned"

# Process all the aligned words and copy them to the copy_dir
readids_file = open(readids_file_path, 'w')
for key in seq_dict:
    is_aligned = seq_dict[key]

    # Passes our filter, COPY
    if is_aligned == "aligned":
        readids_file.write(key + '\n')