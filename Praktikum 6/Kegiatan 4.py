Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Luthfiana Nur Hayati"
>>> NIM = 193
>>> Tinggi = 1.53
>>> Berat = 49
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # karena data "Aku" ditulis dengan tanda kurung
>>> Aku[0]
2001
>>> # karena objek pertama di data "Aku" adalah "TahunLahir", nilai dari "TahunLahir" adalah 2001
>>> a = NIM % 4; Aku[a]
49
>>> # karena sisa hasil bagi dari 193 dibagi 4 adalah 1, jadi hasil dari Aku[1] adalah 49
>>> type(Aku[a])
<class 'int'>
>>> # karena nilai dari "Berat" adalah 1, 1 adalah data tipe integer
>>> Aku[a:4]
(49, 1.53, 193)
>>> # karena data yang diminta dari "Aku" mulai dari data ke-1 sampai ke-3 yaitu "Berat", "Tinggi", "NIM"
>>> type(Aku[4])
<class 'str'>
>>> # karena data ke-4 dari "Aku" adalah "Nama", nilai dari data "Nama" adalah "Luthfiana Nur Hayati"
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> # karena data tuple tidak dapat diganti
>>> type(Data)
<class 'list'>
>>> # karena data "Data" ditulis dengan tanda kurung siku
>>> type(Data[4])
<class 'str'>
>>> # karena nilai dari "Nama" adalah "Luthfiana Nur Hayati", "Luthfiana Nur Hayati" adalah data tipe string
>>> Data[4][5]
'i'
>>> # karena data dari "Nama" adalah "Luthfiana Nur Hayati" yang indeks ke-5 adalah 'i'
>>> Data[4][a:6]
'uthfi'
>>> # karena data dari "Nama" adalah "Luthfiana Nur Hayati", lalu indeks yang diminta dari 1 samapai 6, nilainya adalah "uthfi"
>>> Data[0] = 'ok'; Data
['ok', 49, 1.53, 193, 'Luthfiana Nur Hayati']
>>> # karena data "TahunLahir" diubah menjadi 'ok' dan menampilkan "Data"
>>> Data[-a]
'Luthfiana Nur Hayati'
>>> # karena yang diminta data "Nama" yaitu "Luthfiana Nur Hayati"
>>> range(a)
range(0, 1)
>>> # karena "range(1)" adalah range dari 0 sampai 1 
