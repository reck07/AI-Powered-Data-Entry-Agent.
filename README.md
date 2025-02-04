AI-Powered Data Entry Agent.

This project is an **AI-powered data entry agent** that:
1. Converts **MP3 audio files** to text using speech recognition.
2. Checks and corrects **grammar and spelling mistakes** in the transcribed text.
3. Saves the corrected text into an **Excel file**.

---

Features.
- **Speech-to-Text**: Converts MP3 audio files to text using Google Speech-to-Text.
- **Grammar Checking**: Corrects grammar and spelling mistakes using LanguageTool.
- **Data Export**: Saves the corrected text into an Excel file.
- **Batch Processing**: Can process multiple MP3 files in a folder.
- **User Interface**: Optional web interface using Streamlit.

---

Libraries and Tools Used.
Here’s a list of libraries and tools used in this project:

Core Libraries.
1. SpeechRecognition: For converting speech to text.
   - Installation: `pip install SpeechRecognition`
   - Documentation: [SpeechRecognition Docs](https://pypi.org/project/SpeechRecognition/)

2. LanguageTool: For grammar and spell-checking.
   - Installation: `pip install language-tool-python`
   - Documentation: [LanguageTool Docs](https://pypi.org/project/language-tool-python/)

3. pydub: For converting MP3 files to WAV format.
   - Installation: `pip install pydub`
   - Documentation: [pydub Docs](https://pypi.org/project/pydub/)

4. pandas: For saving data to Excel files.
   - Installation: `pip install pandas`
   - Documentation: [pandas Docs](https://pandas.pydata.org/docs/)

5. openpyxl: For working with Excel files.
   - Installation: `pip install openpyxl`
   - Documentation: [openpyxl Docs](https://openpyxl.readthedocs.io/)

6. ffmpeg: Required for `pydub` to handle MP3 files.
   - Installation:
     - On Ubuntu: `sudo apt install ffmpeg`
     - On macOS: `brew install ffmpeg`
     - On Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html).

Optional Libraries
1. Streamlit: For creating a web interface.
   - Installation: `pip install streamlit`
   - Documentation: [Streamlit Docs](https://docs.streamlit.io/)

2. ffmpeg-python: For advanced audio processing (optional).
   - Installation: `pip install ffmpeg-python`
   - Documentation: [ffmpeg-python Docs](https://pypi.org/project/ffmpeg-python/)

---

Installation.
Step 1: Clone the Repository
1. Open your terminal or command prompt.
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/data-entry-agent.git
   cd data-entry-agent
   ```

Step 2: Set Up a Virtual Environment (Optional but Recommended)
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

Step 3: Install Dependencies
1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

Step 4: Install FFmpeg
1. Install FFmpeg (required for `pydub` to handle MP3 files):
   - On Ubuntu:
     ```bash
     sudo apt install ffmpeg
     ```
   - On macOS:
     ```bash
     brew install ffmpeg
     ```
   - On Windows: Download and install from [ffmpeg.org](https://ffmpeg.org/download.html).

---

Usage

Step 1: Prepare Your Audio Files
1. Place your MP3 files in the `audio/` folder.
   - Example: `audio/test_audio.mp3`

Step 2: Run the Script
1. Run the script:
   ```bash
   python main.py
   ```
2. The script will:
   - Convert the MP3 file to text.
   - Correct grammar and spelling mistakes.
   - Save the corrected text into an Excel file in the `output/` folder.

Step 3: Check the Output
1. Open the `output/` folder to find the Excel file (e.g., `output.xlsx`).
2. The Excel file will contain the corrected text.

---

Optional: Streamlit Web Interface
If you want to use the Streamlit web interface:
1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
2. Open your browser and go to `http://localhost:8501`.
3. Upload an MP3 file and see the results in real-time.

---

Folder Structure
Here’s the folder structure of the project:
```
data-entry-agent/
│
├── audio/                  # Folder for audio files
│   └── test_audio.mp3      # Sample MP3 file for testing
│
├── output/                 # Folder for output files
│   └── output.xlsx         # Output Excel file (will be created by the script)
│
├── main.py                 # Main Python script
│
├── requirements.txt        # File listing dependencies
│
└── README.md               # This file
```

---

Troubleshooting
1. File Not Found Error:
   - Ensure the `audio/` folder exists and contains the MP3 file.
   - Double-check the file path in the script.

2. FFmpeg Not Installed:
   - Install FFmpeg using the instructions above.

3. Streamlit Not Working:
   - Ensure Streamlit is installed: `pip install streamlit`.
   - Check for port conflicts (default port is 8501).

---

Contributing
If you’d like to contribute to this project:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Contact
If you have any questions or need help, feel free to reach out:
- Email: abdulhaseebsagri@gmail.com
- GitHub: https://github.com/reck07

---

Enjoy using the AI-Powered Data Entry Agent!🚀

---

Example `requirements.txt`
Here’s what your `requirements.txt` file should look like:
```
SpeechRecognition==3.10.0
language-tool-python==2.7.0
pydub==0.25.1
pandas==2.0.3
openpyxl==3.1.2
streamlit==1.26.0
ffmpeg-python==0.2.0
