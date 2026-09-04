import mne

# Ruta del EDF
edf_file = r"path"

# Leer archivo
raw = mne.io.read_raw_edf(edf_file, preload=True)
# print(raw.info)

