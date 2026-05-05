import librosa
import numpy as np

# Load the MP3 file
song = librosa.load("/mnt/storage1/Music/UNSORTED/Sanctum-Eddie_Mize.mp3")
y, sr = song
# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
# print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)
# print(beat_times)
onset_env = librosa.onset.onset_strength(y=y, sr=sr)

# tempo = Ilibrosa.beat.tempo(onset_envelope=onset_env, sr=sr)
tempo = librosa.feature.rhythm.tempo(onset_envelope=onset_env, sr=sr)

tempo
exit(0)
# Get the beats per minute
bpm = librosa.beat.tempo(song) #, sr=44100)

# Print the beats per minute
print(bpm)

exit (0)

# Get the beats per minute of each song
bpms = [librosa.beat.tempo(song, sr=44100) for song in songs]

# Find the average beats per minute
avg_bpm = np.mean(bpms)

# Change the tempo of each song to match the average beats per minute
for i, song in enumerate(songs):
    librosa.effects.tempo(song, sr=44100, tempo=avg_bpm)

# Save the modified songs
for i, song in enumerate(songs):
    librosa.output.write_wav(f"modified_song_{i}.wav", song, sr=44100)