# CS325-IA2
## Empirical Verification of correctness

To help you debug your program and run the verification your self,
you can use the provided checker.py with the following command:

```python check_cost.py -c <costfilename> -o <outputfilename>```

If no filenames are provided, it will assume a default name for cost file imp2cost.txt and default name for output file imp2output.txt. 

You can further verify if your output correctly matches the optimal cost specified by the provided
solution file with the following command:

```python check_cost.py -c <costfilename> -o <outputfilename> -s <solutionfilename>```

If solutionfilename is not provided, it will only check if the provided cost matches the provided alignment in the outputfile.

## Checklist for code expectation:

* python <your_script_name>.py should generate imp2output.txt when placed in the same folder
with imp2input.txt and imp2cost.txt.

* python check_cost.py passes successfully, indicating no formatting error and the reported costs are
consistent with the provided alignments.
