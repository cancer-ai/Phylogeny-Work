from pathlib import Path
import os
import json
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help = "Path to the input .json file to read mutations from")
parser.add_argument("-o", "--output", help = "Path to output the mutations file")
parser.add_argument("-t", "--type", help = "Type of mutation to find, use nuc")
args = parser.parse_args()

#node_data = json.load(open('/project/mayocancerai/Phylogeny/Output/sequences_238_Output/ancestral_and_238_hcov_sequences.json', 'r'))
data = Path(args.input)
output_file = open(Path(args.output), 'w')
with data.open() as json_file:
  node_data = json.load(json_file)
for name, data in node_data["nodes"].items():
  if args.type=="nuc":
    muts = ",".join(data.get("muts", []))
  else:
    muts = ",".join(data.get("aa_muts", {}).get(args.type, []))
  print(f"{name}\t{muts}", file=output_file)
