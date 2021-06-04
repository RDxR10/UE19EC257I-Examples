import winsound
import wave
from scipy.io import wavfile
import scipy.fft
#import scipy.fftpack.fftfreq
from scipy.fftpack import fftfreq
import csv
import matplotlib.pyplot as plt
fields = ['No of Channels', 'Sample Width', 'Framerate', 'No of frames', 'Compression Type', 'Compression Name'] 
import numpy as np

with wave.open("sound_f.wav", "rb") as wav_file:    # Open WAV file in read-only mode.
    # Get basic information.
    n_channels = wav_file.getnchannels()      # Number of channels. (1=Mono, 2=Stereo).
    sample_width = wav_file.getsampwidth()    # Sample width in bytes.
    framerate = wav_file.getframerate()       # Frame rate.
    n_frames = wav_file.getnframes()          # Number of frames.
    comp_type = wav_file.getcomptype()        # Compression type (only supports "NONE").
    comp_name = wav_file.getcompname()        # Compression name.

    # Read audio data.
    frames = wav_file.readframes(n_frames)    # Read n_frames new frames.
    #assert len(frames) == sample_width * n_frames

print("No of channels: ", n_channels)
print("Sample Width: ", sample_width)
print("Framerate: ", framerate)
print("No of frames: ", n_frames)
print("Compression Type: ", comp_type)
print("Compression Name: ", comp_name)

rows = [[n_channels, sample_width, framerate, n_frames, comp_type, comp_name]] 
with open('sound_csv.csv', 'w') as f:      
    w = csv.writer(f)
    w.writerow(fields)
    w.writerows(rows)
