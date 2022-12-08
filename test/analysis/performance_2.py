import sys
import os

out_dir_path = sys.argv[1]
models = ["default", "TINYX0111", "TINYX011", "TINYX01", "TINYX2", "TINYX3"]

use_cases = ["sepsis", "viral", "covid"]

execution_times = []
for model in models:
    execution_times.append([])
    for use_case in use_cases:
        execution_times[-1].append(0.0)


for idx, model in enumerate(models):
    file_name = out_dir_path + model + "_2.out"

    if not os.path.exists(file_name):
        continue

    out_file = open(file_name)

    for line in out_file:
        if line.startswith("COVID"):
            index = line.strip().split(":")
            value = index[-1].strip().split(" ")
            execution_times[idx][2] += float(value[0].strip())
        elif line.startswith("VIRAL"):
            index = line.strip().split(":")
            value = index[-1].strip().split(" ")
            execution_times[idx][1] += float(value[0].strip())
        elif line.startswith("SEPSIS"):
            index = line.strip().split(":")
            value = index[-1].strip().split(" ")
            execution_times[idx][0] += float(value[0].strip())


# PRINT the values in tsv format
print("Execution Times", end = "")
for model in models:
    print("\t" + model, end = "")


for idx, use_case in enumerate(use_cases):
    print("\n" + use_cases[idx], end = "")
    for idx2, model in enumerate(models):
        print("\t" + str(execution_times[idx2][idx]), end = "")

print("\n", end = "")
