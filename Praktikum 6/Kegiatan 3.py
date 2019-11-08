Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Luthfiana Nur Hayati"
>>> NIM = "L200190193"
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # karena data "X" telah diubah menjadi tipe data integer
>>> type(b)
<class 'int'>
>>> # karena data "Nama" mempunyai instruksi "len"
>>> a / b
59.65
>>> # karena hasil dari 1193 bagi 20 adalah 59.65
>>> a // b
59
>>> # karena tanda "//" artinya pembagian dengan pembulatan ke bawah
>>> 10 * (a - 999)
1940
>>> # karena hasil dari "a" dikurang 999 adalah 194, lalu 194 dikali dengan 10 hasilnya 1940
>>> b ** 2
400
>>> # karena tanda "**" artinya pangkat
>>> a % b
13
>>> # karena tanda "%" artinya sisa hasil pembagian
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # karena "12.5" adalah bentuk bilangan desimal
>>> a / c
95.44
>>> # karena hasil dari 1193 bagi 12.5 adalah 95.44
>>> a // c
95.0
>>> # karena tanda "//" artinya pembagian dengan pembulatan ke bawah
>>> a % c
5.5
>>> # karena tanda "%" artinya sisa hasil pembagian
>>> c > b
False
>>> # karena c lebih kecil dari b atau c < b
>>> type(c > b)
<class 'bool'>
>>> # karena "c > b" adalah bentuk perbandingan menghasilkan False/True
>>> a > b and b > c
True
>>> # karena "a > b" adalah True dan "b > c" adalah True
>>> a > 1100 or b < 10
True
>>> # karena "a > 1100" adalah True atau "b < 10" adalah False
