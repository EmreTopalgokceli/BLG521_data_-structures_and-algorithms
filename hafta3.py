
## Veri tipleri

123

10.5

'Emre'

a = "Emre"

False
True

type(a)

my_list = [1,3.14,'Python', True]

kapsayici_liste = [1, 'Metin', [1,2], {'adi':'Emre'}]


kapsayici_liste[-1]

del my_list[1:3]

my_list.append(9)
my_list.insert(1,2)
my_list.pop(1)

del my_list[2]

my_list.remove('Python')

yeni_liste = my_list + kapsayici_liste

tekrar_list = my_list * 4


len(tekrar_list)


'11'in tekrar_list



my_list = [1,3.14,'Python', [3,5,6]]

my_list[-1][6]



# List comprehension

seyler = ['Masa', 'sandalye', 'tabak', 'hali']


yeni_seyler = []
for x in seyler:
    if 's' in x:
        yeni_seyler.append(x)


yeni_seyler2 = [x for x in seyler if 's' in x]


sonuc = []
for x in seyler:
    if x != 'hali':
        sonuc.append(x)
    else:
        sonuc.append('Iran halisi')


sonuc2 = [x if x != 'hali' else 'Iran halisi' for x in seyler]



my_dict = {'a':1,
           'b':5,
           'v':2.5}




type(my_dict)

my_dict['b']
my_dict['d'] = 11
my_dict.pop('b')

len(my_dict)

'e' in my_dict


my_dict.keys()
my_dict.values()
my_dict.items()


for i, x in my_dict.items():
    print(i, x)


my_tuple = (1,3.14,'Python', True)

type(my_tuple)

my_tuple[0:2]

len()

4 in my_tuple

my_tuple = (1,3.14,'Python', True, (1,3))


my_tuple = (1,3.14, ['Emre Lokantasi', 'Ali Kebab'])

my_tuple[2][-1] = 'Ali Halicilik'
my_tuple[2][0] = 'AB Optik'



s = {1, 2, 3}

type(s)

s.add(11)


a = set('abracadabra')
b = set('alacazam')


a - b

a | b

a & b

a ^ b


## Uygulama 1 - Stok Yonetimi (sozluk veri yapisi)

urun_stoklari = {
    'masa' : 10,
    'sandalye' : 20,
    'koltuk' : 15,
    'dolap' : 5
}

# Yapilmasi istenenler
# stok_ekle
# stok_cikar
# stok_durumu

def stok_ekle(key, value):
    if key in urun_stoklari:
        urun_stoklari[key] += value
    print(f'{key} icin stok miktari {urun_stoklari[key]} olarak guncellendi.')

def stok_cikar(key, value):
    if key in urun_stoklari and urun_stoklari[key]>= value:
        urun_stoklari[key] -= value
        print(f'{key} icin stok miktari {urun_stoklari[key]} olarak guncellendi.')
    else:
        print(f'{key} stokta yeterli miktarda bulunmamaktadir.')

def stok_durumu(key):
    if key in urun_stoklari:
        print('evet')
    else:
        print('hayir')


# Test işlemleri
stok_ekle('masa', 5)  # masa stok miktarını artır
stok_cikar('sandalye', 75)  # sandalye stok miktarını azalt
stok_durumu('koltuk')  # koltuk stok durumunu kontrol et
stok_durumu('halı')  # halı'nın stok durumunu kontrol et (listede yok)


## f string

'Stoklara son olarak sandalye eklendi.' # Statik

for i in urun_stoklari:
    print(f'Stoklara son olarak {i} eklendi.')

for i, x in urun_stoklari.items():  # Sozluk olursa items()
    print(f'Stoklara son olarak {x} adet {i} eklendi.')

for i, x in urun_stoklari.items():
    x += x**2
    i = i.capitalize()
    print(f'Stoklara son olarak {x} adet {i} eklendi.')


for i, x in urun_stoklari.items():
    x += x**2
    i = i.capitalize()
    if len(i) <=5:
        i = f'{i}_TR'
    print(f'Stoklara son olarak {x} adet {i} eklendi.')



stok_ekle('masa', 5)



# Uygulama 2  - Oy kullanma (set veri yapisi)

# Kullanılmış oy ID'lerini saklamak için boş bir set oluştur
oy_sandigi = set()

def oy_kullan(kimlik_no):
    # Eğer kullanıcı ID'si sette varsa, kullanıcı daha önce oy kullanmış demektir.
    if kimlik_no in oy_sandigi:
        print(f"Kullanıcı {kimlik_no} zaten oy kullanmış.")
    else:
        # Kullanıcı daha önce oy kullanmamışsa, oyu kabul et ve sete ekleyerek kaydet.
        oy_sandigi.add(kimlik_no)
        print(f"Kullanıcı {kimlik_no} için oy kabul edildi.")

