import pandas as pd
import os

# Paths to the input files
train_file_path = '/scratch/s4802829/dissertation/TORGO/ALL/ref_age_healthy_train.txt'
# val_file_path = '/scratch/s4802829/dissertation/TORGO/ALL/ref_val.txt'
# eval_file_path = '/scratch/s4802829/dissertation/TORGO/ALL/ref_eval.txt'

# Directory to save the split files
output_dir = '/scratch/s4802829/dissertation/TORGO/ALL/6_speaker_dependent/by_speaker'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to split data by speakers
def split_by_speaker(file_path, split_name):
    # Read the file into a DataFrame
    data = pd.read_csv(file_path, sep='|')

    # Extract speaker identifier from the file names
    data['speaker'] = data['path'].apply(lambda x: os.path.basename(x).split('_')[0])

    # Group data by speaker and save each group to a separate file
    for speaker, group in data.groupby('speaker'):
        output_file_path = os.path.join(output_dir, f'{split_name}_{speaker}.txt')
        group.drop(columns=['speaker']).to_csv(output_file_path, sep='|', index=False)

# Split each input file by speakers
split_by_speaker(train_file_path, 'train')
# split_by_speaker(val_file_path, 'val')
# split_by_speaker(eval_file_path, 'eval')

print("Splitting complete. Files saved to:", output_dir)