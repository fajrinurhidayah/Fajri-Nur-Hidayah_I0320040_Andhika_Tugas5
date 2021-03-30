#Soal 1
#Program menyapa pengunjung

nama = input('Masukkan nama: ')                                 #input nama
j_k = input('Masukkan jenis kelamin: ')                         #input jenis kelamin

#program
if j_k == 'laki-laki':
    print('Selamat datang, Mr. ', nama, ', have a nice day!' )
else:
    print('Selamat datang, Mrs.', nama, ', have a nice day!')

