#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Selamat datang di kalkulator perhitungan luas dan volume!")
print("Pilih opsi yang akan anda gunakan:")
print("1. Menghitung luas 2 dimensi")
print("2. Menghitung volume 3 dimensi")

pilihan = input("Masukkan pilihan Anda (1 atau 2): ")

if pilihan == "1":
    print("Pilih bentuk 2 dimensi yang ingin dihitung:")
    print("1. Persegi")
    print("2. Persegi panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar genjang")
    print("6. Trapesium")

    bentuk = input("Masukkan pilihan Anda (1-6): ")

    if bentuk == "1":
        sisi = float(input("Masukkan panjang sisi: "))
        luas = sisi * sisi
        print("Luas persegi adalah:", luas)
    elif bentuk == "2":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = panjang * lebar
        print("Luas persegi panjang adalah:", luas)
    elif bentuk == "3":
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga adalah:", luas)
    elif bentuk == "4":
        jari_jari = float(input("Masukkan jari-jari: "))
        luas = 3.14 * jari_jari**2
        print("Luas lingkaran adalah: ", luas)
    elif bentuk == "5":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = alas * tinggi
        print("Luas jajar genjang adalah: ", luas)
    elif bentuk == "6":
        sisi_a = float(input("Masukkan sisi A: "))
        sisi_b = float(input("Masukkan sisi B: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 0.5 * (sisi_a + sisi_b) * tinggi
        print("Luas trapesium adalah: ", luas)
    else:
        print("Maaf, bentuk tidak dikenal.")
        
elif pilihan == "2":
    print("Pilih bentuk 3 dimensi yang ingin dihitung:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Limas")
    print("6. Prisma")

    bentuk = input("Masukkan pilihan Anda (1-6): ")
    
if bentuk == "1":
        sisi = float(input("Masukkan panjang sisi: "))
        volume = sisi**3
        print("Volume kubus adalah: ", volume)
elif bentuk == "2":
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        volume = panjang * lebar * tinggi
        print("Volume balok dengan panjang", panjang, ", lebar", lebar, ", dan tinggi", tinggi, "adalah", volume)
elif bentuk == "3":
        jari_jari = float(input("Masukkan jari-jari tabung: "))
        tinggi = float(input("Masukkan tinggi tabung: "))
        volume = math.pi * jari_jari ** 2 * tinggi
        print("Volume tabung dengan jari-jari", jari_jari, "dan tinggi", tinggi, "adalah", volume)
elif bentuk == "4":
        jari_jari = float(input("Masukkan jari-jari kerucut: "))
        tinggi = float(input("Masukkan tinggi kerucut: "))
        volume = 1/3 * math.pi * jari_jari ** 2 * tinggi
        print("Volume kerucut dengan jari-jari", jari_jari, "dan tinggi", tinggi, "adalah", volume)
elif bentuk == "5":
        alas = float(input("Masukkan luas alas limas: "))
        tinggi = float(input("Masukkan tinggi limas: "))
        volume = 1/3 * alas * tinggi
        print("Volume limas dengan luas alas", alas, "dan tinggi", tinggi, "adalah", volume)
elif bentuk == "6":
        alas = float(input("Masukkan alas segitiga prisma: "))
        tinggi = float(input("Masukkan tinggi segitiga prisma: "))
        tinggi_prisma = float(input("Masukkan tinggi prisma: "))
        volume = 1/2 * alas * tinggi * tinggi_prisma
        print("Volume prisma segitiga dengan alas", alas, ", tinggi", tinggi, ", dan tinggi prisma", tinggi_prisma, "adalah", volume)
else:
    print("Bentuk tidak dikenali.")


# In[ ]:




