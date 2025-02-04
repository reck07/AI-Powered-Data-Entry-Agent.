import speech_recognition as sr
import language_tool_python
import pandas as pd
import os
from pydub import AudioSegment


# Function to convert MP3 to WAV
def convert_mp3_to_wav(mp3_file, wav_file):
    try:
        audio = AudioSegment.from_mp3(mp3_file)  # Load MP3 file
        audio.export(wav_file, format="wav")  # Export as WAV
        print(f"Converted {mp3_file} to {wav_file}")
    except FileNotFoundError:
        print(f"Error: File not found - {mp3_file}")
        raise
    except Exception as e:
        print(f"Error during MP3 to WAV conversion: {e}")
        raise


# Function to transcribe audio to text
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Load the audio file
    try:
        text = recognizer.recognize_google(audio)  # Use Google Speech-to-Text
        return text
    except sr.UnknownValueError:
        return "Error: Audio could not be understood"
    except sr.RequestError:
        return "Error: API request failed"


# Function to check grammar and spelling
def check_grammar(text):
    tool = language_tool_python.LanguageTool(
        'en-US')  # Use English language rules
    matches = tool.check(text)  # Find grammar and spelling mistakes
    corrected_text = tool.correct(text)  # Correct the text
    return corrected_text, matches


# Function to save data to an Excel file
def save_to_spreadsheet(data, filename):
    df = pd.DataFrame(data, columns=["Text"])  # Create a DataFrame
    df.to_excel(filename, index=False)  # Save to Excel
    print(f"Data saved to {filename}")


# Main function to process audio and save corrected text
def process_audio_to_data(mp3_file, output_file):
    try:
        # Step 1: Convert MP3 to WAV
        wav_file = os.path.join("audio", "temp.wav")  # Temporary WAV file
        convert_mp3_to_wav(mp3_file, wav_file)

        # Step 2: Transcribe audio
        text = transcribe_audio(wav_file)
        print("Transcribed Text:", text)

        # Step 3: Check grammar
        corrected_text, matches = check_grammar(text)
        print("Corrected Text:", corrected_text)

        # Step 4: Save to spreadsheet
        data = {"Text": [corrected_text]}
        save_to_spreadsheet(data, output_file)

        # Step 5: Clean up temporary WAV file
        os.remove(wav_file)
        print(f"Deleted temporary file: {wav_file}")
    except Exception as e:
        print(f"Error during processing: {e}")


# Run the script
if __name__ == '__main__':
    # Define file paths
    audio_folder = "audio"
    output_folder = "output"

    # Ensure folders exist
    os.makedirs(audio_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    mp3_file = os.path.join(audio_folder, "test_audio.mp3")  # Input MP3 file
    output_file = os.path.join(output_folder,
                               "output.xlsx")  # Output Excel file

    # Check if the MP3 file exists
    if not os.path.exists(mp3_file):
        print(f"Error: MP3 file not found at {mp3_file}")
    else:
        # Process the audio and save the results
        process_audio_to_data(mp3_file, output_file)
