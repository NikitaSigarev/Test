# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
pages = 100
page_str = 50
str_syn = 25
syn_byte = 4
MBITE_BYTE = 1024 ** 2

disk_size_byte = disk_size * MBITE_BYTE
book_size = pages * page_str * str_syn * syn_byte
anount = disk_size_byte // book_size

print("Количество книг, помещающихся на дискету:", int(anount))
