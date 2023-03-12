import sys
import os

out_dir_path = sys.argv[1]
models = ["sigmap", "uncalled", "TINYX011"]

use_cases = ["covid", "viral", "sepsis_chm13", "sepsis_hg38"]

execution_times = []
for model in models:
    execution_times.append([])
    for use_case in use_cases:
        execution_times[-1].append(0.0)


for idx, model in enumerate(models):
    if model == "sigmap":
        for idx2, use_case in enumerate(use_cases):
            file_name = out_dir_path + model + "_" + use_case + ".out"
            out_file = open(file_name)
            for line in out_file:
                if "reads in" in line:
                    index = line.strip().split(" ")
                    value = index[-1].strip()
                    value = value[:-2]
                    print(value)
                    execution_times[idx][idx2] -= float(value)

                if "seconds" in line:
                    index = line.strip().split(":")
                    value = index[-1].strip().split(" ")
                    execution_times[idx][idx2] += float(value[0].strip())

        file_name = out_dir_path + "sigmap_basecall.out"
        out_file = open(file_name)

        for line in out_file:
            if line.startswith("COVID"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][0] += float(value[0].strip())

            if line.startswith("VIRAL"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][1] += float(value[0].strip())

            if line.startswith("SEPSIS-chm13"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][2] += float(value[0].strip())

            if line.startswith("SEPSIS-hg38"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][3] += float(value[0].strip())


    elif model == "uncalled":
        file_name = out_dir_path + model + ".out"
        out_file = open(file_name)

        for line in out_file:
            if line.startswith("COVID"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][0] += float(value[0].strip())

            if line.startswith("VIRAL"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][1] += float(value[0].strip())

            if line.startswith("SEPSIS-chm13"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][2] += float(value[0].strip())

                

        file_name = out_dir_path + model + "_basecall.out"
        out_file = open(file_name)
        
        for line in out_file:
            if line.startswith("COVID"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][0] += float(value[0].strip())

            if line.startswith("VIRAL"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][1] += float(value[0].strip())

            if line.startswith("SEPSIS-chm13"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][2] += float(value[0].strip())

    elif model == "TINYX011":
        file_name = out_dir_path + model + ".out"
        out_file = open(file_name)

        for line in out_file:
            if line.startswith("COVID"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][0] += float(value[0].strip())
                if line.startswith("COVID Human LightCall"):
                    execution_times[idx][2] += float(value[0].strip())
                    execution_times[idx][3] += float(value[0].strip())

            if line.startswith("VIRAL"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][1] += float(value[0].strip())

            if line.startswith("SEPSIS-chm13"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][2] += float(value[0].strip())

            if line.startswith("SEPSIS-hg38"):
                index = line.strip().split(":")
                value = index[-1].strip().split(" ")
                execution_times[idx][3] += float(value[0].strip())
                if line.startswith("SEPSIS-hg38 Sepsis-bacteria LightCall"):
                    execution_times[idx][2] += float(value[0].strip())


# PRINT the values in tsv format
print("Execution Times", end = "")
for model in models:
    print("\t" + model, end = "")


for idx, use_case in enumerate(use_cases):
    print("\n" + use_cases[idx], end = "")
    for idx2, model in enumerate(models):
        print("\t" + str(execution_times[idx2][idx]), end = "")

print("\n", end = "")
