from moviepy.editor import AudioFileClip
import os

def trim_audio(input_file, output_file, start_time, end_time):
    audio = AudioFileClip(input_file)
    trimmed_audio = audio.subclip(start_time, end_time)
    trimmed_audio.write_audiofile(output_file)

def mainTrim(minute,input_file):
    print("trim started")
    start_time = 0
    end_time = 60
    for i in range(minute):
        output_file = f'output{i}.mp3'
        trim_audio(input_file, output_file, start_time, end_time)
        start_time += 60 
        end_time += 60
    print("trim ended")

