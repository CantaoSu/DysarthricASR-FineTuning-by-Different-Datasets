import pandas as pd
import re

# # Path to the training dataset
train_file_path = '/scratch/s4802829/dissertation/ASR-Wav2vec-Finetune/data/by_speaker/SI_high/normal_train.txt'

# # Read the training dataset into a DataFrame
data = pd.read_csv(train_file_path, sep='|')

# Function to check for non-letter characters in the transcript
def check_for_non_letters(transcript):
    non_letters = re.findall(r'[^a-zA-Z\s]', transcript)
    return non_letters

# Apply the function to the transcripts
data['non_letters'] = data['transcript'].apply(check_for_non_letters)

# Filter rows with found non-letter characters
rows_with_non_letters = data[data['non_letters'].apply(lambda x: len(x) > 0)]

# Print the results
for index, row in rows_with_non_letters.iterrows():
    print(f"Path: {row['path']}")
    print(f"Transcript: {row['transcript']}")
    print(f"Found Non-Letter Characters: {row['non_letters']}")
    print()

# Save the results to a new file
rows_with_non_letters.to_csv('/scratch/s4802829/dissertation/TORGO/ALL/non_letters_in_transcripts.csv', index=False)

# import pandas as pd

# Path to the training dataset
# train_file_path = '/path/to/normal_train.txt'

# Characters to check
# unicode_characters = {
#     '\u2013': 'en dash',
#     '\u2014': 'em dash',
#     '\u2018': 'left single quotation mark',
#     '\u201d': 'right double quotation mark'
# }

# # Read the training dataset into a DataFrame
# data = pd.read_csv(train_file_path, sep='|')

# # Function to check for the presence of unicode characters
# def check_for_unicode_characters(transcript):
#     found_characters = []
#     for char, description in unicode_characters.items():
#         if char in transcript:
#             found_characters.append((char, description))
#     return found_characters

# # Apply the function to the transcripts
# data['unicode_characters'] = data['transcript'].apply(check_for_unicode_characters)

# # Filter rows with found unicode characters
# rows_with_unicode = data[data['unicode_characters'].apply(lambda x: len(x) > 0)]

# # Print the results
# for index, row in rows_with_unicode.iterrows():
#     print(f"Path: {row['path']}")
#     print(f"Transcript: {row['transcript']}")
#     print(f"Found Unicode Characters: {row['unicode_characters']}")
#     print()

# # Save the results to a new file
# rows_with_unicode.to_csv('/scratch/s4802829/dissertation/TORGO/ALL/unicode_characters_in_transcripts.csv', index=False)

# import pandas as pd
# import re

# # Path to the training dataset
# train_file_path = '/scratch/s4802829/dissertation/ASR-Wav2vec-Finetune/data/by_speaker/SI_high/normal_train.txt'

# # Read the training dataset into a DataFrame
# data = pd.read_csv(train_file_path, sep='|')

# # Function to check for non-standard characters in the transcript
# def check_for_non_standard_characters(transcript):
#     # Regular expression to find characters that are not letters, digits, or common punctuation
#     non_standard_characters = re.findall(r'[^\w\s.,!?\'\"-]', transcript)
#     return non_standard_characters

# # Apply the function to the transcripts
# data['non_standard_characters'] = data['transcript'].apply(check_for_non_standard_characters)

# # Filter rows with found non-standard characters
# rows_with_non_standard_characters = data[data['non_standard_characters'].apply(lambda x: len(x) > 0)]

# # Print the results
# for index, row in rows_with_non_standard_characters.iterrows():
#     print(f"Path: {row['path']}")
#     print(f"Transcript: {row['transcript']}")
#     print(f"Found Non-Standard Characters: {row['non_standard_characters']}")
#     print()

# # Save the results to a new file
# rows_with_non_standard_characters.to_csv('/scratch/s4802829/dissertation/TORGO/ALL/non_standard_characters_in_transcripts.csv', index=False)