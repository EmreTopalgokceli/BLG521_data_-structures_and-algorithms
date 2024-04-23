# Liste oluşturma:
my_list = [1, 2, 3, 4, 5]

# Boş bir liste oluşturma:
empty_list = []

# Liste elemanlarına erişim:
first_element = my_list[0]  # 1. eleman
last_element = my_list[-1]  # Son eleman

# Liste dilimleme (slicing):
sliced_list = my_list[1:3]  # 2. ve 3. elemanlar
sliced_list_from_start = my_list[:3]  # Listenin başından 3. elemana kadar
sliced_list_to_end = my_list[2:]  # 3. elemandan listenin sonuna kadar

# Liste uzunluğu:
length = len(my_list)

# Liste elemanlarını değiştirme:
my_list[0] = 10  # 1. elemanı 10 ile değiştirme

# Liste elemanlarını ekleme:
my_list.append(6)  # Listenin sonuna 6 ekleme
my_list.insert(2, 20)  # 3. konuma (sıfırdan başlayarak) 20 ekleme

# Liste elemanlarını silme:
my_list.remove(3)  # İlk 3 değerini silme
popped_element = my_list.pop()  # Son elemanı çıkarma ve döndürme
del my_list[1]  # 2. elemanı silme

# Liste birleştirme:
combined_list = my_list + [7, 8, 9]

# Liste kopyalama:
copied_list = my_list.copy()

# Liste temizleme:
my_list.clear()

# Liste döngüsü:
for item in my_list:
    print(item)

# Liste sıralama:
sorted_list = sorted(my_list)  # Artan sıralama
reverse_sorted_list = sorted(my_list, reverse=True)  # Azalan sıralama
my_list.sort()  # Listenin kendisini sıralama
my_list.sort(reverse=True)  # Listenin tersine sıralama

# Belirli bir değerin listeye ait olup olmadığını kontrol etme:
is_in_list = 10 in my_list  # True veya False döndürür

# Liste elemanlarını ters çevirme:
reversed_list = my_list[::-1]

# Liste elemanlarının toplamını alma:
total = sum(my_list)

# Liste elemanlarını çarpma:
product = 1
for num in my_list:
    product *= num

# Liste elemanlarını dizeye dönüştürme:
list_as_string = ','.join(map(str, my_list))

# Liste elemanlarını karesini alma (List Comprehension kullanımı):
squared_list = [x**2 for x in my_list]

# Liste elemanlarını filtreleme (List Comprehension kullanımı):
filtered_list = [x for x in my_list if x > 3]

# Liste elemanlarını dizeye çözme:
string_list = list("hello")

# Liste elemanlarının birleştirilmesi:
joined_string = ''.join(string_list)

# Liste elemanlarının eşsiz (unique) olmasını sağlama:
unique_list = list(set(my_list))

# Liste elemanlarının frekanslarını alma:
from collections import Counter
frequency = Counter(my_list)
