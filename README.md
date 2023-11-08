# CSCI-5502-Final-Report

The final project for CSCI 5502: Data Mining

[Source Code README](https://github.com/CUBoulder-DS/CSCI-5502-Final-Report/blob/main/src/README.md)

- How to structure the code you're writing

[Data README](https://github.com/CUBoulder-DS/CSCI-5502-Final-Report/blob/main/data/README.md)

- How to download, setup, use the data (input datasets and output from our own code)

## How to generally do work for the CSCI Quarto project

1.  Install Quarto and `install.packages("rmarkdown")` if you haven't already.
2.  Whenever you do git pull, always rebase: `git pull --rebase`.
3.  ALWAYS keep your git updated, do `git pull` always before any commiting, pushing, branches, etc.
4.  You only need to change/do work on the `.qmd` files in the `quarto-paper` directory
5.  `cd` into the `quarto-paper` folder
6.  Run `quarto render` on the CLI/bash
7.  Do a git pull, commit and push (do force push if needed)

## Directory Structure

- **data/**: This is where the data goes, that is outputted by our code or that we download (that is small enough to fit under the Github limits).
- **CSCI_5502_Final_Report.pdf**: The actual final report paper. Auto-generated whenever `quarto render` is run in the `quarto-paper` directory.
- **quarto-paper/**: Where the Quarto code for the Data Mining report should go.
- **src/**: This is where all code files relating to analysis, data exploration etc go; they DO NOT go in the `quarto-paper` folder in order to keep that clean.
