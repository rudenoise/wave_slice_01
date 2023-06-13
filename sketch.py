from wave_slice.io import fresh_setup, read_to_rosa, write_file
from wave_slice.proc import norm, regularise, separate_at_zero_crossings

sample_rate = 48000
file_name = "edward"

print("hello testing...")

fresh_setup()

input_file = read_to_rosa(file_name, sample_rate)

half_periods = separate_at_zero_crossings(input_file)

half_periods_normalised = norm(half_periods)

write_file(f"{file_name}_normalised", half_periods_normalised, sample_rate)

half_periods_regularised = regularise(half_periods)

write_file(f"{file_name}_regularised", half_periods_regularised, sample_rate)

write_file(f"{file_name}_reg_n_norm", norm(half_periods_regularised), sample_rate)
