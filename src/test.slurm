#!/bin/bash
#SBATCH -e errors_%j.txt
#SBATCH -t 02:30:00
#SBATCH -n 1
#SBATCH -p allgroups


cd ~/Downloads/THZ/repos/QD-realization-modified/src/

srun matlab  < main.m
