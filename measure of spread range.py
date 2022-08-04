import numpy as np

dataset = np.random.randint(5, 30, 10)
range = np.max(dataset) - np.min(dataset)
print('Dataset is',dataset)
print('Range is miximum - minimum')
print(f'Range is {np.max(dataset)} - {np.min(dataset)} =',range)