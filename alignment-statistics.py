#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:56:40 2024

@author: gospozha
"""

from Bio import SeqIO
import os
import statistics
import matplotlib.pyplot as plt
import pandas as pd

# Path to the directory containing the FASTA files
fasta_dir = "/home/gospozha/EvoGen/alignments"


# Initialize variables to store total length, min length, max length, and gap counts
total_length = 0
total_gap_count = 0
min_length = float('inf')
max_length = 0
lengths = []

# Iterate through each FASTA file in the directory
for fasta_file in os.listdir(fasta_dir):
    if fasta_file.endswith(".fasta"):  # Ensure the file is a FASTA file
        file_path = os.path.join(fasta_dir, fasta_file)
        with open(file_path, "r") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                seq_length = len(record.seq)
                gap_count = record.seq.count('-') + record.seq.count('?') + record.seq.count('N')
                
                total_length += seq_length
                total_gap_count += gap_count
                min_length = min(min_length, seq_length)
                max_length = max(max_length, seq_length)
                lengths.append(seq_length)

# Calculate the average length and average gap content
average_length = total_length / len(lengths) if lengths else 0
average_gap_content = total_gap_count / total_length if total_length > 0 else 0

# Calculate the median length
median_length = statistics.median(lengths) if lengths else 0

# Print the results
print(f"Average Length: {average_length}")
print(f"Median Length: {median_length}")
print(f"Minimum Length: {min_length}")
print(f"Maximum Length: {max_length}")
print(f"Average Gap Content: {average_gap_content}")

# Plot the distribution of sequence lengths
plt.hist(lengths, bins=30, edgecolor='black')
plt.title('Distribution of Sequence Lengths')
plt.xlabel('Sequence Length')
plt.ylabel('Frequency')
plt.axvline(average_length, color='red', linestyle='dashed', linewidth=1, label=f'Average Length: {average_length:.2f}')
plt.axvline(median_length, color='green', linestyle='dashed', linewidth=1, label=f'Median Length: {median_length:.2f}')
plt.legend()

# Save the plot to the same directory
plot_path = os.path.join(fasta_dir, 'sequence_length_distribution.png')
plt.savefig(plot_path)

# Show the plot
plt.show()

# Path to the directory containing the FASTA files
fasta_dir = "/home/gospozha/EvoGen/align/concat"


# Initialize variables to store total length, min length, max length, and gap counts
total_length = 0
total_gap_count = 0
lengths = []
gap_fractions = []

# Iterate through each FASTA file in the directory
for fasta_file in os.listdir(fasta_dir):
    if fasta_file.endswith(".gb.fasta"):  # Ensure the file is a FASTA file
        file_path = os.path.join(fasta_dir, fasta_file)
        with open(file_path, "r") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                seq_length = len(record.seq)
                gap_count = record.seq.count('-') + record.seq.count('?') + record.seq.count('N')
                gap_fraction = gap_count / seq_length if seq_length > 0 else 0
                total_length += seq_length
                total_gap_count += gap_count
                lengths.append(seq_length)
                gap_fractions.append((record.id, gap_fraction*100))

# Calculate the average length and average gap content
average_length = total_length / len(lengths) if lengths else 0
average_gap_content = total_gap_count / total_length if total_length > 0 else 0

# Print the results
print(f"Length: {average_length}")
print(f"Average Gap Content: {average_gap_content}")

# Create a DataFrame for the gap fractions
gap_fractions_df = pd.DataFrame(gap_fractions, columns=["Sequence ID", "Gap Fraction"])
print(gap_fractions_df)

# Save the DataFrame to the same directory
csv_path = os.path.join(fasta_dir, 'gap_fractions.csv')
gap_fractions_df.to_csv(csv_path, index=False)
