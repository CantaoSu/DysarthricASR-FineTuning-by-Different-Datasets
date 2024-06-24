'''eval.txt'''

# import pandas as pd
# import numpy as np

# # Path to the file
# file_path = '/scratch/s4802829/dissertation/TORGO/ALL/ref_dysarthric_all.txt'

# # Read the file into a DataFrame
# data = pd.read_csv(file_path, sep='|')

# # Get the unique transcripts
# unique_transcripts = data['transcript'].unique()

# # Randomly select 48 unique transcripts
# np.random.seed(42)  # For reproducibility
# selected_transcripts = np.random.choice(unique_transcripts, 48, replace=False)

# # Filter the DataFrame to get rows with the selected transcripts
# eval_data = data[data['transcript'].isin(selected_transcripts)]

# # Save the eval.txt file
# eval_file_path = '/scratch/s4802829/dissertation/TORGO/ALL/eval.txt'
# eval_data.to_csv(eval_file_path, sep='|', index=False)

# # Remove the selected transcripts from the original DataFrame
# remaining_data = data[~data['transcript'].isin(selected_transcripts)]

# # Save the updated ref_dysarthric_all.txt file
# remaining_file_path = 'ref_dysarthric_train_val.txt'
# remaining_data.to_csv(remaining_file_path, sep='|', index=False)

# print(f"eval.txt created with {len(eval_data)} entries.")
# print(f"ref_dysarthric_all.txt updated with {len(remaining_data)} remaining entries.")

'''split train.txt and val.txt'''
# import pandas as pd
# import numpy as np

# # Path to the file
# file_path = '/scratch/s4802829/dissertation/TORGO/ALL/ref_dysarthric_train_val.txt'

# # Read the file into a DataFrame
# data = pd.read_csv(file_path, sep='|')

# # Get the unique transcripts
# unique_transcripts = data['transcript'].unique()

# # Ensure reproducibility
# np.random.seed(42)

# # Randomly select 48 unique transcripts for validation
# val_transcripts = np.random.choice(unique_transcripts, 48, replace=False)

# # Remove the selected validation transcripts from the list of unique transcripts
# remaining_transcripts = np.setdiff1d(unique_transcripts, val_transcripts)

# # Randomly select 393 unique transcripts for training from the remaining transcripts
# train_transcripts = np.random.choice(remaining_transcripts, 393, replace=False)

# # Filter the DataFrame to get rows for training and validation sets
# train_data = data[data['transcript'].isin(train_transcripts)]
# val_data = data[data['transcript'].isin(val_transcripts)]

# # Save the train.txt file
# train_file_path = '/scratch/s4802829/dissertation/TORGO/ALL/ref_dysarthric_train.txt'
# train_data.to_csv(train_file_path, sep='|', index=False)

# # Save the val.txt file
# val_file_path = '/scratch/s4802829/dissertation/TORGO/ALL/ref_val.txt'
# val_data.to_csv(val_file_path, sep='|', index=False)

# print(f"train.txt created with {len(train_data)} entries.")
# print(f"val.txt created with {len(val_data)} entries.")

import pandas as pd

# Define file paths
ref_val_path = '/scratch/s4802829/dissertation/TORGO/ALL/ref_val.txt'
ref_eval_path = '/scratch/s4802829/dissertation/TORGO/ALL/ref_eval.txt'
ref_age_healthy_all_path = '/scratch/s4802829/dissertation/TORGO/ALL/ref_age_healthy_all.txt'

# Read the val and eval files
val_data = pd.read_csv(ref_val_path, sep='|')
eval_data = pd.read_csv(ref_eval_path, sep='|')

# Combine transcripts from val and eval files
combined_transcripts = set(val_data['transcript']).union(set(eval_data['transcript']))

# Read the ref_age_healthy_all file
ref_age_healthy_all_data = pd.read_csv(ref_age_healthy_all_path, sep='|')

# Filter out the lines with the same transcripts as in val and eval files
filtered_data = ref_age_healthy_all_data[~ref_age_healthy_all_data['transcript'].isin(combined_transcripts)]

# Save the updated ref_age_healthy_all.txt file
filtered_data.to_csv(ref_age_healthy_all_path, sep='|', index=False)

print(f"Updated ref_age_healthy_all.txt with {len(filtered_data)} entries.")
