import numpy as np

choice = int(input("Dataset odd or even what you want? please enter 1 for odd number"
                   "and 2 for even number "))
dataset = np.random.randint(5, 30, 9) if choice == 1 else np.random.randint(5, 30, 10)
print('Dataset is',dataset)

q1 = np.percentile(dataset, 25)
q2 = np.percentile(dataset, 50)
q3 = np.percentile(dataset, 75)
iqr = q3 - q1
print("Q1",q1)
print("Q2",q2)
print("Q3",q3)
print("IQR",iqr)


