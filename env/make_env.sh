#! /bin/bash
mamba env create -p env_run -f pipeline_opt.yml
cd env_run/bin/
wget https://github.com/UWPR/Comet/releases/download/v2024.01.0/comet.linux.exe -O comet
sudo chmod +x comet
