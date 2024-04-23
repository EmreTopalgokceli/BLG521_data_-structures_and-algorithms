# Tuple oluşturma:
my_tuple = (1, 2, 3, 4, 5)

# Tek elemanlı tuple oluşturma:
single_element_tuple = (1,)

# Tuple elemanlarına erişim:
first_element = my_tuple[0]  # 1. eleman
last_element = my_tuple[-1]  # Son eleman

# Tuple dilimleme (slicing):
sliced_tuple = my_tuple[1:3]  # 2. ve 3. elemanlar
sliced_tuple_from_start = my_tuple[:3]  # Başlangıçtan 3. elemana kadar
sliced_tuple_to_end = my_tuple[2:]  # 3. elemandan son elemana kadar

# Tuple uzunluğu:
length = len(my_tuple)

# Tuple elemanlarını birleştirme:
combined_tuple = my_tuple + (6, 7, 8)

# Tuple elemanlarını çoğaltma:
repeated_tuple = my_tuple * 3  # Her elemanı 3 kez tekrarlar

# Tuple içinde belirli bir değerin var olup olmadığını kontrol etme:
is_in_tuple = 3 in my_tuple  # True veya False döndürür

# Tuple elemanlarını ters çevirme:
reversed_tuple = my_tuple[::-1]

# Tuple elemanlarını toplama ve çarpma:
total = sum(my_tuple)  # Elemanların toplamını alır
product = 1
for num in my_tuple:
    product *= num  # Elemanların çarpımını alır

# Tuple elemanlarını sıralama:
sorted_tuple = tuple(sorted(my_tuple))  # Artan sıralama

# Tuple elemanlarını dizeye dönüştürme:
tuple_as_string = ','.join(map(str, my_tuple))

# Tuple elemanlarını eşsiz (unique) elemanlarla diziye dönüştürme:
unique_elements_tuple = tuple(set(my_tuple))

# Tuple elemanlarını filtreleme:
filtered_tuple = tuple(filter(lambda x: x > 3, my_tuple))

# Tuple elemanlarının frekanslarını alma:
from collections import Counter
frequency = Counter(my_tuple)
