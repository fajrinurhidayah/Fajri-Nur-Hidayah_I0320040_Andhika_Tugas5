#Soal 2
print('-'*10 + 'KONVERSI NILAI'+'-'*10)
nama = input('Masukkan nama: ')                      #input nama
nilai = int(input('Masukkan nilai: '))               #input nilai

#Program konversi
if nilai >100 or nilai < 0:
    print('Nilai tidak valid untuk dikonversi')
elif nilai >= 85:
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah A.')
elif nilai >= 80:
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah A-.')
elif nilai >= 75:
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah B+.')
elif nilai >= 70:
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah B.')
elif nilai >= 65:
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah C+.')
elif nilai >= 60:
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah C.')
else:
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah E.')