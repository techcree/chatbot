#ssk
# -*- coding: utf-8 -*-
import random
import os
from requestlist import requests
from randomquestlist import randomquest
                    
print("Hallo!")
print("beenden mit '#'")
print("")

nutzereingabe = ""
while nutzereingabe != "#":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input(">> ")
        
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    
    intelligenteAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in requests:
            print(requests[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(randomquest))
        
    print("")

print("Okay, dann bis zum nächsten Mal")