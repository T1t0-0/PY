# TODO Найдите количество книг, которое можно разместить на дискете
#Характеристики памяти
disk_size_mbyte = 1.44
symbol_size_byte = 4

#Характеристики книги
page = 100
str_ = 50
symbols = 25

total_symbols = page * str_ * symbols
book_size = total_symbols * symbol_size_byte
numbers_of_books = disk_size_mbyte / (book_size / (1024 * 1024))
print("Количество книг, помещающихся на дискету:", round(numbers_of_books))
