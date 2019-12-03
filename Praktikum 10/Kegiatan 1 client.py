import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print "Mesin penjawab otomatis sudah siap"
while pesan.lower() != 'q':
    pesan = raw_input('Perintah: ')
    s.send(pesan)
    if pesan.lower() != 'q':
        response = s.recv(1024)
        print 'Jawab:', response
s.close()
