#!/usr/bin/env python
# coding: utf-8

import sys
from PIL import Image #Manejo de imagenes.
from PIL.ExifTags import TAGS #Para los metadatos


def Metadata(file,im):
    f = open(file,'a')
    image = Image.open(im)
    data = image.getexif()
    for tagid in data:
        tagname = TAGS.get(tagid,tagid)
        value = data.get(tagid)
        f.write(f"{tagname:25}: {value}\n")
    f.write("\n")
    f.write("\n")
    f.close()
    return file


def CFile(Fname):
    file = open(Fname,'a')
    file.close()
    return file

def CheckFile (NameFile):#Verifica el archivo.
    try:
        file = open(NameFile,'r')
        print('The file exist....')
        file.close()
    except FileNotFoundError: #Si no existe llama a la función CFile()
        print('Your file does not exist')
        print('But we have created ones as {}'.format(NameFile))
        return CFile(NameFile)
        
def CheckImage(NameImag): #Verifica si la imagen existe
    try:
        img = Image.open(NameImag)
    except:
        print("Did not found the image...")
        sys.exit(1)



    




