import numpy as np


def txt2jpg(txt_path):
  with open(txt_path) as file:
    lines = file.readlines()

  array = []
  for line in lines:
    replaced_line = line.replace(',', '.')
    splitted_line = replaced_line.split()
    spplitted_line = [float(x) for x in splitted_line]
    array.append(spplitted_line)

  array = array - np.min(np.min(array))
  array = np.array(array) * 255 / np.max(np.max(array))
  array = np.ceil(array)

  return array.astype(int)


