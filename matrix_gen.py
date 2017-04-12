import numpy as np
import json

f1 = open("LAXtoNRT.txt", "r") # LAX to NRT
f2 = open("JFKtoLHR.txt", "r") # JFK to LHR

data1 = json.loads(f1.read())
data2 = json.loads(f2.read())

f1.close()
f2.close()

matrix1 = np.matrix(data1)
matrix2 = np.matrix(data2)