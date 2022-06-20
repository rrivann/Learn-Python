mobil = ['bmw', 'forche', 'tiger', 'supra']

# for g in mobil:
#     print(g)
#     print(len(g))

# # string sebagai iterable

# bakwan = 'bakwan'

# for i in bakwan:
#     print(i)

buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

daftarBelanja = [mobil, buah, sayur]

for subDaftarBelanja in daftarBelanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(20*'=')
        print(komponen)
