# Detect single molecular translocation events from ONT bulk FAST5 files

Contributors: 
- Anastassia Kanavarioti (tessi.kanavarioti@gmail.com)
- Albert Kang (swk30@cam.ac.uk) 

## Run GUI

pip3 install -r requirements.txt 
python3 gui.py

## Example code (CLI)

python3 run.py -i ../../Datasets/minion/20190718_miRNA21_40min_200mV.fast5 > 20190718_miRNA21_40min_200mV.tsv &
python3 run.py -i ../../Datasets/minion/20190718_miRNA21C_40min_200mV.fast5 > 20190718_miRNA21C_40min_200mV.tsv &
python3 run.py -i ../../Datasets/minion/20190719_miRNA21U_40min_200mV.fast5 > 20190719_miRNA21U_40min_200mV.tsv &
python3 run.py -i ../../Datasets/flongle/20190916_A-miRNA21_4h_180mV.fast5 > 20190916_A-miRNA21_4h_180mV.tsv &
python3 run.py -i ../../Datasets/minion/20190918_dT15+A-miRNA21_4h_180mV.fast5 > 20190918_dT15+A-miRNA21_4h_180mV.tsv &
