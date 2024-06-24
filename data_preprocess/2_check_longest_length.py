import pandas as pd
import librosa

# Path to the file
file_path = '/scratch/s4802829/dissertation/ASR-Wav2vec-Finetune/data/by_speaker/SI_high/ref_eval.txt'

# Read the file into a DataFrame
data = pd.read_csv(file_path, sep='|')

# Function to get the duration of an audio file using librosa
def get_audio_duration(file_path):
    audio, sr = librosa.load(file_path, sr=None)
    return librosa.get_duration(y=audio, sr=sr)

# Get the duration for each audio file
data['duration'] = data['path'].apply(get_audio_duration)

# Find the longest audio file
longest_audio = data.loc[data['duration'].idxmax()]

print(f"The longest audio file is {longest_audio['path']} with a duration of {longest_audio['duration']} seconds.")