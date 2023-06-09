import os
import shutil

import librosa
import numpy as np
import soundfile as sf


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


def norm(half_periods):
    half_periods_normalised = []

    for hp in half_periods:
        print(f"{len(hp)=} {int(hp.sum())=}")
        if sum(hp) != 0:
            half_periods_normalised.append(librosa.util.normalize(hp, axis=0))
    return half_periods_normalised


def max_len(hps):
    maximum = 0
    for hp in hps:
        if maximum <= len(hp):
            maximum = len(hp)
    return maximum


def regularise(half_periods):
    half_periods_regularised = []

    maximum = max_len(half_periods)

    print(f"{maximum=}")

    for hp in half_periods:
        length = len(hp)
        if sum(hp) != 0:
            half_periods_regularised.append(
                librosa.resample(
                    hp,
                    orig_sr=length,
                    target_sr=maximum,
                ),
            )
    return half_periods_regularised


def separate_at_zero_crossings(file_name, sample_rate):
    y, _ = librosa.load(f"{file_name}.wav", sr=sample_rate)

    print(f"{y.shape=}")

    zero_crossings = librosa.zero_crossings(y)

    print(f"total zero crossings: {zero_crossings.sum()}")

    half_periods = np.split(y, zero_crossings.nonzero()[0])
    return half_periods


sample_rate = 48000
file_name = "p2-kick"

print("hello testing...")

fresh_setup()

half_periods = separate_at_zero_crossings(file_name, sample_rate)

half_periods_normalised = norm(half_periods)
write_file(f"{file_name}_normalised", half_periods_normalised, sample_rate)

print(f"{np.concatenate(half_periods).shape=}")
print(f"{np.concatenate(half_periods_normalised).shape=}")

half_periods_regularised = regularise(half_periods)

write_file(f"{file_name}_regularised", half_periods_regularised, sample_rate)
