from wave_slice.io import fresh_setup, read_to_rosa, write_file
from wave_slice.proc import norm, regularise, separate_at_zero_crossings

sample_rate = 48000
wav_files_dir_path = "./wav_files"
file_name = "edward"
file_path = f"{wav_files_dir_path}/in/{file_name}.wav"

print("hello testing...")

fresh_setup(wav_files_dir_path)

input_file = read_to_rosa(file_path, sample_rate)

half_periods = separate_at_zero_crossings(input_file)

half_periods_normalised = norm(half_periods)

write_file(
    f"{wav_files_dir_path}/out/{file_name}_normalised.wav",
    half_periods_normalised,
    sample_rate,
)

half_periods_regularised = regularise(half_periods)

write_file(
    f"{wav_files_dir_path}/out/{file_name}_regularised.wav",
    half_periods_regularised,
    sample_rate,
)

write_file(
    f"{wav_files_dir_path}/out/{file_name}_reg_n_norm.wav",
    norm(half_periods_regularised),
    sample_rate,
)
