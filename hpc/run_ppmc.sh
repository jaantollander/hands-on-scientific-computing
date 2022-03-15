#!/bin/bash
#SBATCH --job-name=run_ppmc
#SBATCH --output=ppmc.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --time=00:05:00
#SBATCH --mem=2G

module load anaconda

export OMP_PROC_BIND=true
python calc_ppmc.py
