# Serine-Emission-Probability-from-Multiple-Sequence-Alignment

# Description

* This Python script calculates the emission probability of the amino acid serine (S) at the 8th position of a given multiple sequence alignment (MSA). It ignores gaps when computing the frequency.

# Usage
```
# Provided alignment
alignment = [
    "M--QKCASHLE-AR",
    "MSNL-C-APD-LER",
    "MSAPNCARKYDI-R",
    "MS-SSCADED-IIR",
    "M--TKC-SKLEIDR"
]

# Extract the 8th column without gaps
column_8 = [seq[7] for seq in alignment if seq[7] != '-']

# Count amino acid frequencies
amino_acid_counts = {}
for amino_acid in column_8:
    if amino_acid in amino_acid_counts:
        amino_acid_counts[amino_acid] += 1
    else:
        amino_acid_counts[amino_acid] = 1

# Calculate total amino acids (no gaps)
total_amino_acids = len(column_8)

# Calculate serine emission probability at position 8
prob_serine = amino_acid_counts.get('S', 0) / total_amino_acids

print(f"The emission probability of serine (S) at position 8 is: {prob_serine:.3f}")
```
# Example Output

* The emission probability of serine (S) at position 8 is: 0.400

# Applications
* Estimating amino acid emission probabilities in protein sequence alignments.
* Useful for building profile Hidden Markov Models (HMMs) or other probabilistic models of protein families.
* Can assist in bioinformatics analyses such as motif discovery and evolutionary studies.

License
This project is licensed under the MIT License.
