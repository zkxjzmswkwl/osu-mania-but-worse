import sys
import tempfile
import requests
from pydub import AudioSegment

mp3 = sys.argv[1]
ogg = sys.argv[2]

f = tempfile.NamedTemporaryFile(delete=False)

with open(mp3, 'rb') as mp3_bytes:
    f.write(mp3_bytes.read())
    AudioSegment.from_mp3(f.name).export(ogg, format='ogg')
    f.close()
