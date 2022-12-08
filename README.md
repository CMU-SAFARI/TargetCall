# TargetCall

TargetCall is the first pre-basecalling filter that is applicable to a wide range of use cases. TargetCall’s key idea is to quickly filter out off-target reads (i.e., reads that are dissimilar to the target reference.) before the basecalling step to eliminate the wasted computation in basecalling. TargetCall is based on ONT basecaller Bonito.

## Prerequisites

TargetCall requires minimap2 to be installed. Minimap2 can be installed via [Minimap2 (v2.24)](https://github.com/lh3/minimap2/releases/tag/v2.24)

## Installation
TargetCall is tested on Linux with conda version 4.7.12.

```bash
$ git clone https://github.com/CMU-SAFARI/TargetCall
$ cd TargetCall
$ conda create --name targetcall python=3.8.10
$ conda activate targetcall
(targetcall) $ pip install --upgrade pip
(targetcall) $ pip install -r requirements.txt
(targetcall) $ python setup.py develop
```

## Usage

```bash
$ cd src
$ python targetcall.py ../sample_data/fast5/ ../sample_data/Monkeypox_virus.fasta TINYX011 ../sample_data/
```
This will create three output files under ../sample_data/
- output.fasta: contains noisy basecalled reads of fast5 files using model TINYX011
- output.sam: contains alignment of noisy reads to Monkeypox_virus reference.
- readids.txt: the read IDs of reads that are accepted by the filter.

Read IDs can be used as an input to Bonito for basecalling only the reads that are accepted by the filter using the --read-ids option.

## Provided Models

You can find all models listed under bonito/models/.

| Model Name  | Model Name in the Paper | # of Parameters  | Basecalling Accuracy |
| ------------- | ------------- | ------------- | ------------- |
| default  | Bonito  | 9739K  | 94.60%  |
| TINYX0111  | LC-Main*2  | 565K  | 90.91%  |
| TINYX011  | LC-Main  | 292K  | 89.75%  |
| TINYX01  | LC-Main/2  | 146K  | 86.83%  |
| TINYX2  | LC-Main/4 | 52K  | 80.82%  |
| TINYX3  | LC-Main/8  | 21K  | 70.42%  |

## Reproducing the results in the paper

We explain how to reproduce the results we show in the TargetCall paper in the [test directory](./test/).

