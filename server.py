#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import sys

if len(sys.argv) < 3:
    print 'comando de execução faltando parametro, exemplo: python server.py index.html'
    print 'para utilizar o browser do seu computador em nosso servidor, inicie o servidor como python server.py mod-browser porta'
    sys.exit(1)
else:
    bind_ip = '0.0.0.0'
    bind_port = int(sys.argv[2])
    file_r = sys.argv[1]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max connections

print 'Listening on {}:{}'.format(bind_ip, bind_port)


def handle_client_connection(c):
    print 'threading listering'
    request = c.recv(1024)
    print 'Received {}'.format(request)

    method = request.split()[0]
    print method

    if method != 'GET':
        print 'metodo ' + method + ' ainda não implementado, apenas GET'

    f = file_r

    if f == 'mod-browser':
        f = request.split()[1]
        if f == '/':
            f = 'index.html'
        else:
            f = f[1:]

    if f[len(f) - 1] == '/':
        if file_r != 'mod-browser':
            files = os.listdir(f)
            files_s = ""
            for i in files:
                path = os.path.realpath(f)
                files_s +=""+ i
            response = """
                """+ files_s +"""
            """
        else:
            files = os.listdir(f)
            files_s = ""
            for i in files:
                path = os.path.realpath(f)
                files_s +="<li>"+ i +"</li>"
            response = """
                <!DOCTYPE html>
                <html lang='pt-br'>
                <meta charset="UTF-8">
                <body>
                <ul>
                """+ files_s +"""
                </ul>
                </body>
                </html>
            """
    else:
        if os.path.isfile(f):
            file_o = open(f, 'r')
            response = "".join(file_o.readlines())
        else:
            response = """
                <!DOCTYPE html>
                <html lang='pt-br'>
                <meta charset="UTF-8">
                <body>
                <h1>Arquivo """ + f + """ não existe</h1>
                </body>
                </html>
            """
            print 'HTTP/1.0 404 ERROR\n'
            print 'Content-Type: text/html\n'
            print '\n'
            print response
            c.send('HTTP/1.0 404 ERROR\n')
            c.send('Content-Type: text/html\n')
            c.send('\n')
            c.send(response)
            c.close()
            return
            
    print response
    c.send('HTTP/1.0 200 OK\n')
    c.send('Content-Type: text/html\n')
    c.send('\n')
    c.send(response)
    c.close()


while True:
    client_sock, address = server.accept()
    print 'Accepted connection from {}:{}'.format(address[0], address[1])
    client_handler = threading.Thread(target=handle_client_connection, args=(client_sock,))
    client_handler.start()
    # handle_client_connection(client_sock)

