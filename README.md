
# CLI tool for Computational Biology

	Please read before use!

    Works with python version >= 3.9
    For Linux users only
    Works with `.txt` files only.
    Make the "compute" file executable using linux terminal typing `chmod +x compute` command

## How to use

	Examples:

	`./compute biocli count nucleotide "<path/to/file>"`
	`./compute biocli translate dna-to-rna "<path/to/file>" to_file=True`



## Project layout
``` bst_assignments
   ├── biocli
   │   ├── count.py
   │   ├── pattern.py 
   │   ├── translate.py 
   ├── compute 
   ├── _helper.py
   ├── _errors.py
```

### Contains:

	DNA to RNA sequence translator
	RNA to DNA sequence translator
	Pattern matcher
	Pattern counter
	Nucleotide counter
	Frequency counter

	Sample file added.

Built on top of DynaCLI by BST Labs. [Check it out!](https://github.com/BstLabs/py-dynacli)

