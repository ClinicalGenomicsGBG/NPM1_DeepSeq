#!/bin/bash -l

#echo "$HOSTNAME"

scriptdir="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

echo "SCRIPTDIR: $scriptdir"

echo "Establishing conda environment at `date`"
conda env create -f $scriptdir/environment.yaml 2> /dev/null
echo ".. Done at `date`"

#echo "MY PYTHON: $(which python)"
#PYTHON=$(which python)

DATE=$(date +"%Y_%m_%d_%H_%M_%S")
DAY=$(date +"%Y%m%d")

FASTQDIR=$1
OUTDIR=$2
TMPDIR=$OUTDIR/tmp/NPM1_$DATE
CSV_SAVELOC=$OUTDIR/csv
REF=$3
EMAILS=$4

MYNAME=$(basename $FASTQDIR)

script1=$scriptdir/pear.py
script2=$scriptdir/pipeline_amplicon_pear.py
script3=$scriptdir/npm_var.py

#Copies the fastq files to tmp directory to prepare to start working
mkdir -p $TMPDIR
echo "Copying $FASTQDIR/*.fastq.gz to $TMPDIR"
for file in $(ls $FASTQDIR/*.fastq.gz) ; do
    cp $file $TMPDIR
done

ls $TMPDIR/*.fastq.gz > $TMPDIR/files.txt
cd $TMPDIR

#Gunzips and runs PEAR on the samples
echo "Running: $PYTHON $script1 $TMPDIR/files.txt"
conda run -n NPM1_DeepSeq $script1 $TMPDIR/files.txt

#Does mapping etc
echo "Running: $PYTHON $script2 $TMPDIR"
conda run -n NPM1_DeepSeq $script2 $TMPDIR $REF

# bamfiles.txt is just a file that contains all the sorted bamfile from the previous step.
# $FASTQDIR is used for providing context to the mail attachment in the for of run name
# Email server etc. has to be edited in npm_var.py in order to be used. By default,
# no emails will be sent if no adresses are given
echo "Running: $PYTHON $script3 $TMPDIR/bamfiles.txt $FASTQDIR $EMAILS"
conda run -n NPM1_DeepSeq $script3 $TMPDIR/bamfiles.txt $FASTQDIR $EMAILS

#copy relevant csv file to .. from cwd

echo "Copy loop"
filestocopy=$(ls $TMPDIR | grep ".csv")
for csv in $filestocopy ; do
    echo "Copying $csv to $OUTIDIR"
    cp $csv $OUTDIR
done

echo "Copying single file to outdir"
cp $TMPDIR/NPM1_all_samples.csv $OUTDIR

#remove everything in tmpdir
#rm -rf $TMPDIR

echo "Done at `date` !"
