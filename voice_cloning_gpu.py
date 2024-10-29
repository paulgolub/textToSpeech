import os
import pandas as pd
from TTS.api import TTS
import torch

def get_device():
    return 'cuda'

def main():
    # Path to the CSV file
    csv_path = "dataset/metadata.csv"

    # Set the device (GPU if available, otherwise CPU)
    device = get_device()
    print(f"Using: {device}")

    # Load the pre-trained model for voice cloning
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True)
    tts.to(device)

    # Specify the language (e.g., 'en' for Italian)
    language = 'en'

    # Create the output folder if it doesn't exist
    os.makedirs("output_wavs", exist_ok=True)

    # Read the CSV file and process each row
    try:
        df = pd.read_csv(csv_path, delimiter='|', header=None, names=['sample_voice_path', 'text'])
        
        for index, row in df.iterrows():
            sample_voice_path = row['sample_voice_path'].strip()
            text = row['text'].strip()
            output_path = os.path.join("output_wavs", f"cloned_voice_{index}.wav")

            # Check if the sample file exists
            if not os.path.exists(sample_voice_path):
                print(f"File not found: {sample_voice_path}")
                continue

            # Perform voice synthesis with voice cloning from the sample and specify the language
            try:
                tts.tts_to_file(text=text, file_path=output_path, speaker_wav=sample_voice_path, language=language)
                print(f"Audio file saved to: {output_path}")
            except Exception as e:
                print(f"Error during text synthesis: {e}")

    except Exception as e:
        print(f"Error reading the CSV: {e}")

if __name__ == "__main__":
    main()
