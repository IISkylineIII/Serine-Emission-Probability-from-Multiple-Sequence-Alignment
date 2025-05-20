
alignment = [
    "M--QKCASHLE-AR",
    "MSNL-C-APD-LER",
    "MSAPNCARKYDI-R",
    "MS-SSCADED-IIR",
    "M--TKC-SKLEIDR"
]

column_8 = [seq[7] for seq in alignment if seq[7] != '-']

amino_acid_counts = {}
for amino_acid in column_8:
    if amino_acid in amino_acid_counts:
        amino_acid_counts[amino_acid] += 1
    else:
        amino_acid_counts[amino_acid] = 1

total_amino_acids = len(column_8)

prob_serine = amino_acid_counts.get('S', 0) / total_amino_acids

print(f"The emission probability of serine (S) at position 8 is: {prob_serine:.3f}")
