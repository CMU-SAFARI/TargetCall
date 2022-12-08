#!/bin/bash

mkdir -p TargetCall

#Download refs and fast5 files
wget https://zenodo.org/record/7334592/files/simulated-virus.tar.gz; tar -xzf simulated-virus.tar.gz; rm simulated-virus.tar.gz
wget https://zenodo.org/record/7335539/files/real-virus.tar.gz; tar -xzf real-virus.tar.gz; rm real-virus.tar.gz
wget https://zenodo.org/record/7335517/files/sepsis-bacteria.tar.gz; tar -xzf sepsis-bacteria.tar.gz; rm sepsis-bacteria.tar.gz
wget https://zenodo.org/record/7335525/files/metagenomics-bacteria.tar.gz; tar -xzf metagenomics-bacteria.tar.gz; rm metagenomics-bacteria.tar.gz
wget https://zenodo.org/record/7402342/files/human_2.tar.gz; tar -xzf human_2.tar.gz; rm human_2.tar.gz
wget https://zenodo.org/record/7334648/files/human.tar.gz; tar -xzf human.tar.gz; rm human.tar.gz
wget https://zenodo.org/record/7335545/files/refs.tar.gz; tar -xzf refs.tar.gz; rm refs.tar.gz

mv refs TargetCall
mv fast5/human2/* fast5/human/
rmdir fast5/human2/
mv fast5/ TargetCall
mkdir -p TargetCall/outputs
