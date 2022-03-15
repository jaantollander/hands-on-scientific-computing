#!/usr/bin/env bash
#SBATCH --job-name=hello
#SBATCH --output=result.%J.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:15:00
#SBATCH --mem-per-cpu=300M

module load python

echo "Hello world"
python -c 'import math; print(math.pi)'
