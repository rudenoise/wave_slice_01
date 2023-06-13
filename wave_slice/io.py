import os
import shutil

import librosa
import numpy as np
import soundfile as sf


def read_to_rosa(file_name, sample_rate):
    y, _ = librosa.load(f"./in/{file_name}.wav", sr=sample_rate)
    return y


def fresh_setup():
    try:
        shutil.rmtree("./out")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir("./out")


def write_file(file_name, sound_arrays, sample_rate):
    sf.write(
        f"./out/{file_name}.wav",
        np.concatenate(sound_arrays),
        sample_rate,
        format='wav',
    )
