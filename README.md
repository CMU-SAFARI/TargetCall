# TargetCall

TargetCall is the first pre-basecalling filter that is applicable to a wide range of use cases. TargetCall’s key idea is to quickly filter out off-target reads (i.e., reads that are dissimilar to the target reference.) before the basecalling step to eliminate the wasted computation in basecalling.

## Prerequisites

TargetCall requires minimap2 to be installed. Minimap2 can be installed via [Minimap2 (v2.24)](https://github.com/lh3/minimap2/releases/tag/v2.24)

## Installation

```bash
$ git clone https://github.com/CMU-SAFARI/TargetCall
$ cd bonito
$ python3 -m venv venv3
$ source venv3/bin/activate
(venv3) $ pip install --upgrade pip
(venv3) $ pip install -r requirements.txt
(venv3) $ python setup.py develop
```

## Usage

```bash
$ cd src
$ python targetcall.py ../sample_data/fast5/ ../sample_data/Monkeypox_virus.fasta TINYX011 ../sample_data/outputs/
```

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

### Licence and Copyright
(c) 2019 Oxford Nanopore Technologies Ltd.

Bonito is distributed under the terms of the Oxford Nanopore
Technologies, Ltd.  Public License, v. 1.0.  If a copy of the License
was not distributed with this file, You can obtain one at
http://nanoporetech.com

### Research Release

Research releases are provided as technology demonstrators to provide early access to features or stimulate Community development of tools. Support for this software will be minimal and is only provided directly by the developers. Feature requests, improvements, and discussions are welcome and can be implemented by forking and pull requests. However much as we would like to rectify every issue and piece of feedback users may have, the developers may have limited resource for support of this software. Research releases may be unstable and subject to rapid iteration by Oxford Nanopore Technologies.


