
import pandas as pd
import matplotlib.pyplot as plt

veri = pd.read_csv(r"C:\Users\ezgii\OneDrive\Masaüstü\iris-1.csv")
veri 
print(veri.columns)

#Bu şekilde yazarsak aynı tabloya iki grafik şeklinde yazar
#plt.plot(veri.PetalLengthCm)
#plt.plot(veri.SepalLengthCm)

#Farklı tablolara yazmasını istiyorsak
plt.figure()
plt.plot(veri.PetalLengthCm)
plt.show()

plt.figure()
plt.plot(veri.SepalLengthCm)
plt.show()


#2 satır 1 sutunluk bir tablo tanımladık ax lerin sıfırıncısı ilk eksen birinci plot
fig, ax = plt.subplots(2,1)

#Ana başlığı suptitle ve figure üzerinden tanımlarız
fig.suptitle("ANA BAŞLIK")

ax[0].plot(veri.SepalLengthCm, color = "pink", label = "SepalLengthCm")
ax[0].set_title("Sepal Length")
ax[0].set_xlabel("index")
ax[0].set_ylabel("Cm")


ax[1].plot(veri.PetalLengthCm, color = "lightblue", label = "PetalLengthCm")
ax[1].set_title("Petal Length")
ax[1].set_xlabel("index")
ax[1].set_ylabel("Cm")

#Otomatik olarak ayarlar alt grafikler (subplot) arasındaki boşluğu otomatik ayarlar
fig.tight_layout()


#Manuel olarak ayarlar
fig.subplots_adjust(top = 0.85)
plt.show()



##Dağılım Grafiği (Scatter)##
#   → 2x2'lik düzenin 1. pozisyonuna grafik ekliyor.
#   → x ve y koordinatları ile dağılım grafiği çiziyor.

plt.figure(figsize=(10, 8))  

plt.subplot(2, 2, 1)  
plt.scatter([1, 2, 3, 4], [5, 6, 7, 8])  
plt.title("Alt Grafik 1")  # Başlık ekle

##Çizgi Grafiği LinePlot ##
#  → x ve y değerlerini bağlayan çizgi grafiği çiziyor
plt.subplot(2, 2, 2)  
plt.plot([1, 2, 3, 4], [8, 7, 6, 5])  
plt.title("Alt Grafik 2")

plt.subplot(2,2,3)
plt.hist([1,2,3,4,5,6,7,8])
plt.title("Alt grafik 3")

plt.subplot(2,2,4)
plt.plot([1,2,3,4],[8,7,6,5])
plt.title("Alt grafik 4")

""""1️⃣ plt.subplot()
Her bir alt grafiği tek tek oluşturur ve manüel yönetim gerektirir.
Her çağrıldığında yeni bir eksen (ax) oluşturur, önceki ekseni silmez.
Basit düzenler için uygundur, ancak büyük ve karmaşık grafiklerde kontrol zorlaşır.
Boşluk yönetimi plt.tight_layout() veya plt.subplots_adjust() ile manuel olarak yapılmalıdır.

2️⃣ plt.subplots()
Tüm alt grafikleri tek seferde oluşturur ve daha düzenli bir yapı sunar.
fig, axes = plt.subplots() yapısı ile eksenlere (axes[row, col]) kolay erişim sağlar.
Geniş ölçekli ve organize grafikler için daha uygundur.
Daha fazla kontrol sunar ve boşluk yönetimi daha kolaydır.
"""

