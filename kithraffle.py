#Thank you to @fockniketalk
import requests, time, re, sys, random
from random import getrandbits

url = 'https://kithnyc.typeform.com/to/ySnFiu'
print("Kith Raffle Script for Futurecraft 4D @allen56_")

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

list1 = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]		   
sizes = ['US 6','US 7', 'US 8', 'US 8.5', 'US 9', 'US 9.5', 'US 10' ,'US 10.5' ,'US 11' ,'US 11.5' ,'US 12', 'US 13']



def main(limit):
    for i in range(0, limit):
        payload ={
            'form[textfield:OSwjNf51Vlq5]': list1[random.randint(0, 99)],
            'form[textfield:WS8KFzUfJKZ6]': list1[random.randint(0, 99)],
            'form[email:mSTAlyznz1A1]': 'allencao98+{}@gmail.com'.format(getrandbits(40)), #change to your email
			'form[list:Z89n81xJhqQK][choices]': 'Kith Soho', # don't change
            'form[list:kXPnX9LjujQw][choices]': 'Men\'s 8',
            'form[textfield:p6P2thoLnUI4]': 'bdfmlk55',
            'form[landed_at]': '1516330529', # don't change
            'form[language]': 'en', # don't change
            'form[token]': 'e5455f13bd09203c7f5f0b433129e116$2y$11$e2dJZC0zIXZQK1pxbSZbL.LzJE2QS5SFRX2Z7Lk/oL/j6JicEpiXS'
            }
        resp = requests.post(url, data=payload, headers=headers)
        if any(re.findall(r'success', str(resp.text), re.IGNORECASE)):
            print(time.strftime("%H:%M:%S") + " / Successfully entered, @allen56_" )
        else:
            print(time.strftime("%H:%M:%S") + " / Could not enter!")

main (1000) # change to the amount u want, currently 100 times.
exit()
