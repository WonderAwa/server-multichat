# -- coding: utf-8 --
#!/usr/bin/python3
import select
import socket

HOST = ""
PORT = 7777
sserveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sserveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sserveur.bind((HOST, PORT))
sserveur.listen(1)
l = []
nc={}
print('Bienvenue dans le serveur chat')
while True:
    # on récupère la liste des socket clients sur lesquels 
    # on peut lire de la donnée (la fonction .recv termine  
    # sans delai)
    r_socks, _, _ = select.select(l + [sserveur],[],[])
    
    for sock in r_socks:
        if sock == sserveur:
            # cas d'une nouvelle connexion
            sc, addr = sserveur.accept()
            print("client connecté", addr)
            # on l'ajoute à liste des clients
            l.append(sc)
        else:
            # on récupère la donnée qui était en attente
            data = sock.recv(1500)
            
            if data == b"" or data == b"\n":
                # fin de connexion de la part du client
                try:
                    print("client déconnecté", sock.getpeername())
                    sock.close()
                except:
                    print("Déconnecté")
                l.remove(sock)
          
            else:
                decoded=data.decode()
                dl=decoded.split(' ',maxsplit=1)
                 
                if dl[0]!='NICK'and dl[0]!='WHO\n' and dl[0]!='MSG' and dl[0]!='KILL' and dl[0]=='QUIT':
                    d= 'Message invalide \n'
                    sock.sendall(d.encode())
                    
                
                if dl[0]=='NICK':
                    if len(dl)>=2:
                        nc[sock]=dl[1]
                        post,add=sock.getpeername()
                        print('client "{}" ,"{}"=>"{}"'.format('localhost',add,nc[sock].rstrip('\n')))

                                                       
                if dl[0]=='WHO\n':
                    msg= '[serveur chat]'
                    for i in nc:
                        msg += ' ' +nc[i].rstrip('\n')
                    sock.send((msg + '\n').encode())
                                    
                if dl[0]=='MSG':
                    msg="["+nc[sock].rstrip('\n')+"]" +' ' + dl[1]
                    for c in l:
                        if c != sock:
                            c.sendall(msg.encode())
                            print(msg.encode(),'envoyé à', nc[c].rstrip('\n'))
                            
                if dl[0]=='QUIT':
                    msg="[" + nc[sock].rstrip('\n') + "]" + dl[1]
                    for c in l:
                        if c != sock:
                            c.send(msg.encode())
                    print('client déconnecté "{}"'.format(nc[sock].rstrip('\n')))
                    sock.close()
                    l.remove(sock)
                    del nc[sock]
                    continue

                if dl[0]=='KILL':
                    h=dl[1].split(' ',maxsplit=1)
                    vir=0
                    for i in nc:
                        if nc[i].rstrip('\n')==h[0]:
                            vir=i
                            print('client déconecté pour abus "{}"'.format(nc[vir]))
                            msg = "["+nc[sock].rstrip('\n')+"]" +' '+h[1]
                            i.sendall(msg.encode())
                            i.close()
                            l.remove(i)
                            continue
                    del nc[vir]