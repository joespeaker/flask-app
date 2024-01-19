from turtle import speed
from pytube import YouTube
import os
from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile
import slow
import shutil

def download(youtube_link, room_size, wet_level, speed):
  #youtube url
  yt = YouTube(youtube_link)
  video = yt.streams.filter(only_audio=True).first()

  #sets destination as current directory
  destination = '.'
  out_file = video.download(output_path=destination)

  #renames to mp3 from mp4
  new_file =  'song.mp3'
  os.rename(out_file, new_file)



  # Read in a whole audio file:
  with AudioFile("song.mp3", 'r') as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate

  # Make a Pedalboard object, containing multiple plugins:
  board = Pedalboard([
    #values should be 0.8 and 0.1
      Reverb(room_size=room_size, wet_level=wet_level)
      ])

  # Run the audio through this pedalboard!
  effected = board(audio, samplerate)

  # Write the audio back as a wav file:
  with AudioFile('processed-output.wav', 'w', samplerate, effected.shape[0]) as f:
    f.write(effected)

  #value should be 1.2
  slow.stretch('processed-output.wav', speed)

  #delete unprocessed files
  os.remove('song.mp3')
  os.remove('processed-output.wav')

  #move file to folder on desktop
  curr_dir = os.getcwd()
  file_name = yt.title + ".wav"
  static_folder = "static"

  file_path = os.path.join(curr_dir, "stretched.wav")
  destination_path = os.path.join(curr_dir, static_folder, file_name)

  os.makedirs(os.path.join(curr_dir, static_folder), exist_ok=True)
  shutil.move(file_path, destination_path)
  return yt.title
