import dendropy
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--newick", help = "Path to the input .json file to read mutations from")
parser.add_argument("-o", "--output", help = "Path to output the mutations file")
parser.add_argument("-r", "--root", help = "Type of mutation to find, use nuc")
args = parser.parse_args()

def preorder_traversal_paths(node, path, paths):
    if node.is_leaf():
        paths.append(path + [node.taxon.label])
    else:
        path.append(node.taxon.label)
        for child in node.child_nodes():
            preorder_traversal_paths(child, path, paths)
        path.pop()

def print_preorder_traversal_paths(newick_file):
    # Load the tree from the Newick file
    tree = dendropy.Tree.get(
        path=newick_file,
        schema="newick",
        label=None,
        taxon_namespace=None,
        collection_offset=None,
        tree_offset=None,
        rooting="default-rooted",
        edge_length_type=float,
        suppress_edge_lengths=False,
        extract_comment_metadata=True,
        store_tree_weights=False,
        finish_node_fn=None,
        case_sensitive_taxon_labels=False,
        preserve_underscores=False,
        suppress_internal_node_taxa=False,
        suppress_leaf_node_taxa=False,
        terminating_semicolon_required=True,
        ignore_unrecognized_keyword_arguments=False)

    root_node = tree.find_node_with_taxon_label(node_label)
    tree.reroot_at_node(root_node)
    # Get the root node and perform preorder traversal to get all paths
    root = tree.seed_node
    paths = []
    preorder_traversal_paths(root, [], paths)

    output_file = open(args.output, 'w')
    # Print the paths
    for path in paths:
        print(", ".join(path), file = output_file)

node_label = args.root
newick_file = args.newick
print_preorder_traversal_paths(newick_file)
