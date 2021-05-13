Hello! 

This is my personal take on a simple proxy rotator that is intended to be imported localy as a python module to help easily manage a proxy pool for python configs utilizing "Requests"

To Use:


- Add the folder to your root project directory

- fill the https/socks5/http etc files with proxies in the following format
  * NO AUTH = 103.55.62.88:1080
  * AUTH = user:pass@103.55.69.88:1080

- Import the files as a module to your respective project file

- Create the proxy pool object by calling --- new = rotate.proxyPool('/path/to/proxy/file/socks5.txt', 'socks5') ---

- Each time you would like a random proxy call ---  new.get_rand() --- to get a random proxy from your list formatted for the type of connection specified when creating the proxyPool object


                                                                        * * *


To check the that the rotator is working properly, use this example
code to print the DNS information for each proxy. 
====================================================================


new = rotate.proxyPool('/home/kali/proxy_rotator/socks5.txt', 'socks5')

while True:

  randProx = new.get_rand()
  proxy = {'http': randProx,
            'https': randProx}
  
  g = session.get("http://ip-api.com/json/", proxies=proxy)
  print(g.text)
  
  

                                                                        * * *


Any feedback or, input welcome and appreciated!




  
