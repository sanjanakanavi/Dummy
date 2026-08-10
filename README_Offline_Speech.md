# Offline Speech-to-Text Applications

This repository contains three different offline speech-to-text applications that work without requiring external APIs.

## Applications Included

### 1. Simple_Offline_Speech.py
- **Type**: Command-line application
- **Features**: Simple, lightweight, easy to use
- **Internet**: First use may need internet to download models
- **Best for**: Quick testing and simple transcription

### 2. SpeechToText_Offline.py
- **Type**: GUI application with tkinter
- **Features**: User-friendly interface, real-time transcription, save to file
- **Internet**: First use may need internet to download models
- **Best for**: Regular use with nice interface

### 3. SpeechToText_Vosk_Offline.py
- **Type**: GUI application with Vosk
- **Features**: 100% offline, no internet required, real-time transcription
- **Internet**: Completely offline after initial model download
- **Best for**: Privacy-focused users who want complete offline functionality

## Installation

### Prerequisites
- Python 3.7 or higher
- Microphone access
- Windows: No additional setup needed
- Linux: `sudo apt-get install portaudio19-dev`
- macOS: `brew install portaudio`

### Install Python Packages

```bash
# Install all requirements
pip install -r requirements_offline_speech.txt

# Or install individually:
pip install speechrecognition pyaudio
pip install vosk sounddevice
```

## Usage

### Simple Command-Line Version
```bash
python Simple_Offline_Speech.py
```
- Follow the prompts
- Speak when it says "Listening..."
- Choose whether to save transcriptions to file

### GUI Version (Speech Recognition)
```bash
python SpeechToText_Offline.py
```
- Click "Start Listening"
- Speak into your microphone
- Text appears in real-time
- Use buttons to clear text or save to file

### Completely Offline Version (Vosk)
```bash
python SpeechToText_Vosk_Offline.py
```
- First run will download Vosk model (~40MB)
- After download, works completely offline
- Same interface as GUI version but 100% offline

## Features

### All Applications
- ✅ No external API keys required
- ✅ Works offline (after initial setup)
- ✅ Real-time speech recognition
- ✅ Save transcriptions to files
- ✅ Timestamp support

### GUI Applications
- ✅ Modern, user-friendly interface
- ✅ Start/Stop listening controls
- ✅ Clear text functionality
- ✅ Save to file with timestamps
- ✅ Status indicators

### Vosk Version (Completely Offline)
- ✅ 100% offline after model download
- ✅ No internet connection required
- ✅ Privacy-focused
- ✅ Works in air-gapped environments

## Troubleshooting

### Common Issues

1. **"No module named 'pyaudio'"**
   ```bash
   # Windows
   pip install pyaudio
   
   # Linux
   sudo apt-get install portaudio19-dev
   pip install pyaudio
   
   # macOS
   brew install portaudio
   pip install pyaudio
   ```

2. **Microphone not detected**
   - Check microphone permissions in your OS
   - Ensure microphone is not muted
   - Try different microphone if available

3. **Poor recognition accuracy**
   - Speak clearly and at normal volume
   - Reduce background noise
   - Ensure microphone is close to your mouth

4. **Vosk model download fails**
   - Check internet connection
   - Try manual download from https://alphacephei.com/vosk/models
   - Extract model to application directory

### Performance Tips

- Use a good quality microphone
- Minimize background noise
- Speak clearly and at normal pace
- For Vosk version, use the larger model for better accuracy

## Model Information

### Speech Recognition Models
- **Google Speech Recognition**: Used in simple versions, requires internet for first use
- **Vosk Models**: Completely offline, multiple languages available
  - Small model: ~40MB, good for basic recognition
  - Large model: ~1.5GB, better accuracy

### Downloading Additional Vosk Models
Visit https://alphacephei.com/vosk/models for more language models:
- English (various sizes)
- Spanish, French, German, etc.
- Multilingual models

## Privacy and Security

- **No data sent to external servers** (after initial model download)
- **All processing done locally** on your computer
- **No audio recordings stored** (unless you save transcriptions)
- **Vosk version**: Completely private, no internet required

## File Structure

```
├── Simple_Offline_Speech.py          # Command-line version
├── SpeechToText_Offline.py           # GUI version
├── SpeechToText_Vosk_Offline.py      # Completely offline GUI version
├── requirements_offline_speech.txt    # Python dependencies
├── README_Offline_Speech.md          # This file
└── vosk-model-small-en-us-0.15/      # Vosk model (downloaded automatically)
```

## Contributing

Feel free to improve these applications:
- Add support for more languages
- Improve the GUI design
- Add new features like audio recording
- Optimize performance

## License

This project is open source. Use it freely for personal and educational purposes. 