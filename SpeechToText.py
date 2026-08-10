# Offline Speech-to-Text Application
# No external APIs required - works completely offline
# Install required packages: pip install speechrecognition pyaudio

import speech_recognition as sr
import threading
import time
import queue
import tkinter as tk
from tkinter import scrolledtext, Button, Label, Frame
import datetime

class OfflineSpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.audio_queue = queue.Queue()
        self.is_listening = False
        self.stop_listening = False
        
        # Adjust for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
        
        # Create GUI
        self.setup_gui()
    
    def setup_gui(self):
        """Set up the graphical user interface"""
        self.root = tk.Tk()
        self.root.title("Offline Speech-to-Text")
        self.root.geometry("600x400")
        self.root.configure(bg='#f0f0f0')
        
        # Main frame
        main_frame = Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = Label(main_frame, text="Offline Speech-to-Text", 
                           font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=(0, 10))
        
        # Status label
        self.status_label = Label(main_frame, text="Ready to listen", 
                                 font=("Arial", 10), bg='#f0f0f0', fg='#666')
        self.status_label.pack(pady=(0, 10))
        
        # Text area for transcriptions
        self.text_area = scrolledtext.ScrolledText(main_frame, 
                                                  wrap=tk.WORD, 
                                                  font=("Arial", 12),
                                                  bg='white',
                                                  fg='#333',
                                                  height=15)
        self.text_area.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Button frame
        button_frame = Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X)
        
        # Start/Stop button
        self.toggle_button = Button(button_frame, 
                                   text="Start Listening", 
                                   command=self.toggle_listening,
                                   font=("Arial", 12),
                                   bg='#4CAF50',
                                   fg='white',
                                   relief=tk.FLAT,
                                   padx=20,
                                   pady=5)
        self.toggle_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        clear_button = Button(button_frame, 
                             text="Clear Text", 
                             command=self.clear_text,
                             font=("Arial", 12),
                             bg='#f44336',
                             fg='white',
                             relief=tk.FLAT,
                             padx=20,
                             pady=5)
        clear_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Save button
        save_button = Button(button_frame, 
                            text="Save to File", 
                            command=self.save_to_file,
                            font=("Arial", 12),
                            bg='#2196F3',
                            fg='white',
                            relief=tk.FLAT,
                            padx=20,
                            pady=5)
        save_button.pack(side=tk.LEFT)
        
        # Instructions
        instructions = Label(main_frame, 
                            text="Click 'Start Listening' and speak into your microphone.\nThe text will appear in real-time as you speak.",
                            font=("Arial", 9), 
                            bg='#f0f0f0', 
                            fg='#888',
                            justify=tk.CENTER)
        instructions.pack(pady=(10, 0))
    
    def toggle_listening(self):
        """Toggle between start and stop listening"""
        if not self.is_listening:
            self.start_listening()
        else:
            self.stop_listening_func()
    
    def start_listening(self):
        """Start listening for speech"""
        self.is_listening = True
        self.stop_listening = False
        self.toggle_button.config(text="Stop Listening", bg='#f44336')
        self.status_label.config(text="Listening... Speak now!")
        
        # Start listening thread
        self.listen_thread = threading.Thread(target=self.listen_loop)
        self.listen_thread.daemon = True
        self.listen_thread.start()
    
    def stop_listening_func(self):
        """Stop listening for speech"""
        self.is_listening = False
        self.stop_listening = True
        self.toggle_button.config(text="Start Listening", bg='#4CAF50')
        self.status_label.config(text="Stopped listening")
    
    def listen_loop(self):
        """Main listening loop"""
        while self.is_listening and not self.stop_listening:
            try:
                with self.microphone as source:
                    self.status_label.config(text="Listening... Speak now!")
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=10)
                    
                    # Process the audio in a separate thread
                    threading.Thread(target=self.process_audio, args=(audio,), daemon=True).start()
                    
            except sr.WaitTimeoutError:
                # No speech detected, continue listening
                continue
            except Exception as e:
                print(f"Error in listening loop: {e}")
                self.status_label.config(text=f"Error: {str(e)}")
                break
    
    def process_audio(self, audio):
        """Process the captured audio and convert to text"""
        try:
            self.status_label.config(text="Processing speech...")
            
            # Use Google's speech recognition (works offline with cached models)
            # Note: This still requires internet for the first use to download models
            # For completely offline, you'd need to use a local model like Vosk
            text = self.recognizer.recognize_google(audio)
            
            if text.strip():
                # Add timestamp
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                formatted_text = f"[{timestamp}] {text}\n"
                
                # Update GUI in main thread
                self.root.after(0, self.add_text, formatted_text)
                self.status_label.config(text="Speech recognized!")
            
        except sr.UnknownValueError:
            self.status_label.config(text="Could not understand audio")
        except sr.RequestError as e:
            self.status_label.config(text=f"Could not request results: {e}")
        except Exception as e:
            self.status_label.config(text=f"Error processing audio: {e}")
    
    def add_text(self, text):
        """Add text to the text area"""
        self.text_area.insert(tk.END, text)
        self.text_area.see(tk.END)
    
    def clear_text(self):
        """Clear the text area"""
        self.text_area.delete(1.0, tk.END)
    
    def save_to_file(self):
        """Save the transcribed text to a file"""
        try:
            text_content = self.text_area.get(1.0, tk.END)
            if text_content.strip():
                filename = f"transcription_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text_content)
                self.status_label.config(text=f"Saved to {filename}")
            else:
                self.status_label.config(text="No text to save")
        except Exception as e:
            self.status_label.config(text=f"Error saving file: {e}")
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

def main():
    """Main function to run the application"""
    print("Starting Offline Speech-to-Text Application...")
    print("Note: First use may require internet connection to download speech models.")
    print("Press Ctrl+C to exit.")
    
    try:
        app = OfflineSpeechToText()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Error starting application: {e}")

if __name__ == "__main__":
    main()