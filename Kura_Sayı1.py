
# Listenin içine random adet random sayı yazar sonuçta bu listedeki sayıların arasından random seçer

import random 
import os
import time

s = int(input("Kaç Yarışmacı Olacak : "))
os.system("cls")
#print(" ")

	
zaman = random.randint(3,20)
liste = []

for i in range(zaman):
	yarışmacı = random.randint(1,s)
	liste.append(yarışmacı)
	time.sleep(0.3)
	print("	\n	",yarışmacı)
	time.sleep(1)
	os.system("cls")

liste.reverse() # Bu iki satır en son çıkan numarayı kazanan yapar
s = liste[0]

s = random.choice(liste)

print(" ")
print("----------KAZANAN----------")
time.sleep(3)
print("\n 	    ",s)