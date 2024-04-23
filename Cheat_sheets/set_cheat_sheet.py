# Küme oluşturma:
my_set = {1, 2, 3, 4, 5}

# Boş bir küme oluşturma:
empty_set = set()

# Küme elemanlarını ekleme:
my_set.add(6)

# Birden çok elemanı kümeye ekleme:
my_set.update([7, 8, 9])

# Kümeden eleman çıkarma:
my_set.remove(3)  # 3 değerini çıkarır, hata verir eğer 3 kümede yoksa
my_set.discard(10)  # 10 değerini çıkarır, hata vermez eğer 10 kümede yoksa
popped_element = my_set.pop()  # Bir eleman çıkarır ve döndürür

# Küme elemanlarını silme:
my_set.clear()

# Küme elemanlarına erişim:
for element in my_set:
    print(element)

# Küme elemanlarını sıralama:
sorted_set = sorted(my_set)

# Küme elemanlarının uzunluğu:
length = len(my_set)

# Belirli bir elemanın kümede olup olmadığını kontrol etme:
is_in_set = 10 in my_set  # True veya False döndürür

# Küme kopyalama:
copied_set = my_set.copy()

# Küme birleştirme:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Birleşim kümesi: {1, 2, 3, 4, 5}
intersection_set = set1.intersection(set2)  # Kesişim kümesi: {3}
difference_set = set1.difference(set2)  # Fark kümesi: {1, 2}
symmetric_difference_set = set1.symmetric_difference(set2)  # Simetrik Fark kümesi: {1, 2, 4, 5}

# Alt küme (subset) ve süper küme (superset) kontrolü:
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)

# Kümelerin eşitliğini kontrol etme:
is_equal = set1 == set2
