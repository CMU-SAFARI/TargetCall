import sys
import os

def extract_stats(gd_file_name, test_file_name, usecase):
    print("ref: " + gd_file_name)
    print("test: " + test_file_name)

    gd_file = open(gd_file_name)
    test_file = open(test_file_name)

    seq_dict = {}
    result_dict = {}

    for line in gd_file:
        if not line.startswith("@"):
            line = line.strip()
            words = line.split()

            if(words[0] not in seq_dict.keys()):
                seq_dict[words[0]] = "not aligned"

            if words[2] != "*":
                seq_dict[words[0]] = "aligned"

    TP_count = 0
    FP_count = 0
    TN_count = 0
    FN_count = 0

    for line in test_file:
        if not line.startswith("@"):
            line = line.strip()
            words = line.split()

            is_aligned = "not aligned"
            if words[0] in seq_dict:
                is_aligned = seq_dict[words[0]]
            seq_dict[words[0]] = "counted"
            # Does not pass our filter
            if(".sam" in test_file_name):
                if words[2] == "*":
                    if is_aligned == "not aligned":
                        TN_count = TN_count + 1
                    elif is_aligned == "aligned":
                        FN_count = FN_count + 1
                # Passes our filter
                else: 
                    if is_aligned == "not aligned":
                        FP_count = FP_count + 1
                    elif is_aligned == "aligned":
                        TP_count = TP_count + 1

            elif(".paf" in test_file_name):
                if words[5] == "*":
                    if is_aligned == "not aligned":
                        TN_count = TN_count + 1
                    elif is_aligned == "aligned":
                        FN_count = FN_count + 1
                # Passes our filter
                else: 
                    if is_aligned == "not aligned":
                        FP_count = FP_count + 1
                    elif is_aligned == "aligned":
                        TP_count = TP_count + 1
    
    if use_case == "viral" or use_case ==  "covid":
        return TP_count, FP_count, TN_count, FN_count
    else:
        return TN_count, FN_count, TP_count, FP_count

data_dir_path = sys.argv[1]
models = ["TINYX0111", "TINYX011", "TINYX01", "TINYX2", "TINYX3"]
use_cases = ["sepsis", "viral", "covid"]

TPs = []
TNs = []
FPs = []
FNs = []
for use_case in use_cases:
    TPs.append([])
    TNs.append([])
    FPs.append([])
    FNs.append([])
    for model in models:
        TPs[-1].append(0)
        TNs[-1].append(0)
        FPs[-1].append(0)
        FNs[-1].append(0)

for idx, use_case in enumerate(use_cases):     
    for idx2, model in enumerate(models):
        dir_path = data_dir_path + use_case + "/" + model  + "/sam/"
        default_dir_path = data_dir_path + use_case + "/default/sam/"
        dir_list = os.listdir(dir_path)
        
        for dir in dir_list:
            file_path = dir_path + dir
            nameinit = dir.strip().split('.')
            default_file_path = default_dir_path + nameinit[0] + '.sam'
            TP, FP, TN, FN = extract_stats(default_file_path, file_path, use_case)
            TPs[idx][idx2] += TP
            FPs[idx][idx2] += FP
            TNs[idx][idx2] += TN
            FNs[idx][idx2] += FN


# PRINT the values in tsv format
print("TP", end = "")
for model in models:
    print("\t" + model, end = "")

for idx, use_case in enumerate(use_cases):
    print("\n" + use_cases[idx], end = "")
    for idx2, model in enumerate(models):
        print("\t" + str(TPs[idx][idx2]), end = "")

print("\nFP", end = "")
for model in models:
    print("\t" + model, end = "")

for idx, use_case in enumerate(use_cases):
    print("\n" + use_cases[idx], end = "")
    for idx2, model in enumerate(models):
        print("\t" + str(FPs[idx][idx2]), end = "")


print("\n ----- PRINTING TRUE NEGATIVES ---- ")
print("\nTN", end = "")
for model in models:
    print("\t" + model, end = "")

for idx, use_case in enumerate(use_cases):
    print("\n" + use_cases[idx], end = "")
    for idx2, model in enumerate(models):
        print("\t" + str(TNs[idx][idx2]), end = "")


print("\n ----- PRINTING FALSE NEGATIVES ---- ")
print("\nFN", end = "")
for model in models:
    print("\t" + model, end = "")

for idx, use_case in enumerate(use_cases):
    print("\n" + use_cases[idx], end = "")
    for idx2, model in enumerate(models):
        print("\t" + str(FNs[idx][idx2]), end = "")
