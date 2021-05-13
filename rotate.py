import requests
import random


class proxyPool:
    def __init__(self, pList, protoent):
        def format_proxy(protocol):
            opts = {'socks': 'socks://', 'socks5': 'socks5://', 'https': 'https://', 'http': 'http://'}
            return opts[protocol]

        def make_list(list):
            ProxyObj = open(list, "r").read().splitlines()
            return ProxyObj

        self.protocol = format_proxy(protoent)
        self.pool = make_list(pList)


    def get_rand(self, dns = False):
        temp = self.protocol + self.pool[random.randrange(0, len(self.pool))]
        if dns == True:
            print(requests.get("http://ip-api.com/json/", proxies={"http": temp}).text)
            return temp
        else:
            return temp


