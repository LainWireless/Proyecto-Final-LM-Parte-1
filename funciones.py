import json
import requests
import os
import urllib
from urllib import request
def personajes(ts,key,khash,nombre):
    name=[]
    ident=[]
    desc=[]
    r=requests.get(f"https://gateway.marvel.com/v1/public/characters?nameStartsWith={nombre}&ts={ts}&apikey={key}&hash={khash}")
    datos = r.json()
    for i in datos.get("data").get("results"):
        name.append(i.get("name"))
        ident.append(i.get("id"))
        desc.append(i.get("description"))
        print(f"Nombre: {name[-1]}")
        print(f"ID: {ident[-1]}")
        print(f"Descripción: {desc[-1]}")
        print()
def series(ts,key,khash,nombre,año):
    name=[]
    ident=[]
    desc=[]
    types=[]
    creators1=[]
    creators=[]
    r=requests.get(f"https://gateway.marvel.com/v1/public/series?titleStartsWith={nombre}&startYear={año}&ts={ts}&apikey={key}&hash={khash}")
    datos = r.json()
    for i in datos.get("data").get("results"):
        name.append(i.get("title"))
        ident.append(i.get("id"))
        desc.append(i.get("description"))
        types.append(i.get("type"))
        creators.append(i.get("creators").get("items"))
        print(f"Nombre: {name[-1]}")
        print(f"ID: {ident[-1]}")
        print(f"Descripción: {desc[-1]}")
        print(f"Tipo: {types[-1]}")
        for j in creators[-1]:
            creators1.append(j.get("name"))
            print(f"Creador: {creators1[-1]}")
        print()
def comics(ts,key,khash,id):
    name=[]
    ident=[]
    desc=[]
    format=[]
    seriesname=[]
    prices=[]
    r=requests.get(f"https://gateway.marvel.com/v1/public/comics?characters={id}&ts={ts}&apikey={key}&hash={khash}")  
    datos = r.json()
    for i in datos.get("data").get("results"):
        name.append(i.get("title"))
        ident.append(i.get("id"))
        desc.append(i.get("description"))
        format.append(i.get("format"))
        seriesname.append(i.get("series").get("name"))
        prices.append(i.get("prices"))
        print(f"Nombre: {name[-1]}")
        print(f"ID: {ident[-1]}")
        print(f"Descripción: {desc[-1]}")
        print(f"Formato: {format[-1]}")
        print(f"Serie: {seriesname[-1]}")
        for j in prices[-1]:
            print(f"Precio: {j.get('price')}")
        print()