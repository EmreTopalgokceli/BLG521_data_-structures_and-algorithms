################
### Degısken ###
################
x = 5
y = "Merhaba"

del x,y

### Global ve local degisken

x = 5  # Global değişken
def fonksiyon():
    print(x)

def fonksiyon():
    y = 10  # Yerel değişken
    print(y)

def onla_topla(x):
    y = 10
    print (x+y)

onla_topla(5)

y = 10
def onla_topla(x):
    print (x+y)

onla_topla(5)


##########################
### Degısken kuralları ###
##########################


# 1. Değişken Adları Sayı ile Başlamaz
#    - ❌ `2adet_elma = "5 kg"`
#    - ✅ `adet_elma2 = "5 kg"`
2adet_elma = "5 kg"
adet_elma2 = "5 kg"

# 2. Değişken Adları Özel Sembol İçermez (_ Altçizgi Hariç)
#    - ❌ `maaş! = "3000 TL"`
#    - ✅ `maas_miktari = "3000 TL"`
maaş! = "3000 TL"
maas_miktari = "3000 TL"

# 3. Değişken Adlarında Boşluk Olmaz
#    - ❌ `kullanıcı adı = "yönetici"`
#    - ✅ `kullanici_adi = "yönetici"`
kullanıcı adı = "yönetici"
kullanici_adi = "yönetici"

# 4. Değişken Adlarında Bazı Özel Anlam İfade Eden Kelimeler Kullanılmaz
#    - ❌ `False = 10`
#    - ✅ `false_degiskeni = 10`



# Python’da özel anlam ifade eden kelimeleri görmek

import keyword
keyword.kwlist


### Coklu atama ornegı
# Çoklu atama örneği
x = y = z = 10
print("x:", x)
print("y:", y)
print("z:", z)

### Farklı değerler atama
x, y, z = 10, 20, 30
print("x:", x)
print("y:", y)
print("z:", z)



### Degisken takasi
# Değişken takası örneği
x = 5
y = 10

# Değişken takası
x, y = y, x


### Degisken silme
del x, y, z






#####################################################
### Python'da kullanılan matematiksel operatörler ###
#####################################################


2+3
6/2
2**4


# Modül (Kalan) (%)

10 % 3

# Tamsayı Bölme (//)

11//3

# Modul ornek

def kalan_bul(toplam_kisi, kapasite):
    bot_sayisi = toplam_kisi % kapasite
    print(bot_sayisi)


kalan_bul(100000, 259)

def toplam_bot(toplam_kisi, kapasite):
    bot_sayisi = toplam_kisi // kapasite
    print(bot_sayisi)

toplam_bot(100000, 259)


### Ornekler

5==6

5!=6

30==6*5

5<3




##################################
### Python'da Fonksiyon Yazimi ###
##################################

def toplama(a,b):
    return a+b

toplama(3,2)


def toplama2(a,b,c):
    top = a+b
    return top/c

toplama2(3,7,2)

def toplama2(a,b,c):
    return (a+b)/c

toplama2(3,7,2)

def kare_al(a):
    return a**2

kare_al(5)

# return ve print farki: return kullandigimizda fonksiyonun ciktisini baska bir islem icin girdi olarak kullanabiliriz.
kare_al(5)*10
# print kullandigimizda bu sekilde yapamayiz

def kare_al(a):
    print(a**2)

kare_al(4)


##################################
### Python'da if-else yapisi ###
##################################


def sayi_durumu_2(sayi):
    if sayi > 0:
        print('Pozitif'),
    elif sayi < 0:
        print('Negatif'),
    else:
        print('Sifir')


sayi_durumu_2()


## Simdi modul (kalan, %) yapisini kullanarak baska bir if-else fonksiyonu yazalim
def tek_mi_cift_mi(sayi):
    if sayi % 2 == 0:
        return "Çift"
    else:
        return "Tek"

# Fonksiyonu kullanarak bir sayının tek mi yoksa çift mi olduğunu kontrol edelim
tek_mi_cift_mi(7)
tek_mi_cift_mi(10)

# Yukaridakinin ters sekilde yazalim (Yani tek sayilari kontrol etsin)
def tek_mi_cift_mi(sayi):
    if sayi % 2 != 0:
        return "Tek"
    else:
        return "Cift"

# Hava Durumu Kontrolü Fonksiyonu

def hava_durumu_önerisi(sicaklik):
    if sicaklik > 30:
        return "Bugün hava çok sıcak! Plaj zamanı."
    elif sicaklik > 20:
        return "Harika bir hava! Parka gitmek için ideal."
    else:
        return "Hava biraz serin. Bir kazak almayı unutma."

# Örnek kullanım:
hava_durumu_önerisi(31)
hava_durumu_önerisi(25)
hava_durumu_önerisi(15)



# input fonksiyonuyla interactive yapalim


# Hava durumu

def hava_durumu_önerisi():
    sicaklik = int(input("Bugünün sıcaklığını girin (derece olarak): "))

    if sicaklik > 30:
        return "Bugün hava çok sıcak! Plaj zamanı."
    elif sicaklik > 20:
        return "Harika bir hava! Parka gitmek için ideal."
    else:
        return "Hava biraz serin. Bir kazak almayı unutma."



### FOR: for döngüsu her bir elemanı sırayla alır ve belirtilen işlemi yapar.



liste = [1, 2, 3, 4, 5]

# Her bir öğe için döngüyü kullanarak işlem yap
for eleman in liste:
    print(eleman)





liste = [1, 2, 3, 4, 5]

# Her bir öğe için döngüyü kullanarak işlem yap
for eleman in liste:
    kare = eleman ** 2
    print(f"{eleman}'nin karesi: {kare}")



### while - while döngüsü belirli bir koşul sağlandığı sürece çalışır.
# Koşul sağlanmaya devam ettiği sürece döngü de devam eder.

sayac = 0
while sayac < 5:
    print(sayac)
    sayac += 1


### break  ifadesi, bir döngüyü belirli bir koşul gerçekleştiğinde durdurmak için kullanılır.

sayac = 0
while True:
    print(sayac)
    sayac += 1
    if sayac >= 5:
        break


### continue
#Bu döngüde, sayi değişkeni çift olduğunda, yani 2'ye tam bölündüğünde, continue ifadesi sayıyı
# ekrana yazdırmaz ve döngünün bir sonraki iterasyonuna atlar. Bu nedenle, yalnızca
# tek sayılar ekrana yazdırılır.

sayi = 0
while sayi < 10:
    sayi += 1
    if sayi % 2 == 0:
        continue
    print(sayi)
