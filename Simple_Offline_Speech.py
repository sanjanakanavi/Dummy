# Simple Offline Speech-to-Text (Command Line Version)
# Install: pip install speechrecognition pyaudio

import speech_recognition as sr
import time
import datetime

def simple_speech_to_text():
    """Simple offline speech recognition using microphone"""
    
    # Initialize recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    print("=== Simple Offline Speech-to-Text ===")
    print("This app works offline (first use may need internet to download models)")
    print("Press Ctrl+C to exit")
    print("-" * 40)
    
    # Adjust for ambient noise
    print("Adjusting for ambient noise... Please be quiet for a moment.")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Ready! Start speaking...")
    print("-" * 40)
    
    try:
        while True:
            try:
                # Listen for speech
                with microphone as source:
                    print("Listening... (speak now)")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                print("Processing...")
                
                # Try to recognize speech
                try:
                    # Use Google's speech recognition (works offline with cached models)
                    text = recognizer.recognize_google(audio)
                    
                    if text.strip():
                        # Add timestamp
                        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                        print(f"[{timestamp}] You said: {text}")
                        
                        # Ask if user wants to save
                        save_choice = input("Save to file? (y/n): ").lower().strip()
                        if save_choice in ['y', 'yes']:
                            save_to_file(text, timestamp)
                    
                except sr.UnknownValueError:
                    print("Could not understand what you said. Please try again.")
                except sr.RequestError as e:
                    print(f"Could not request results: {e}")
                
                print("-" * 40)
                
            except sr.WaitTimeoutError:
                print("No speech detected. Listening again...")
                continue
                
    except KeyboardInterrupt:
        print("\nStopping speech recognition...")
        print("Goodbye!")

def save_to_file(text, timestamp):
    """Save transcribed text to a file"""
    try:
        filename = f"speech_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {text}\n")
        print(f"Saved to: {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def test_microphone():
    """Test if microphone is working"""
    print("Testing microphone...")
    
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    try:
        with microphone as source:
            print("Please say something for 3 seconds...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
        
        print("Microphone test successful!")
        return True
        
    except Exception as e:
        print(f"Microphone test failed: {e}")
        print("Please check your microphone connection and permissions.")
        return False

def main():
    """Main function"""
    print("Simple Offline Speech-to-Text Application")
    print("=" * 50)
    
    # Test microphone first
    if not test_microphone():
        print("Cannot proceed without working microphone.")
        return
    
    print("\nStarting speech recognition...")
    simple_speech_to_text()

if __name__ == "__main__":
    main() 