# NPM1_DeepSeq
Analysis pipeline for Ultra Deep Sequencing of NPM1 exon 11.

Requirements:

- Conda

Conda will install the rest of the requirements to a new environment automatically, which will be used for the analysis. You can look in `environment.yaml` to see exactly which softwares are used.

How to run:

    bash run_NPM1_analysis.sh <full path to folder containing all *fastq.gz> <full path to output folder> <full path human reference fasta> <email adress to recieve result email (OPTIONAL, requires extra configuration)>
Note: Arguments are positional.

Some notes on speed: The pipeline will adapt the # of cores used to what is available on the system. It is recommended that the machine has at least as many logical cores as samples are being run. The pipeline has been tested and works on a 4c/8t machine with 16GB RAM. This pipeline is fairly I/O intensive, either RAID disks or SSD is recommended for optimal speed.

The first time the pipeline is run, it will need to download and install all the dependencies into the new Conda environment called `NPM1_DeepSeq`, which will take some time. Additionally, the pipeline needs a bwa reference for some steps, so if the reference fasta in not yet a bwa reference, one will be generated, which will take some extra time. Make sure you have write permissions in the reference directory if this is the case.

Emailing:
You will need to configure the function `send_mail` in `npm_var.py` in order to send eamils. Specifically you need to input your smtp sever into the `host` variable on line 121.  

Variants:
You can see which variants are being searched for in the `npm_seq.py` file. You can also add additional variants using this file.

Please report any bugs or issues on the GitHub "Issues" tab or email alvar.almstedt@gu.se
