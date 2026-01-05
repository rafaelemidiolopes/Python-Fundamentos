import urllib
import urllib.request
try:
    urllib.request.urlopen('http://www.pudim.com')
except urllib.error.URLError: 
    print('O site está inacessível no momento! ')
else: 
    print('O site está acessível! ')