import os
from pydub import AudioSegment
import math
def duration(filePath):
    print("getDuration started")
    os.environ['PATH'] += os.pathsep + '/Users/kroanke/audio-orchestrator-ffmpeg/bin'
    audio = AudioSegment.from_file(filePath)
    duration_in_seconds = math.floor(len(audio) / 60000.0)
    print(f'Duration is {duration_in_seconds} seconds.')
    return duration_in_seconds



