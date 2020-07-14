# NPM1_DeepSeq
Analysis pipeline for Ultra Deep Sequencing of NPM1

Requirements:

- Conda

Conda will install the rest of the requirements to a new environment automatically, which will be used for the analysis. You can look in `environment.yaml` to see exactly which softwares are used.

How to run:

    bash run_NPM1_analysis.sh <full path to folder containing all *fastq.gz> <full path to output folder> <full path human reference fasta> <email adress to recieve result email (OPTIONAL, requires extra configuration)>

Some notes on speed: The pipeline will adapt the #cores used to what ia available to the system. It is recommended that the machine has at least as many logical cores as samples are being run. The pipeline has been tested and works on a 4c/8t machine with 16GB RAM. This pipeline is fairly IO intensive, either RAID disks SSD is recommended.

The first time the pipeline is run, it will need to download and install all the dependencies into the new Conda environment called `NPM1_DeepSeq`, which will take some additional time. Additionally the pipeline needs a bwa reference for some steps, so if the reference fasta in not yet a bwa reference, one will be generated, which will take some extra time.

Emailing:
You will need to configure the function `send_mail` in `npm_var.py` in order to send eamils. Specifically you need to input your smtp sever into the `host` variable on line 121.  
