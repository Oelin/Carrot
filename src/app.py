from subprocess import getoutput
from _thread import start_new_thread as thread
from re import search
from base64 import b64decode
from json import loads, dumps
from socket import socket


with open('./public/index.html') as file:
  index = file.read()


def search_results(keywords):
  # note results are not output encoded. The client must sanitise the output.
  return [*map(loads, getoutput(f'grep -m 15 -iwE \'{" ".join(keywords).replace(chr(0x27), chr(0x20))}\' ./index.lst').split('\n'))]


def listen():
  s = socket()
  s.bind(('', 80))
  s.listen(5)

  while 1:
    try:
      client, _ = s.accept()
      thread(app, (client,))
      print(f'serviced connection from {_}')
    except:
      s.close()


def app(client):
  try:
    message = str(client.recv(4096), 'utf-8')

    if '@' in message:
      query_enc = search('@([a-zA-Z0-9\+\-=]+)@', message).group(1)
      keywords = loads(b64decode(query_enc))

      if type(keywords) == type([]):
        reply = dumps(search_results(keywords))
        mime = 'application/json'
    else:
      reply = index
      mime = 'text/html'

  except:
    reply = 'sorry, something inside me glitched'
    mime = 'text/plain'

  client.send(bytes(f'HTTP/1.1 200 OK\r\n{mime}\r\n\r\n{reply}\r\n\r\n\r\n', 'utf-8'))
  client.close()


listen()
