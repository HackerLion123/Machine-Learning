import subprocess


import cmu_sphinx as trans

audio_url = 'www.freesoundvault.com/sounds/sound_fx/hb17.wav'

#video_url = ''

transcriber = trans.Transcriber(audio_url)

for line in transcriber.transcript_stream():

	print(line)