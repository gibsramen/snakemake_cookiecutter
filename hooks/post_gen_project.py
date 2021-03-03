import os

target_dirs = ["results", "scripts", "data/raw", "data/interim",
               "data/processed", "pbs_out", "rules"]

for d in target_dirs:
    os.makedirs(d)
