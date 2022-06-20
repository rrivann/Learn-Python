# kita belajar casting
# merubah dari satu tipe ketipe lain
# tipe data =int,float,str,bool

# INTEGER
print('======INTEGER======')
data_int = 9
print('data = ', data_int, 'tipe = ', type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_boolean = bool(data_int)  # akan false jika nilai int = 0
print('data = ', data_float, 'tipe = ', type(data_float))
print('data = ', data_str, 'tipe = ', type(data_str))
print('data = ', data_boolean, 'tipe = ', type(data_boolean))


# FLOAT
print('======FLOAT======')
data_float = 9.9
print('data = ', data_float, 'tipe = ', type(data_float))

data_int = int(data_float)  # akan dibulatkan ke bawah
data_str = str(data_float)
data_boolean = bool(data_float)  # akan false jika nilai float = 0
print('data = ', data_int, 'tipe = ', type(data_int))
print('data = ', data_str, 'tipe = ', type(data_str))
print('data = ', data_boolean, 'tipe = ', type(data_boolean))

# BOOLEAN
print('======BOOLEAN======')
data_boolean = False
print('data = ', data_boolean, 'tipe = ', type(data_boolean))

data_int = int(data_boolean)  # akan dibulatkan ke bawah
data_str = str(data_boolean)
data_float = float(data_boolean)  # akan false jika nilai float = 0
print('data = ', data_int, 'tipe = ', type(data_int))
print('data = ', data_str, 'tipe = ', type(data_str))
print('data = ', data_float, 'tipe = ', type(data_float))


# STRING
print('======STRING======')
data_str = '10'
print('data = ', data_str, 'tipe = ', type(data_str))

data_int = int(data_str)  # string harus angka
data_boolean = bool(data_str)  # false jika str kosong
data_float = float(data_str)  # string harus angka
print('data = ', data_int, 'tipe = ', type(data_int))
print('data = ', data_boolean, 'tipe = ', type(data_boolean))
print('data = ', data_float, 'tipe = ', type(data_float))
