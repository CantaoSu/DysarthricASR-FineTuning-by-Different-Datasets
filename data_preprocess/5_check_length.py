import pandas as pd
import librosa

# Path to the ref_age_healthy_train.txt file
file_path = '/scratch/s4802829/dissertation/ASR-Wav2vec-Finetune/data/by_speaker/SI_high/age_train_FC03.txt'

# Read the file into a DataFrame
data = pd.read_csv(file_path, sep='|')

# Function to get the duration of an audio file using librosa
def get_audio_duration(file_path):
    audio, sr = librosa.load(file_path, sr=None)
    return librosa.get_duration(y=audio, sr=sr)

# Calculate the duration for each audio file
total_duration = 0
for path in data['path']:
    total_duration += get_audio_duration(path)

# Print the total duration
print(f"The total length of all audio files is {total_duration} seconds.")