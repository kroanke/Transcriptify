import subprocess
import os


def mainWav(minute):
    print("wav started")
    for i in range(minute):
        mp3_file = f'output{i}.mp3'
        wav_file = f'output{i}.wav'
        subprocess.run(["/Users/kroanke/audio-orchestrator-ffmpeg/bin/ffmpeg", "-i", mp3_file, wav_file])
        os.remove(mp3_file)
    print("wav ended")
