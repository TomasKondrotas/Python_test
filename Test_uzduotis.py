# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:53:01 2021

@author: tomas
"""
#1
numbers = []
while True:
    try:
        a = input("enter your list")
        a=a.split(",")
        for i in a:
            numbers.append(int(i))
            a= numbers
            
        print("everything ok")
        break
    except ValueError as e:
        print(e.args)
    except:
        print("Something wrong. Try again...")





print("suma",sum(a))
print(max(a))
print(min(a))
print(len(a))

print(a[2:4])
for i in a:
    if i > 10:
        print(i)
print(list(reversed(a))) # Reverse entered list
print(sorted(a)) # sorted list 
print(list((sorted(a, reverse=True)))) # reverse sorted list desending

#2
sort_me = ["Kaunas", "Vilnius", "Alytus", "Klaipeda", "Varena", "Druskininkai", "Klaipeda"]
sort_me = sorted(sort_me, key=len)
print(sort_me)
sort_me = list(reversed(sort_me))
print(sort_me)

#4
sort_me = { 
     "a": [7, 1, 9], 
     "b": [8, -4, 3],
     "c": [9, 10, 151],
     "d": [-3, 9, 11]
            }
sort_me = sorted(sort_me, key=sort_me.get(1)
print(sort_me)
