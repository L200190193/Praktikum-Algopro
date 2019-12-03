import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print"Server penjawab otomatis sudah siap"
data = ''
kamus = {'nama': 'Luthfiana Nur Hayati', 'NIM': 'L200190193', 'angkatan': '2019', 'keluar': 'siap!!'}
while data.lower() != 'q':
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower() == 'q':
            s.close()
            break
        print 'Perintah:', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, perintah tidak dimengerti')
