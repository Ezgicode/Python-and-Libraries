"""
dataseti indir
class ların (target variable) diagnosis ayrılması
2,3 bir subplot çizdirelim
İlk satırda M için scatter ( radius_mean vs texture_mean), hist(radius_mean),plot(radius_mean)
İkinci satırda B için scatter(radius_mean vs texture_mean), hist(radius_mean), plot(radius_mean)
"""

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\ezgii\OneDrive\Masaüstü\breast-cancer-data.csv")

m_data = data[data["diagnosis"] == "M"]
m_data.reset_index(drop = True, inplace = True)

b_data = data[data["diagnosis"] == "B"]
b_data.reset_index(drop = True, inplace = True) 

plt.title("M")

plt.subplot(2,3,1)
plt.scatter(m_data["radius_mean"],m_data["texture_mean"], color = "Pink", label = "ney")
plt.xlabel("Radius Mean")
plt.ylabel("Texture Mean")

plt.subplot(2,3,2)
plt.hist(m_data["radius_mean"])

plt.subplot(2,3,3)
plt.plot(m_data["radius_mean"])

plt.title("B")

plt.subplot(2,3,4)
plt.scatter(b_data["radius_mean"],b_data["texture_mean"])

plt.subplot(2,3,5)
plt.hist(b_data["radius_mean"])

plt.subplot(2,3,6)
plt.plot(b_data["radius_mean"])

plt.tight_layout()
plt.show()
