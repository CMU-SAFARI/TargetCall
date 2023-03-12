import sys
import os

data_file = open(sys.argv[1])

total_duration = 0
num_samples = 0
total_reads = 0

last_duration = -1
for line in data_file:
    if " completed reads" in line:
        total_reads += int(line.strip().split(":")[-1])
        continue
    elif "duration" in line:
        secs = line.strip().split(":")[-1]
        mins = line.strip().split(":")[-2]
        total_duration += int(secs) + int(mins)*60
        last_duration = int(secs) + int(mins)*60
    elif "samples per second" in line:
        sps = line.strip().split(" ")[-1][:3]
        num_samples += float(sps)*last_duration

print(f"Total number of samples: {num_samples} million")
print(f"Total duration: {total_duration//60} minutes {total_duration%60} seconds")
print(f"Total number of reads: {total_reads}")
print(f"Average: {num_samples/total_duration} million samples per second")