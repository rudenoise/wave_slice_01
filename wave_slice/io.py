import os
import shutil
import soundfile as sf
import numpy as np


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
