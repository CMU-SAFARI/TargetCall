# Reproducing the results in the paper

We explain how we evaluate TargetCall in our paper in arxiv to enable easy reproduction of the results.

## Prerequisites

We evalutate the performance and accuracy benefits of TargetCall by integrating it into Bonito pipeline. We compare TargetCall with UNCALLED and Sigmap.

We list the links to download and compile each tool for comparison below:

* [UNCALLED](https://github.com/skovaka/UNCALLED)
* [Sigmap](https://github.com/haowenz/sigmap)

We use various tools to process and analyze the data we generate using each tool. The following tools must also be installed in your machine:

* [Minimap2](https://github.com/lh3/minimap2)
* [DeepVariant](https://github.com/google/deepvariant/blob/r1.4/docs/deepvariant-quick-start.md)

Please make sure that all of these tools are in your `PATH`

## Datasets

All the datasets can be downloaded via Zenodo. We provide the script to download all these files under [data directory](./data/). In order to download:

```bash
cd data

bash download-data.sh # Download entire dataset and organize it
cd .. #going back to the test directory
```

Now that you have downloaded all the datasets, we can start running all the tools to collect the results.

## Integrating TargetCall to Bonito

### Bonito

Here we run Bonito without TargetCall. $datadir should be the absolute path of /data/TargetCall/

```bash
(targetcall) $ cd default
(targetcall) $ python reproduce.py $datadir &> ../data/TargetCall/outputs/default.out
(targetcall) $ python reproduce2.py $datadir &> ../data/TargetCall/outputs/default_2.out
(targetcall) $ cd ..
```

### TargetCall

Here we run TargetCall before Bonito. $model_name is the name of the model you would like to test. The names from the table in README should be used for the evaluations.

```bash
(targetcall) $ cd filters
(targetcall) $ python reproduce.py $datadir $model_name &> ../data/TargetCall/outputs/$model_name.out
(targetcall) $ python reproduce2.py $datadir $model_name &> ../data/TargetCall/outputs/$model_name_2.out
(targetcall) $ cd ..
```

## Comparing TargetCall with Targeted Sequencing Methods

We compare TargetCall with two state-of-the-art targeted sequencing methods, UNCALLED and Sigmap.

### UNCALLED

Here we run UNCALLED on datasets of three use cases (except sepsis use case for reference genome hg38). We need to run two scripts to get results for UNCALLED since we created two virtual environments when performing our evaluations. The first script should be run within the environment UNCALLED is installed. The second, should be run within the environment TargetCall is installed. $uncalled_exe should be the absolute path to the UNCALLED executable.

```bash
(targetcall) $ cd uncalled 
(UNCALLED) $ python compare_uncalled.py $datadir $uncalled_exe &> ../data/TargetCall/outputs/uncalled.out
(targetcall) $ python uncalled_basecall.py $datadir &> ../data/TargetCall/outputs/uncalled_basecall.out.out
(targetcall) $ cd ..
```

### Sigmap

Here we run Sigmap on datasets of three use cases on all four reference genomes. $sigmap_exe should be the absolute path to the sigmap executable. We have a seperate script for each use case. For collecting execution time numbers, we exclude the time to load reads for sigmap since this part is not pipelined for the rest of the code to simulate real time analysis.

```bash
(targetcall) $ cd sigmap 
(targetcall) $ python covid.py $datadir $sigmap_exe &> ../data/TargetCall/outputs/sigmap_covid.out
(targetcall) $ python viral.py $datadir $sigmap_exe &> ../data/TargetCall/outputs/sigmap_viral.out
(targetcall) $ python sepsis_chm13.py $datadir $sigmap_exe &> ../data/TargetCall/outputs/sigmap_sepsis_chm13.out
(targetcall) $ python sepsis_hg38.py $datadir $sigmap_exe &> ../data/TargetCall/outputs/sigmap_sepsis_hg38.out
(targetcall) $ python basecall.py $datadir &> ../data/TargetCall/outputs/sigmap_basecall.out
(targetcall) $ cd ..
```

### TargetCall

Here we run TargetCall with the best filter selected on all four target references. You may need to delete the old files before running the following command.

```bash
(targetcall) $ cd targetcall
(targetcall) $ python reproduce.py TINYX011 $datadir &> ../data/TargetCall/outputs/TINYX011.out
(targetcall) $ cd ..
```


## Comparing the Results

We provide the scripts we use for evaluating the results under the [analysis](./analysis/) directory. Below we explain how to evaluate the results we generate for 1) basecalling execution time, 2) end-to-end execution time and 3) filtering accuracy and 4) end-to-end accuracy.

### Basecalling Execution Time

Executing the code below will print the basecalling execution time of all the models we provide. If you only want to get the results for a specific set of models, you may need to adjust the list models in the code. 

```bash
$ cd analysis
$ cd python performance.py ../data/TargetCall/outputs/
$ cd ..
```

### End-to-End Execution Time

Executing the code below will print the read mapping and variant calling time of all the models we provide. If you only want to get the results for a specific set of models, you may need to adjust the list models in the code. To get the end-to-end execution time results, you need to combine the results below with the results you obtain in the previous section.

```bash
$ cd analysis
$ cd python performance_2.py ../data/TargetCall/outputs/
$ cd ..
```

### Filtering Accuracy

Executing the code below will print True Positive, True Negative, False Positive and False Negatives of all the models in filtering reads we provide. If you only want to get the results for a specific set of models, you may need to adjust the list models in the code. 

```bash
$ cd analysis
$ cd python read_accuracy.py ../data/TargetCall/
$ cd ..
```

### End-to-End Accuracy

Executing the code below will print the relative abundances of all species of all the models we provide. If you only want to get the results for a specific set of models, you may need to adjust the list models in the code. 

```bash
$ cd analysis
$ cd python relative_abundance.py ../data/TargetCall/
$ cd ..
```

### Comparison Against UNCALLED and Sigmap

To get comparison numbers of TargetCall against UNCALLED and Sigmap, you need to run the scripts from Filtering Accuracy sections with model list [TINYX011, uncalled, sigmap]. For collecting performance numbers to compare TargetCall against UNCALLED and Sigmap, you need the following commands.

```bash
$ cd analysis
$ cd python prior_performance.py ../data/TargetCall/outputs/
$ cd ..
```