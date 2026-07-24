# Open Reading Frame (ORF) Prediction using Python

## Overview

This project predicts Open Reading Frames (ORFs) from a DNA sequence. An Open Reading Frame (ORF) is a DNA sequence that:

- Starts with a Start Codon (ATG)
- Ends with a Stop Codon (TAA, TAG, or TGA)
- Can potentially encode a protein.

## Features

- Reads DNA sequence from user
- Finds all possible ORFs
- Prints

  - Start position
  - Stop position
  - Length
  - ORF sequence

## Example

Input

```
ATGAAATTTGGGTAGATGCCCCCTAA
```

Output

```
ORF 1
Start : 1
Stop  : 15
Length: 15 bp

ATGAAATTTGGGTAG

---------------------

ORF 2
Start : 16
Stop  : 27
Length: 12 bp

ATGCCCCCTAA
```

## Author

Snigdha Maiti 
