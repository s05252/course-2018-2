import numpy as np

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI",
"ADBE", "ADT"])
print(sap)

sap2d = sap.reshape(2, 4)
print(sap2d)

sap3d = sap.reshape(2, 2, 2)
print(sap3d)

print(sap2d.T) 

print(sap3d.swapaxes(1, 2))