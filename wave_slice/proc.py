import librosa
import numpy as np


def norm(half_periods):
    half_periods_normalised = []

    for hp in half_periods:
        if sum(hp) != 0:
            half_periods_normalised.append(librosa.util.normalize(hp, axis=0))
    return half_periods_normalised


def max_len(hps):
    all = [len(hp) for hp in hps]
    return int(sum(all) / len(all))


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

    zero_crossings = librosa.zero_crossings(y)

    print(f"total zero crossings: {zero_crossings.sum()}")

    half_periods = np.split(y, zero_crossings.nonzero()[0])
    return half_periods
