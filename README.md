# `osbp_detect`

This library has been developed with the objective to detect and report translocations of Osmium-labelled oligonucleotides using Oxford Nanopore devices. 

The algorithm in its current form can also be used for the detection of any small molecule traversing any nanopore.

The CLI/GUI allows for the detection of single unassisted oligonucleotide translocation events from ONT bulk FAST5 files.

## Contributors

- Anastassia Kanavarioti (tessi.kanavarioti@gmail.com)
- Albert Kang (swk30@cam.ac.uk) 

## How it works

Let *y* be an ordered sequence of real values representing a typical time-series obtained from a Nanopore device. 

We largely categorise regions of *y* into one of two states: current from an open channel, Io, where nothing is passing through the Nanopore, and the residual current when some translocation event is taking place, Ir. 

## Run GUI

```python3 gui.py```

## Example CLI

```python3 run.py -i ../../Datasets/minion/20190718_miRNA21_40min_200mV.fast5 > 20190718_miRNA21_40min_200mV.tsv &```
