#!/usr/bin/env bash
#SBATCH --job-name=pi_montecarlo
#SBATCH --output=pi.%a.out
#SBATCH --time=00:20:00
#SBATCH --mem=500M
#SBATCH --array=0-3

module load julia

case $SLURM_ARRAY_TASK_ID in
   0)  N=100 ;;
   1)  N=1000  ;;
   2)  N=10000  ;;
   3)  N=100000  ;;
esac

SCRIPT='success = sum(rand(n).^2 + rand(n).^2 .<= 1); print("{\"pi_estimate\": $(4*success/n), \"iterations\": $(n), \"successes\": $(success)}")'

srun julia -e "n=$N;$SCRIPT"
