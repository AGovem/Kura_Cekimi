
# Listeye eklenen değerler arasından random bir satırdaki değeri seçer

import random
import os    
import time

z = random.randint(1,5)
dsy = "Yarışmacı_Listesi.txt"

def temizle():

	dosya = open(dsy,"w")
	dosya.write("")
	dosya.close()
	os.system("cls")

def kontrol():	
	try:
		dosya = open(dsy)
		dosya.close()

	except FileNotFoundError:
		dosya = open(dsy,"w")
		dosya.close()

def liste_goster():
	dosya = open(dsy, "r")
	veri = dosya.read()
	print(veri)
	dosya.close()
	input()

kontrol()

while True:

	os.system("cls")

	print("""
		1) Yarışmacı Ekle
		2) Kura Çek
		3) Liste Temizle
		4) Listeyi Göster

		q) Çıkış
		""")
	
	a = input("İşlem No. : ")
	
	if a == "1":

		i = input("Yarışmacı Adı Girin (Kuraya Geçmek İçin 'd'ye Bas) : ")
		
		dosya = open(dsy,"a")
		dosya.write(i+"\n")
		dosya.close()
		os.system("cls")
		
	elif a == "2":

		os.system("cls")
		dosya = open(dsy,"r")
		b = dosya.readlines()
		yarışmacı = random.choice(b)
		time.sleep(1)
		print("----------KAZANAN----------\n")
		time.sleep(2)
		print("          ",yarışmacı)
		input()
		os.system("cls")

	elif a == "3":
		temizle()

	elif a == "4":
		liste_goster()

	elif a == "q" or a == "Q":
		quit()
