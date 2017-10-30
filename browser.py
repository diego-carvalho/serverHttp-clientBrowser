#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

if len(sys.argv) < 1:
    print 'comando de execução faltando parametro, exemplo: python browser.py index.html 8080'
    sys.exit(1)
else:

    path = sys.argv[1]
    if 'http' in path:
        path = path.split('://')[1]

    path = path.split('/')

    bind_ip = path[0]

    file_r = "/".join(path[1:])

    if len(sys.argv) == 3:
        bind_port = int(sys.argv[2])
    else:
        bind_port = 80


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((bind_ip, bind_port))


s = "GET /" + file_r + " HTTP/1.1\nHost: " + bind_ip + ":" + str(bind_port) + "\nConnection: keep-alive\nCache-Control: max-age=0\nUser-Agent: Mozilla/5.0(X11;Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/62.0.3202.75Safari/537.36\nUpgrade-Insecure-Requests: 1\nAccept: text/html, application/xhtml + xml, application/xml;q=0.9, image/webp, image/apng, /;q=0.8\nAccept-Language: pt-BR, pt;q=0.9, en-US;q=0.8, en;q=0.7\n\n\n"


#client.send('GET /' +file_r+ ' HTTP/1.1\r\nHost: {}.{}\r\n\r\n'.format('dcomp', 'ufsj.edu.br'))
client.send(s)

response = client.recv(1024)

if file_r[len(file_r) - 1] == '/':
    s = str(response).split("<li>")
    s = s[1:]
    for i in s:
        r = i.split("</li>")
        print r[0]
else:
    cod = response.split()[1]
    if cod == '200':
        f = file_r.split('/')
        file_out = f[len(f) - 1]
        file_o = open('downloads/'+file_out, 'w')
        file_o.write("".join(response.split('\n\n')[1:]))
    print response
