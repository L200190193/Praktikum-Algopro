import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50005))
s.listen(5)
print "Server siap"
perintah =''
r=0
phi=3.14
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == 'keluar':
            komm.send('done')
            s.close()
            break
        print "pesan:",perintah
        if len(item)==2:
            if perintah == 'jari-jari':
                r=int(item[1])
                komm.send('jari-jari disimpan')
            else:
                komm.send('Pesan tidak diketahui')
        elif perintah == 'hitung':
            L=float(4*phi*r**2)
            response ='Luas Bola dengan r {} adalah {}'.format(phi,r,L)
            komm.send(response)
        else:
            komm.send('Pesan tidak diketahui')
