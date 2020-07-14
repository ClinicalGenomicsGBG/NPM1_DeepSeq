# NPM1_DeepSeq
Analysis pipeline for Ultra Deep Sequencing of NPM1

Requirements:

- Conda

Conda will install the rest of the requirements to a new environment automatically, which will be used for the analysis. You can look in `environment.yaml` to see exactly which softwares are used

How to run:

    bash run_NPM1_analysis.sh <full path to folder containing fastq.gz> <full path to output folder> <full path human reference fasta> <email adress to recieve result email (OPTIONAL, requires extra configuration)>
    
Notes on emailing:
You will need to configure one of the fuctions in `npm_var.py` in order to send eamils