# Örnek kullanıcılarla test edelim
oy_kullan(1) # Kullanıcı 1 için oy kabul edildi.
oy_kullan(2) # Kullanıcı 2 için oy kabul edildi.
oy_kullan(1) # Kullanıcı 1 zaten oy kullanmış.
oy_kullan(3) # Kullanıcı 3 için oy kabul edildi.



# bu bir liste olsaydi
oy_sandigi = list()

def oy_kullan(i):
    oy_sandigi.append(i)

oy_kullan(1) # Gordugunuz gibi ayni id ile defalarca iy kullaniliyor

# bu bir set olsaydi

oy_sandigi = set()

def oy_kullan(i):
    oy_sandigi.add(i)

oy_kullan(1)


# Peki bir listeyi de set gibi calisacak sekilde tasarlayamaz miyiz.

oy_sandigi = list()

def oy_kullan(kimlik_no):
    # Eğer kullanıcı ID'si sette varsa, kullanıcı daha önce oy kullanmış demektir.
    if kimlik_no in oy_sandigi:
        print(f"Kullanıcı {kimlik_no} zaten oy kullanmış.")
    else:
        # Kullanıcı daha önce oy kullanmamışsa, oyu kabul et ve sete ekleyerek kaydet.
        oy_sandigi.add(kimlik_no)
        print(f"Kullanıcı {kimlik_no} için oy kabul edildi.")

# Örnek kullanıcılarla test edelim
oy_kullan(1) # Kullanıcı 1 için oy kabul edildi.
oy_kullan(2) # Kullanıcı 2 için oy kabul edildi.
oy_kullan(1) # Kullanıcı 1 zaten oy kullanmış.
oy_kullan(3) # Kullanıcı 3 için oy kabul edildi.




######## Hafta 4 ########
## Stack

word_belgemiz = []


def islem_yap(islem):
    word_belgemiz.append(islem)
    print(word_belgemiz)

#
# def islem_yap(islem):
#     push(islem)
#     print(word_belgemiz)

def geri_al():
    word_belgemiz.pop()
    print(word_belgemiz)


islem_yap('Benim adim')
islem_yap("Emre")

geri_al()


# Yukarida yaptigimiz islemi class yapisi ile yapalim

class Stack:
    def __init__(self):
        self.items = []

    def islem_yap(self, i):
        """Yığına yeni bir öğe ekler."""
        self.items.append(i)

    def geri_al(self):
        self.items.pop()


word_belgem = Stack()

word_belgem.islem_yap('Merhaba benim adim Emre')
word_belgem.islem_yap('Merhaba hos geldin')
word_belgem.items
word_belgem.geri_al()
word_belgem.items


# Python'da bos listeler False olarak doner.

emre = []
bool(emre)
not emre

not True
# Yani bos liste false olarak doner,
# not ise mantiksal sinamayi tersine cevirir.


## Slaytta yer alan empty, push, pop, size, peek yapilarindan olusan bir slayt tanimlayalim

class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        '''Normalde liste bossa bu fonksiyon False
        donecek ama ve True donmesini istiyorum. Cunku
        tetikleyici olarak kullanacagim'''
        return not self.items

    def push(self, i):
        """Yığına yeni bir öğe ekler."""
        self.items.append(i)

    def pop(self):
        """Yığından en üstteki öğeyi çıkarır ve döndürür."""
        if self.empty():
            print("Pop from empty stack")
        else:
            return self.items.pop()

# Alternatif kullanim

    def pop(self):
        """Yığından en üstteki öğeyi çıkarır ve döndürür."""
        if self.empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()


    def size(self):
        """Yığındaki öğe sayısını döndürür."""
        return len(self.items)

    def peek(self):
        """Yığının en üstündeki öğeyi döndürür."""
        if self.empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]


# Yığın örneğini oluştur
word_belgem = Stack()

# Yığına öğeler ekleyin
word_belgem.push("Merhaba")
word_belgem.push("Dünya")

# Yığının en üstündeki öğeyi görüntüle
print(word_belgem.peek())  # Çıktı: Dünya

# Yığından öğeleri çıkar ve görüntüle
print(word_belgem.pop())  # Çıktı: Dünya
print(word_belgem.pop())  # Çıktı: Merhaba

# Yığının boş olup olmadığını kontrol et
print(word_belgem.empty())  # Çıktı: True