# Completely Offline Speech-to-Text Application using Vosk
# No internet connection required at all
# Install required packages: pip install vosk pyaudio sounddevice

import vosk
import json
import queue
import sounddevice as sd
import threading
import tkinter as tk
from tkinter import scrolledtext, Button, Label, Frame, messagebox
import datetime
import os
import sys

class VoskOfflineSpeechToText:
    def __init__(self):
        self.model_path = None
        self.model = None
        self.recognizer = None
        self.audio_queue = queue.Queue()
        self.is_listening = False
        self.stop_listening = False
        
        # Audio settings
        self.sample_rate = 16000
        self.channels = 1
        
        # Check for Vosk model
        self.check_vosk_model()
        
        # Create GUI
        self.setup_gui()
    
    def check_vosk_model(self):
        """Check if Vosk model is available and download if needed"""
        # Common model paths
        possible_paths = [
            "vosk-model-small-en-us-0.15",
            "vosk-model-en-us-0.22",
            "model"
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                self.model_path = path
                break
        
        if not self.model_path:
            self.show_model_download_dialog()
        else:
            self.load_model()
    
    def show_model_download_dialog(self):
        """Show dialog to download Vosk model"""
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        result = messagebox.askyesno(
            "Vosk Model Required",
            "Vosk speech recognition model not found.\n\n"
            "Would you like to download a small English model (~40MB)?\n\n"
            "This will require an internet connection for the first time only.\n"
            "After download, the app will work completely offline."
        )
        
        if result:
            self.download_model()
        else:
            messagebox.showinfo(
                "Manual Download",
                "You can manually download Vosk models from:\n"
                "https://alphacephei.com/vosk/models\n\n"
                "Download a model and extract it to this directory.\n"
                "Then restart the application."
            )
            sys.exit(0)
        
        root.destroy()
    
    def download_model(self):
        """Download Vosk model"""
        import urllib.request
        import zipfile
        
        model_url = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
        model_filename = "vosk-model-small-en-us-0.15.zip"
        
        try:
            # Show download progress
            progress_root = tk.Tk()
            progress_root.title("Downloading Model")
            progress_root.geometry("400x150")
            progress_root.resizable(False, False)
            
            progress_label = Label(progress_root, text="Downloading Vosk model...\nThis may take a few minutes.", 
                                 font=("Arial", 12), pady=20)
            progress_label.pack()
            
            progress_bar = tk.Canvas(progress_root, width=300, height=20, bg='lightgray')
            progress_bar.pack(pady=10)
            
            def update_progress(block_num, block_size, total_size):
                if total_size > 0:
                    progress = min(block_num * block_size / total_size, 1.0)
                    progress_bar.delete("all")
                    progress_bar.create_rectangle(0, 0, 300 * progress, 20, fill='green')
                    progress_root.update()
            
            # Download the model
            urllib.request.urlretrieve(model_url, model_filename, update_progress)
            
            # Extract the model
            progress_label.config(text="Extracting model...")
            progress_root.update()
            
            with zipfile.ZipFile(model_filename, 'r') as zip_ref:
                zip_ref.extractall(".")
            
            # Clean up
            os.remove(model_filename)
            
            self.model_path = "vosk-model-small-en-us-0.15"
            progress_root.destroy()
            
            # Load the model
            self.load_model()
            
        except Exception as e:
            messagebox.showerror("Download Error", f"Failed to download model: {e}")
            sys.exit(1)
    
    def load_model(self):
        """Load the Vosk model"""
        try:
            self.model = vosk.Model(self.model_path)
            self.recognizer = vosk.KaldiRecognizer(self.model, self.sample_rate)
            print(f"Vosk model loaded from: {self.model_path}")
        except Exception as e:
            messagebox.showerror("Model Error", f"Failed to load Vosk model: {e}")
            sys.exit(1)
    
    def setup_gui(self):
        """Set up the graphical user interface"""
        self.root = tk.Tk()
        self.root.title("Vosk Offline Speech-to-Text")
        self.root.geometry("700x500")
        self.root.configure(bg='#f0f0f0')
        
        # Main frame
        main_frame = Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Title
        title_label = Label(main_frame, text="Vosk Offline Speech-to-Text", 
                           font=("Arial", 18, "bold"), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=(0, 5))
        
        # Subtitle
        subtitle_label = Label(main_frame, text="100% Offline - No Internet Required", 
                              font=("Arial", 10), bg='#f0f0f0', fg='#666')
        subtitle_label.pack(pady=(0, 15))
        
        # Status label
        self.status_label = Label(main_frame, text="Ready to listen", 
                                 font=("Arial", 11), bg='#f0f0f0', fg='#666')
        self.status_label.pack(pady=(0, 10))
        
        # Text area for transcriptions
        text_frame = Frame(main_frame, bg='#f0f0f0')
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        self.text_area = scrolledtext.ScrolledText(text_frame, 
                                                  wrap=tk.WORD, 
                                                  font=("Arial", 12),
                                                  bg='white',
                                                  fg='#333',
                                                  height=18)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Button frame
        button_frame = Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X)
        
        # Start/Stop button
        self.toggle_button = Button(button_frame, 
                                   text="Start Listening", 
                                   command=self.toggle_listening,
                                   font=("Arial", 12, "bold"),
                                   bg='#4CAF50',
                                   fg='white',
                                   relief=tk.FLAT,
                                   padx=25,
                                   pady=8)
        self.toggle_button.pack(side=tk.LEFT, padx=(0, 15))
        
        # Clear button
        clear_button = Button(button_frame, 
                             text="Clear Text", 
                             command=self.clear_text,
                             font=("Arial", 12),
                             bg='#f44336',
                             fg='white',
                             relief=tk.FLAT,
                             padx=20,
                             pady=8)
        clear_button.pack(side=tk.LEFT, padx=(0, 15))
        
        # Save button
        save_button = Button(button_frame, 
                            text="Save to File", 
                            command=self.save_to_file,
                            font=("Arial", 12),
                            bg='#2196F3',
                            fg='white',
                            relief=tk.FLAT,
                            padx=20,
                            pady=8)
        save_button.pack(side=tk.LEFT, padx=(0, 15))
        
        # Model info button
        info_button = Button(button_frame, 
                            text="Model Info", 
                            command=self.show_model_info,
                            font=("Arial", 12),
                            bg='#FF9800',
                            fg='white',
                            relief=tk.FLAT,
                            padx=20,
                            pady=8)
        info_button.pack(side=tk.LEFT)
        
        # Instructions
        instructions = Label(main_frame, 
                            text="Click 'Start Listening' and speak into your microphone.\n"
                                 "The text will appear in real-time. Works completely offline!",
                            font=("Arial", 10), 
                            bg='#f0f0f0', 
                            fg='#888',
                            justify=tk.CENTER)
        instructions.pack(pady=(15, 0))
    
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
        
        # Start audio stream
        self.audio_stream = sd.RawInputStream(
            samplerate=self.sample_rate,
            blocksize=8000,
            device=None,
            dtype='int16',
            channels=self.channels,
            callback=self.audio_callback
        )
        
        self.audio_stream.start()
        
        # Start processing thread
        self.process_thread = threading.Thread(target=self.process_audio)
        self.process_thread.daemon = True
        self.process_thread.start()
    
    def stop_listening_func(self):
        """Stop listening for speech"""
        self.is_listening = False
        self.stop_listening = True
        self.toggle_button.config(text="Start Listening", bg='#4CAF50')
        self.status_label.config(text="Stopped listening")
        
        if hasattr(self, 'audio_stream'):
            self.audio_stream.stop()
            self.audio_stream.close()
    
    def audio_callback(self, indata, frames, time, status):
        """Callback for audio input"""
        if status:
            print(f"Audio callback status: {status}")
        if self.is_listening:
            self.audio_queue.put(bytes(indata))
    
    def process_audio(self):
        """Process audio data from the queue"""
        while self.is_listening and not self.stop_listening:
            try:
                data = self.audio_queue.get(timeout=1)
                
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get('text', '').strip()
                    
                    if text:
                        # Add timestamp
                        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                        formatted_text = f"[{timestamp}] {text}\n"
                        
                        # Update GUI in main thread
                        self.root.after(0, self.add_text, formatted_text)
                        self.status_label.config(text="Speech recognized!")
                
                # Check for partial results
                partial_result = json.loads(self.recognizer.PartialResult())
                partial_text = partial_result.get('partial', '').strip()
                
                if partial_text:
                    self.status_label.config(text=f"Listening: {partial_text}")
                
            except queue.Empty:
                continue
            except Exception as e:
                print(f"Error processing audio: {e}")
                self.status_label.config(text=f"Error: {str(e)}")
    
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
                filename = f"vosk_transcription_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text_content)
                self.status_label.config(text=f"Saved to {filename}")
            else:
                self.status_label.config(text="No text to save")
        except Exception as e:
            self.status_label.config(text=f"Error saving file: {e}")
    
    def show_model_info(self):
        """Show information about the loaded model"""
        if self.model_path:
            info_text = f"Model: {self.model_path}\n"
            info_text += f"Sample Rate: {self.sample_rate} Hz\n"
            info_text += f"Channels: {self.channels}\n"
            info_text += "Status: Loaded and Ready"
            
            messagebox.showinfo("Model Information", info_text)
        else:
            messagebox.showwarning("Model Information", "No model loaded")
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

def main():
    """Main function to run the application"""
    print("Starting Vosk Offline Speech-to-Text Application...")
    print("This application works completely offline!")
    print("Press Ctrl+C to exit.")
    
    try:
        app = VoskOfflineSpeechToText()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Error starting application: {e}")

if __name__ == "__main__":
    main() 