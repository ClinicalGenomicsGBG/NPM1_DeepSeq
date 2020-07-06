#!/bin/bash -l

#echo "$HOSTNAME"

scriptdir=$(dirname $0)

PYTHON=$(which python)
#script1=/apps/bio/software/NPM1/python/main/pear.py
#script2=/apps/bio/software/NPM1/python/main/pipeline_amplicon_pear.py
#script3=/apps/bio/software/NPM1/python/main/npm_var.py

DATE=$(date +"%Y_%m_%d_%H_%M_%S")

#module load PEAR/0.9.6
#module load fastx/0.0.13
#module load bwa/0.5.9
#module load picard-tools/2.2.4
#module load samtools/1.0

FASTQDIR=$1
OUTDIR=$2
TMPDIR=$OUTDIR/tmp/NPM1_$DATE
#SCRIPTS=/apps/bio/software/NPM1/python/main
#KLINKEM_OUT=/seqstore/remote/share/klinkem01/Djupsekvensering/pipeline_outputs
CSV_SAVELOC=$OUTDIR/csv
#RUNNAME=$3
EMAILS=$3


script1=$scriptdir/pear.py
script2=$scriptdir/pipeline_amplicon_pear.py
script3=$scriptdir/npm_var.py


#Copies the fastq files to tmp directory to prepare to start working
mkdir $TMPDIR
echo "Copying $FASTQDIR/*.fastq.gz to $TMPDIR"
cp $FASTQDIR/*.fastq.gz $TMPDIR
ls $TMPDIR/*.fastq.gz > $TMPDIR/files.txt
cd $TMPDIR

#Gunzips and runs PEAR on the samples
echo "Running: $PYTHON $script1 $TMPDIR/files.txt"
$PYTHON $script1 $TMPDIR/files.txt

#Does mapping etc
echo "Running: $PYTHON $script2 $TMPDIR"
$PYTHON $script2 $TMPDIR


# bamfiles.txt is just a file that contains all the sorted bamfile from the previous step.
# $FASTQDIR is used for providing context to the mail attachment in the for of run name
# Email server etc. has to be edited in npm_var.py in order to be used. By default,
# no emails will be sent if no adresses are given
echo "Running: $PYTHON $script3 $TMPDIR/bamfiles.txt $FASTQDIR $EMAILS"
$PYTHON $script3 $TMPDIR/bamfiles.txt $FASTQDIR $EMAILS

#echo "Copying $TMPDIR/*.sorted.bam* to $KLINKEM_OUT/bam/$RUN"
#cp $TMPDIR/*.sorted.bam* $KLINKEM_OUT/bam/$RUN

#echo "Copying $TMPDIR/*.fastq.gz to $KLINKEM_OUT/fastq/$RUN"
#cp $TMPDIR/*.fastq.gz $KLINKEM_OUT/fastq/$RUN


#This would take all csvs from the analysis. For CLC import this is not needed at the moment
#echo "Copying $TMPDIR/NPM1_*$(date '+%y%m%d').csv to $KLINKEM_OUT/csv ..."
#cp $TMPDIR/NPM1_*$(date '+%y%m%d').csv $KLINKEM_OUT/csv
#echo "Copying $TMPDIR/CLC_*.csv to $CSV_SAVELOC"
#cp $TMPDIR/CLC_*.csv $CSV_SAVELOC


echo "Done at `date` !"
