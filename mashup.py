import os

import mido
from mido import MidiFile, MidiTrack

cv1 = MidiFile('new_song.mid', clip=True)
cv3 = MidiFile('adl-piano-midi/Ambient/Chill Lounge/Future Loop Foundation/The Sea and The Sky.mid', clip=True)

del cv1.tracks[4]
del cv1.tracks[4]

cv1.tracks.append(cv3.tracks[4])
cv1.tracks.append(cv3.tracks[5])

cv1.save('mashup.mid')
