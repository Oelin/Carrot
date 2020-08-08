from requests import session
from re import findall, search
from urllib.parse import urlparse as parse
from os import system
from sys import argv
from json import dumps

urlre = 'src|href=["\']([a-zA-Z0-9\./\-%\?=:]+)["\']'


def urls(page, path):
  found = set(findall(urlre, page)) - {''}

  for url in found:
    yield (parse(url).netloc and url) or f'https://{path}/{url}'


def crawl(url, file):
  s = session()
  children = [url]
  visited = set()

  while children:
    current = children.pop(0)
    visited.add(current)

    path = parse(url).path

    try:
      page = s.get(current).text

    except:
      continue

    if len(children) < 32:
      children += list(set(urls(page, path)) - visited)

    # flush visited
    if len(visited) > 300:
      visited = set() 

    # indexing step
    # extract titles
    title = search('<title>(.+)</title>', page)

    if title:
      title = title.group(1)
      try:
         json = dumps({'title': title, 'url': current})
         system(f'echo \'{json}\' >> {file}')
      except:
         print('encountered error, ignoring...')


crawl(argv[1], argv[2])
