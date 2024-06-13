# Laboratory of Evolutionary genomics and Paleogenomics

## The collection of scripts used in the projects

  * [alignment-statistics.py](../blob/main/alignment-statistics.py) can be used to get average, median, min and max length and average gap content of a series of fasta multiple alignment files (i.e. collection of orthologs). It also can draw a distribution plot of sequence lengths.
  * [check_monophyly.py](../blob/main/check_monophyly.py) is used to check clades in the newick tree for monophyly and create a table with the results for each treefile and every clade
  * [parse-rad1-m-ete.py](../blob/main/parse-rad1-m-ete.py) is a parser for an output from ete3 evol tool for testing evolutionary hypotheses
  * [root_tree.py](../blob/main/root_tree.py) can root the collection of tree files on a specific node
  * [to_ultrametric_tree.py](../blob/main/to_ultrametric_tree.py) can convert multiple tree files to ultrametric trees (for example, for further plotting in Densitree)
  * [tree-to-file.py](../blob/main/tree-to-file.py) is used to create an input file to RERconverge tool. It can read multiple tree files and than write filename and the tree in newick format to a txt file
