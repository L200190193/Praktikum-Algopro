import shelve

data = open("L200190193.txt", "r")
NIM = data.readline()
TTL = data.readline()
NAMA = data.readline()
KOTA = data.readline()
data.close()

F = shelve.open("Luthfi.txt")
F["berkas"] = [NIM, TTL, NAMA, KOTA]
print(F["berkas"][0])
print(F["berkas"][1])
print(F["berkas"][2])
print(F["berkas"][3])
