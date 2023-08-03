# Phylogeny-Work
# phylo_tree_paths.py
Contained is a binary tree traveral code that accepts a Newick formatted phylogenetic tree and returns all of the preorder paths starting with the root node. 
Used with the command: python /project/mayocancerai/Phylogeny/Code/phylo_tree_paths.py
The command accepts 3 arguments:
    --newick: Path to the input newick formatted phylogenetic tree
    --root: Root of the phylogenetic tree
    --output: Output path for the traversal paths

# parse_node_data.py
Contained is a code the reads the .json file output by augur ancestral and pulls all of the mutations data. 
Used with the command: python /project/mayocancerai/Phylogeny/Code/parse_node_data.py
The command accepts 3 arguments:
    --input: Path to the input .json file to read mutations from.
    --output: Path to output the mutations to.
    --type: Type of mutations to find. Use nuc.
