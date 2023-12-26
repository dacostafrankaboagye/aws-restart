'''
Owner: Frank Aboagye
Generate using : Chatgpt 3.5
'''
# import re
# # Define the input and output file names
# input_file_name = 'preproinsulin-seq.txt'
# output_file_name = 'cleaned_insulin.txt'

# # Read the content of the input file
# print("performing read....")
# with open(input_file_name, 'r') as input_file:
#     content = input_file.read()


# # Use regular expressions to clean up the content
# print("clearning the data....")
# cleaned_content = re.sub(r'ORIGIN|\d+|//|\s+|\n|\r', '', content)


# # Write the cleaned content to the output file
# print("writing to output file....")
# with open(output_file_name, 'w') as output_file:
#     output_file.write(cleaned_content)

# # Confirm programmatically that the file has 110 characters
# file_length = len(cleaned_content)
# print(f"The cleaned file has {file_length} characters.")

import re

# Define the input and output file names
input_file_name = 'preproinsulin-seq.txt'
output_file_prefix = 'insulin-seq-clean'

# Read the content of the input file
with open(input_file_name, 'r') as input_file:
    content = input_file.read()

# Use regular expressions to clean up the content
cleaned_content = re.sub(r'ORIGIN|\d+|//|\s+|\n|\r', '', content)

# Create separate files for different amino acid ranges
ranges = [(1, 24, 'ls'), (25, 54, 'b'), (55, 89, 'c'), (90, 110, 'a')]

for start, end, prefix in ranges:
    # Extract the specified amino acid range
    amino_acids_range = cleaned_content[start - 1:end]

    # Define the output file name
    output_file_name = f'{output_file_prefix}-{prefix}insulin-seq-clean.txt'

    # Write the extracted content to the output file
    with open(output_file_name, 'w') as output_file:
        output_file.write(amino_acids_range)

    # Verify the length of the created file
    file_length = len(amino_acids_range)
    print(f"The file {output_file_name} has {file_length} characters.")
