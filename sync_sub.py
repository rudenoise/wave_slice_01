from wave_slice.io import fresh_setup, read_to_rosa, write_file
from wave_slice.proc import norm, regularise, separate_at_zero_crossings

sample_rate = 48000

wav_files_dir_path = "./wav_files"
# name the files
bass_file = "2020-06-12-BG"
sub_file = "2020-06-12-SerumSUB"

bass_file = f"{wav_files_dir_path}/in/{bass_file}.wav"
sub_file = f"{wav_files_dir_path}/in/{sub_file}.wav"

# load them using librosa
bass_file = read_to_rosa(bass_file, sample_rate)
sub_file = read_to_rosa(sub_file, sample_rate)

# parcel up into sections, split on zero crossings
bass_sections = separate_at_zero_crossings(bass_file)
sub_sections = separate_at_zero_crossings(sub_file)
