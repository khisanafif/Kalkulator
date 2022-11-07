
print('='*45)
print('~'*10 ,'KALKULATOR SEDERHANA ', '~'*11)
x= 1
# Program ini dibuat oleh Khisan Afif Ainur Rohim(222410102075), Yohannes Christtovian Wahyu Nugroho (222410102071), Abelta Putra Efendi(222410102094)
while x:
     a= int(input('   Angka Pertama = '))
     print('~'*45)
     b= int(input('   Angka Kedua = '))
     print('~'*45)

     print('''  Jenis Jenis Operasi yang dapat digunakan:
    	1. [+](Penjumlahan)
    	2. [-] (Pengurangan)
    	3. [×] (Perkalian )
    	4. [÷] (Pembagian ''')

     operasi = input('  Masukkan operasi: ')
  
     print('~'*45)
     if operasi == '1': 
          print('  Hasil dari',a,'+',b,'=',a+b)
     elif operasi == '2': 
          print('  Hasil dari',a,'-',b,'=',a-b)
     elif operasi == '4': 
          print('  Hasil dari',a,'÷',b,'=',a/b)
     elif operasi == '3':
          print('  Hasil dari',a,'×',b,'=',a*b)
    
     else:
          print('operasi apaan ni? ')
          print('='*45)
     print('~'*45)
     print('Masukkan 1 untuk mengulang dan Masukkan 2 untuk berhenti')
     print('~'*45)
     x= int(input('Apakah anda ingin mengulangi operasi? = '))
     print('~'*45)
     if x== 2:
          print('Terimakasih telah menggunakan program kami')
          print('~'*45)
          break
     elif x == 1 :
          print(x)
     else: pass