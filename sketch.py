from wave_slice.io import fresh_setup, write_file
from wave_slice.proc import separate_at_zero_crossings, norm, regularise


sample_rate = 48000
file_name = "edward"

print("hello testing...")

fresh_setup()

half_periods = separate_at_zero_crossings(file_name, sample_rate)

half_periods_normalised = norm(half_periods)

write_file(f"{file_name}_normalised", half_periods_normalised, sample_rate)

half_periods_regularised = regularise(half_periods)

write_file(f"{file_name}_regularised", half_periods_regularised, sample_rate)

write_file(f"{file_name}_reg_n_norm", norm(half_periods_regularised), sample_rate)
