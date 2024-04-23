# Sözlük oluşturma:
my_dict = {'anahtar1': 'değer1', 'anahtar2': 'değer2', 'anahtar3': 'değer3'}

# Boş bir sözlük oluşturma:
empty_dict = {}

# Sözlük elemanlarına erişim:
value = my_dict['anahtar1']  # 'değer1'

# Sözlük uzunluğu:
length = len(my_dict)

# Sözlük elemanlarını değiştirme veya ekleme:
my_dict['anahtar4'] = 'değer4'  # Yeni bir anahtar-değer çifti ekleme veya var olanı güncelleme

# Sözlük elemanlarını silme:
del my_dict['anahtar2']  # 'anahtar2' anahtarını ve değerini silme
popped_value = my_dict.pop('anahtar3')  # 'anahtar3' anahtarını çıkarma ve değeri döndürme

# Belirli bir anahtarın sözlükte olup olmadığını kontrol etme:
is_in_dict = 'anahtar1' in my_dict  # True veya False döndürür

# Sözlük kopyalama:
copied_dict = my_dict.copy()

# Sözlük temizleme:
my_dict.clear()

# Tüm anahtarlar, değerler ve öğeler:
keys = my_dict.keys()  # Tüm anahtarları alır
values = my_dict.values()  # Tüm değerleri alır
items = my_dict.items()  # Tüm öğeleri alır (anahtar-değer çiftleri)

# Sözlük döngüsü:
for key, value in my_dict.items():
    print(key, value)

# Birden çok sözlük birleştirme:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}  # {'a': 1, 'b': 3, 'c': 4}

# Sözlük elemanlarını sıralama:
sorted_dict = dict(sorted(my_dict.items()))  # Anahtara göre artan sıralama

# Eşsiz (unique) değerleri alarak yeni bir sözlük oluşturma:
unique_values_dict = dict.fromkeys(my_dict.values())

# Sözlük elemanlarının frekanslarını alma:
from collections import Counter
frequency = Counter(my_dict.values())
