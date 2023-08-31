# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
# mytext = 'Welcome to geeksforgeeks!'
#
# # Language in which you want to convert
# language = 'en'
#
# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
#
# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("welcome.mp3")
#
# # Playing the converted file
# os.system("mpg321 welcome.mp3")

import tkinter as tk
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import speedup
from tkinter import ttk


def get_tts_audio(text: str, output_file_path: str = "text.mp3"):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save(output_file_path)

    return output_file_path


def get_text():
    entered_text.set(text_entry.get("1.0", "end-1c"))
    root.quit()


def create_text_window():
    global root, text_entry, entered_text, playback_speed_var

    root = tk.Tk()
    root.title("Paragraph Entry Window")

    label = tk.Label(root, text="Enter your paragraphs with quotations:")
    label.pack()

    text_entry = tk.Text(root, height=10, width=40)
    text_entry.pack()

    entered_text = tk.StringVar()

    label_speed = tk.Label(root, text="Select Playback Speed:")
    label_speed.pack()

    playback_speed_var = tk.DoubleVar()
    playback_speed_var.set(1.0)  # Default playback speed

    playback_speed_dropdown = ttk.Combobox(root, textvariable=playback_speed_var,
                                           values=["1.0", "1.25", "1.5", "1.75", "2.0"])
    playback_speed_dropdown.pack()

    button = tk.Button(root, text="Submit", command=get_text)
    button.pack()

    root.mainloop()

    return entered_text.get(), playback_speed_var.get()


def play_mp3(file_path, playback_speed=1.0):
    """
    Play an MP3 file with adjustable playback speed.

    Args:
        file_path (str): Path to the MP3 file.
        playback_speed (float): Playback speed (1.0 is normal speed).

    Returns:
        None
    """
    audio = AudioSegment.from_mp3(file_path)

    # Adjust the playback speed
    modified_audio = speedup(audio, playback_speed, 150)
    modified_audio.export("text_new.mp3", format="mp3")
    # Play the modified audio
    play(modified_audio)


if __name__ == "__main__":
    entered_text, playback_speed = create_text_window()
    print("Entered Text:")
    print(entered_text)
    print("Playback Speed:")
    print(playback_speed)
    output_file_path = get_tts_audio(entered_text)
    play_mp3(output_file_path, playback_speed=playback_speed)