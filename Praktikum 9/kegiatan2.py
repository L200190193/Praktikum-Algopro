data = open("L200190193.txt", "w")
data.write("L200190193\n")
data.write("02-14-2001\n")
data.write("Luthfiana Nur Hayati\n")
data.write("Sragen")
data.close()

data = open("L200190193.txt", "r")
NIM = data.readline()
TTL = data.readline()
NAMA = data.readline()
KOTA = data.readline()
data.close()

print(NAMA)
print(KOTA, TTL)
print(NIM)
