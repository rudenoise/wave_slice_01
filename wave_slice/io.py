import os
import shutil

import librosa
import numpy as np
import soundfile as sf


def read_to_rosa(file_path, sample_rate):
    y, _ = librosa.load(file_path, sr=sample_rate)
    return y


def fresh_setup(wave_files_path):
    try:
        shutil.rmtree(f"{wave_files_path}/out")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(f"{wave_files_path}/out")


def write_file(file_path, sound_arrays, sample_rate):
    sf.write(
        file_path,
        np.concatenate(sound_arrays),
        sample_rate,
        format='wav',
    )
