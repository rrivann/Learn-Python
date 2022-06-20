# # episode latihan logika dan komparasi

# # membuat gabungan area rentang dari angka

# # +++++++3---------10++++++++
# inputUser = float(input(
#     'masukan angka yang bernilai\n kurang dari 3\n atau \nlebih besar dari 10\n : '))

# # +++++3------------
# # memeriksa angka kurang dari 3
# isKurangDari = (inputUser < 3)
# print('kurang dari 3 =', isKurangDari)

# # ---------------10+++++++
# # memeriksa angka lebih dari 10
# isLebihDari = (inputUser > 10)
# print('lebih dari 10', isLebihDari)

# isCorrect = isKurangDari or isLebihDari
# print('angka yang anda masukkan:', isCorrect)


# # --------3+++++++++10--------
# # kasus irisan
# print('\n', 10*'=', '\n')
# inputUser = float(input(
#     'masukan angka yang bernilai\n lebih dari 3\n dan \nkurang dari 10\n : '))

# # -----3++++++++++++++++++++++++
# # lebih dari 3
# isLebihDari = inputUser > 3
# print('lebih dari 3=', isLebihDari)

# # +++++++++++++++10-------------
# # kurang dari 10
# isKurangDari = inputUser < 10
# print('kurang dari 10=', isKurangDari)

# # --------3+++++++++10--------
# isCorrect = isKurangDari and isLebihDari
# print('angka yang anda masukkan:', isCorrect)


# PR
# --------0+++++++++5--------8++++++11---------
# kasus irisan
print('\n', 10*'=', '\n')
inputUser = float(input(
    'masukan angka yang bernilai\n lebih dari 0\n dan \nkurang dari 5\n atau lebih dari 8\n dan \nkurang dari 11\n  : '))

isLebihDari = inputUser > 0 or inputUser > 8
print('lebih dari 0=', isLebihDari)


isKurangDari = inputUser < 5 or inputUser < 11
print('kurang dari 5=', isKurangDari)

isCorrect = isKurangDari and isLebihDari
print('angka yang anda masukkan:', isCorrect)

# +++++++0---------5++++++++8-----11++++++
inputUser = float(input(
    'masukan angka yang bernilai\n kurang dari 0\n atau \nlebih besar dari 5\n dan kurang dari 8\n atau \nlebih besar dari 11\n  : '))

# +++++0------------
# memeriksa angka kurang dari 0
isKurangDari = (inputUser < 0 or inputUser < 8)
print('kurang dari 0 =', isKurangDari)

# ---------------10+++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 5 or inputUser > 11)
print('lebih dari 10', isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukkan:', isCorrect)
