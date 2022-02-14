
# CLI tool for Computational Biology

	Please read before use!

    Works with python version >= 3.9
    For Linux users only
    Works with `.txt` files only.
    Install requirements via pip3.
    Make the "compute" file executable using linux terminal typing `chmod +x compute` command

## How to use

	Examples:
```
	`$ ./compute biocli -h`
    usage: compute biocli [-h] {count,pattern,translate}
    
    positional arguments:
        {count,pattern,translate}
          count                    Count feature to count the nucleotides and patterns in the given DNA or RNA sequence.
          pattern                  Pattern feature for finding given pattern in the given DNA or RNA sequence.
          translate                Translate feature to translate the given DNA sequence to RNA and vice versa.

    optional arguments:
        -h, --help                 show this help message and exit


	`$ ./compute biocli translate dna-to-rna "sample.txt" to_file=False`
    RNA -- UGCUCCGCCGAACCAUUCAUGCGGGAUACGACUUGGAUGACAUAGGAAAUUCAUAAUUAUCGUGUCUAAGUAAUUGCAUGCAGGCUGCAAUAACGUUGUUGGCCGAGCGUAAUACAAGAUUAGCCGCUGUUGAUGCUCAUUAGACGCGUUGGUAAAUUUGACGUUCUUAUGACCCCUACGUAUAACAGAAUAGCCUCUGGUGACUUUUCUGAGCACCGAUCUCGCAAUAUAUUAGCCACUAUAUUAUCUAAGCCGAGCCAAUCAUUGAUACACAUAGUAAUGUCAGGACGUCGAACCUAGAUUGUAUGACUCCGCUAAGGUAUUCCGAGAGACACUAGGAUACUAGAUAUAUUCCCAAAGUAAGGCGACGCCUAGUCUUUAGAGAGCGAGUAUGCCUUUGCCAAGUGUUGGAUGAGCCCGCCCCUUAAUAGGUGCUACGCUAGAGGCAAAGCAUGUGGGCGGUGGCCACACUUCAAUCAGGUGGCGAGUAGACGCUUCAGCCCGUUCGAUCUUAAGUAUCAGUAUAGGGACUCGAGUACAGUGUCCAAAUUACUGCGCUCGGUCCUAUGCUGACAAGGCGAACUCUGCAGAGAAUGGUCCGAAUUCACAUUCGGACAAUACGAUGUAGGACCGAACAAGCACAGUUUGAUUCGCCUCGGAAGACGGUGCAACUGAAACAGUAGAUCUCCUUAUCAAUGUAGGGCGAAGUACUGCCCGCGUGAGGGCACCAGCAUCCAGUCUCGUUGCUGUUCGUAUGGGGAUCAACGGCGGGUUGUUCUUAAGAACAUCAGGAUGAGUUAAUCGAGAGUACUGAACCGCUAUUCGACACCGCAGGUUGCGACACCAAAUUGCCUAAACAUCAACAGCCUCAAUUACCUGCUGUCCACUCGAGCUUGGGGUACAGUGUUAUCCUUCACUUGAACGACAAGAUAAUGAACAUUGUGGACUUGCGUAUA
```


## Project layout
``` 
├── bst_assignment
   ├── biocli
   │   ├── count.py
   │   ├── pattern.py 
   │   ├── translate.py 
   │   ├── _helper.py
   │   ├── _errors.py
   │   ├── __init__.py
   ├── compute 

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

